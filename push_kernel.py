
import json, requests
from pathlib import Path

kaggle_json = Path(r'C:\Users\dasha\.kaggle\kaggle.json')
creds = json.loads(kaggle_json.read_text())
username = creds['username']
key = creds['key']

source_path = Path(r'C:\Users\dasha\Projects\COMMENCINGTHESCOURGE\products\kaggle-audit-node24-ci-guard\audit.ipynb')
payload = {
    'title': 'Audit: node24-ci-guard',
    'language': 'python',
    'kernelType': 'notebook',
    'isPrivate': False,
    'enableGpu': False,
    'enableInternet': False,
    'datasetDataSources': [],
    'kernelDataSources': [],
    'competitionDataSources': [],
    'modelDataSources': [],
    'categoryIds': [],
    'text': source_path.read_text(encoding='utf-8'),
}
r = requests.post('https://www.kaggle.com/api/v1/kernels/push', auth=(username, key), json=payload, timeout=120)
print('status', r.status_code)
print(r.text[:4000])
