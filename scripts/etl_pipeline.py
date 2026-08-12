"""
Master ETL pipeline for the Bluestock Mutual Fund Analytics project.

Runs the existing validation, cleaning, and database-loading scripts
in the required order.
"""

from pathlib import Path
import subprocess
import sys


# Project root: one level above the scripts folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


REQUIRED_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
]


PIPELINE_STEPS = [
    "amfi_validation.py",
    "clean_nav.py",
    "clean_performance.py",
    "clean_transactions.py",
    "load_database.py",
]


def check_required_files():
    """Check that all required raw input files exist."""
    missing_files = [
        filename
        for filename in REQUIRED_FILES
        if not (RAW_DIR / filename).exists()
    ]

    if missing_files:
        print("ERROR: Missing required raw files:")
        for filename in missing_files:
            print(f"  - {filename}")
        return False

    return True


def run_script(script_name):
    """Run one ETL script and stop if it fails."""
    script_path = SCRIPTS_DIR / script_name

    print("\n" + "=" * 60)
    print(f"Running: {script_name}")
    print("=" * 60)

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=PROJECT_ROOT,
            check=True
        )
        print(f"SUCCESS: {script_name}")
        return True

    except subprocess.CalledProcessError as error:
        print(f"ERROR: {script_name} failed.")
        print(f"Exit code: {error.returncode}")
        return False

    except FileNotFoundError:
        print(f"ERROR: Script not found: {script_path}")
        return False


def main():
    """Run the complete ETL pipeline."""
    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS - ETL PIPELINE")
    print("=" * 60)

    # Check required directories
    if not RAW_DIR.exists():
        print(f"ERROR: Raw data folder not found: {RAW_DIR}")
        sys.exit(1)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Check required input files
    if not check_required_files():
        sys.exit(1)

    print("\nAll required raw files found.")

    # Run ETL steps in order
    for script_name in PIPELINE_STEPS:
        if not run_script(script_name):
            print("\nETL PIPELINE FAILED.")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()