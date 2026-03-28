import pandas as pd
import sys
import os

file_path = sys.argv[1]

df = pd.read_csv(file_path)

df.to_csv("data_raw.csv", index=False)

os.system("python preprocess.py data_raw.csv")