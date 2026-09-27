import pandas as pd
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

base = r"C:\amazon dataset\student_resource\dataset"

# Ground truth analysis (smaller, faster)
gt = pd.read_csv(os.path.join(base, 'train', 'train_ground_truth.tsv'), sep='\t')
print('=== GROUND TRUTH ANALYSIS ===')
print('total S1 entities:', len(gt))
print('null matched_entity_ids (singletons):', gt['matched_entity_ids'].isnull().sum())
print('singleton fraction: %.4f' % (gt['matched_entity_ids'].isnull().mean()))

gt['n_matches'] = gt['matched_entity_ids'].apply(lambda s: 0 if pd.isnull(s) or s=='' else len(s.split(',')))
print('\nmatch count distribution:')
print(gt['n_matches'].value_counts().sort_index().head(20))

gt['has_s2'] = gt['matched_entity_ids'].apply(lambda s: any(x.startswith('S2-') for x in (s.split(',') if not pd.isnull(s) and s else [])))
gt['has_s3'] = gt['matched_entity_ids'].apply(lambda s: any(x.startswith('S3-') for x in (s.split(',') if not pd.isnull(s) and s else [])))
print('\nhas S2 match:', gt['has_s2'].sum())
print('has S3 match:', gt['has_s3'].sum())
print('both:', ((gt['has_s2']) & (gt['has_s3'])).sum())

# Country distribution (sample to be fast)
s1 = pd.read_csv(os.path.join(base, 'train', 'train_source1.tsv'), sep='\t', usecols=['country'])
print('\n=== COUNTRY DISTRIBUTION (S1) ===')
print(s1['country'].value_counts())