"""Master entry point for the Bluestock Mutual Fund Analytics project."""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent
ETL_SCRIPT = PROJECT_ROOT / "scripts" / "etl_pipeline.py"


def main():
    """Run the complete ETL pipeline."""
    if not ETL_SCRIPT.exists():
        print(f"ERROR: ETL script not found: {ETL_SCRIPT}")
        sys.exit(1)

    try:
        subprocess.run(
            [sys.executable, str(ETL_SCRIPT)],
            cwd=PROJECT_ROOT,
            check=True
        )
    except subprocess.CalledProcessError as error:
        print(f"ERROR: ETL pipeline failed with exit code {error.returncode}.")
        sys.exit(error.returncode)


if __name__ == "__main__":
    main()