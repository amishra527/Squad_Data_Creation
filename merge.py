import json
import os

def merge_json_files(start_dir, output_file):
    merged_data= {}
    for dirpath,dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                with open(os.path.join(dirpath, filename)) as f:
                    print(dirpath)
                    print(dirnames)
                    print(filename)
                    data = json.load(f)
                merged_data.update(data)

    with open(output_file, 'a') as f:
        json.dump(merged_data, f)

merge_json_files("C:/Users/NIC/Desktop/hackthon" , "merge.json")




# {'id': '57340bdf4776f419006617a4', 'title': 'Montana', 'context': "However, at the state level, the pattern of split ticket voting and divided government holds. Democrats currently hold one of the state's U.S. Senate seats, as well as four of the five statewide offices (Governor, Superintendent of Public Instruction, Secretary of State and State Auditor). The lone congressional district has been Republican since 1996 and in 2014 Steve Daines won one of the state's Senate seats for the GOP. The Legislative branch had split party control between the house and senate most years between 2004 and 2010, when the mid-term elections returned both branches to Republican control. The state Senate is, as of 2015, controlled by the Republicans 29 to 21, and the State House of Representatives at 59 to 41.", 'question': 'How long has the single congressional district been Republican?', 'answers': {'text': ['1996'], 'answer_start': [349]}}

