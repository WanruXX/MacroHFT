import gzip
import json
import csv

with gzip.open(R'C:\Users\wanru.xia\Downloads\ETH_USDT-202501.csv.gz', 'rt') as f:
    file_content = f.read()
    
# json_object = json.loads(file_content)

contents = file_content.split("\n")
print("done")