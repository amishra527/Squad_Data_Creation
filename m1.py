import os
import json
def search_folder_for_json(folder_path):
    new_json = []
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        # print(data) # print out the data from the JSON file
                        if 'id' in data and 'title' in data and 'context' in data and 'question' in data and 'answers' in data:
                            if 'text' in data['answers'] and 'answer_start' in data['answers']:
                                new_data = {'id': data['id'], 'title': data['title'], 'context': data['context'], 'question': data['question'], 'answers': data['answers']}
                                new_json.append(new_data)
                except UnicodeDecodeError:
                    print(f"Unicode error in file: {file_path}")
    with open('new_json.json', 'w') as f:
        json.dump(new_json, f)
folder_path = 'C:/Users/NIC/Desktop/hackthon'
search_folder_for_json(folder_path)







# import os
# import json
# import shutil
# def search_folder_for_json(folder_path):
#     new_json = []
#     for subdir, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.json'):
#                 file_path = os.path.join(subdir, file)
#                 try:
#                     with open(file_path, 'r') as f:
#                         data = json.load(f)
#                         if 'id' in data and 'title' in data and 'context' in data and 'question' in data and 'answers' in data:
#                             if 'text' in data['answers'] and 'answer_start' in data['answers']:
#                                 new_data = {'id': data['id'], 'title': data['title'], 'context': data['context'], 'question': data['question'], 'answers': data['answers']}
#                                 new_json.append(new_data)
#                 except UnicodeDecodeError:
#                     print(f"Unicode error in file: {file_path}")
#     with open('new_json.json', 'w') as f:
#         json.dump(new_json, f)
# folder_path = 'C:/Users/NIC/Desktop/hackthon'
# search_folder_for_json(folder_path)

# import os
# import json
# import shutil
# def search_folder_for_json(folder_path):
#     new_json = []
#     for subdir, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.json'):
#                 file_path = os.path.join(subdir, file)
#                 with open(file_path, 'r') as f:
#                     data = json.load(f)
#                     if 'id' in data and 'title' in data and 'context' in data and 'question' in data and 'answers' in data:
#                         if 'text' in data['answers'] and 'answer_start' in data['answers']:
#                             new_data = {'id': data['id'], 'title': data['title'], 'context': data['context'], 'question': data['question'], 'answers': data['answers']}
#                             new_json.append(new_data)
#     with open('new_json.json', 'w') as f:
#         json.dump(new_json, f)
# folder_path = 'C:/Users/NIC/Desktop/hackthon'
# search_folder_for_json(folder_path)

# import os
# import json
# import shutil
# def search_folder_for_json(folder_path):
#     new_json = []
#     for subdir, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.json'):
#                 file_path = os.path.join(subdir, file)
#                 with open(file_path, 'r') as f:
#                     data = json.load(f)
#                     if 'id' in data and 'title' in data and 'context' in data and 'question' in data and 'answers' in data:
#                         if 'text' in data['answers'] and 'answer_start' in data['answers']:
#                             new_json.append(data)
#     with open('new_json.json', 'w') as f:
#         json.dump(new_json, f)
# folder_path = 'C:/Users/NIC/Desktop/hackthon'
# search_folder_for_json(folder_path)