import pandas as pd
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

base = r"C:\amazon dataset\student_resource\dataset"

for name in ['train_source1','train_source2','train_source3','train_ground_truth']:
    path = os.path.join(base, 'train', name + '.tsv')
    df = pd.read_csv(path, sep='\t')
    print('===', name, df.shape)
    print(df.head(3).to_string())
    print(df.dtypes)
    print('nulls:', df.isnull().sum().to_dict())
    print()