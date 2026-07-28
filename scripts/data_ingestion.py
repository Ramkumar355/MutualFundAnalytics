import pandas as pd
import os
folder_path = "data/raw"
files = os.listdir(folder_path)
for file in files:
    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("=" * 50)
    print("File:", file)
    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())