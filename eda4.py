import pandas as pd
import os
import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

base = r"C:\amazon dataset\student_resource\dataset"

# Sample matching pairs from ground truth to understand noise patterns
gt = pd.read_csv(os.path.join(base, 'train', 'train_ground_truth.tsv'), sep='\t')
s1 = pd.read_csv(os.path.join(base, 'train', 'train_source1.tsv'), sep='\t')
s2 = pd.read_csv(os.path.join(base, 'train', 'train_source2.tsv'), sep='\t')
s3 = pd.read_csv(os.path.join(base, 'train', 'train_source3.tsv'), sep='\t')

s1_map = s1.set_index('entity_id')
s2_map = s2.set_index('entity_id')
s3_map = s3.set_index('entity_id')

# Sample 30 matched entities with their matches
sample = gt[gt['matched_entity_ids'].notna()].sample(30, random_state=42)
print('=== SAMPLE MATCHES (name/address noise) ===')
for _, row in sample.iterrows():
    s1_id = row['source1_entity_id']
    matches = row['matched_entity_ids'].split(',')
    s1_row = s1_map.loc[s1_id]
    print('\nS1:', s1_id)
    print('  name:', repr(s1_row['business_name']))
    print('  addr:', repr(s1_row['business_address']))
    print('  country:', s1_row['country'])
    for m in matches[:4]:
        if m.startswith('S2-'):
            m_row = s2_map.loc[m]
        else:
            m_row = s3_map.loc[m]
        print('  ->', m, '|', repr(m_row['business_name']), '|', repr(m_row['business_address']), '|', m_row['country'])

# Also look at singletons
print('\n\n=== SAMPLE SINGLETONS ===')
singles = gt[gt['matched_entity_ids'].isna()].sample(15, random_state=42)
for _, row in singles.iterrows():
    s1_id = row['source1_entity_id']
    s1_row = s1_map.loc[s1_id]
    print('\nS1:', s1_id)
    print('  name:', repr(s1_row['business_name']))
    print('  addr:', repr(s1_row['business_address']))
    print('  country:', s1_row['country'])