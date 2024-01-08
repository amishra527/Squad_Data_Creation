import json
import os

def merge_json(directory, json_name):
    merge_data = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, encoding='utf-8', errors='ignore') as f:
                    try:
                        data = json.load(f)
                        merge_data.update(data)
                    except ValueError:
                        print(f'Error reading file {file_path}')
    with open('merge.json', 'w', encoding='utf-8') as f:
        json.dump(merge_data, f, ensure_ascii=False, indent=4)


merge_json("C:/Users/NIC/Desktop/hackthon" , "merge.json")