import pandas as pd
import os
import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

base = r"C:\amazon dataset\student_resource\dataset"

# Country distribution for S2 and S3 (sampled for speed)
for src in ['source2', 'source3']:
    df = pd.read_csv(os.path.join(base, 'train', 'train_%s.tsv' % src), sep='\t', usecols=['country'])
    print('=== COUNTRY (%s) ===' % src)
    print(df['country'].value_counts())
    print()

# Test set country distribution
for src in ['source1', 'source2', 'source3']:
    df = pd.read_csv(os.path.join(base, 'test', 'test_%s.tsv' % src), sep='\t', usecols=['country'])
    print('=== TEST COUNTRY (%s) ===' % src)
    print(df['country'].value_counts())
    print()