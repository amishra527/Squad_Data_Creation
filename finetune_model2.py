from transformers import pipeline,AutoModelForQuestionAnswering as amfq, AutoTokenizer
print("hi iam here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad",force_download=True)
print
model = amfq.from_pretrained("distilbert-base-uncased-distilled-squad",force_download=True)
#print(tokenizer)
#print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
#exit()
#pipe = pipeline("text-classification")
#print(pipe("This restaurant is awesome"))
# tokenizer = AutoTokenizer.from_pretrained("./tokenizer")
# model = amfq.from_pretrained("model")




from datasets import load_dataset, Dataset
import json, csv, ast
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# df = pd.read_csv('output21.csv')
# df['answers'] = df['answers'].apply(ast.literal_eval)
# df['answers'] = df['answers'].apply(lambda x: eval(x))
# squad = Dataset.from_pandas(df, split="train[:5012]")
df = pd.read_json('C:/Users/NIC/Desktop/hackthon/dataframe.json', orient='records')
df['answers'] = df['answers'].astype(str)
squad = Dataset.from_pandas(df, split="train[:80]")

# squad = load_dataset("parquet", data_files={'train': 'noblank.parquet'}, split="train[:5000]")
# squad = load_dataset('json', data_files='nodubs_t_q_a_4.json', split="train[:5000]")
# squad = load_dataset('csv', data_files='file.csv', delimiter=",", split="train[:5000]")
# squad = load_dataset('json', data_files='nodubs_t_q_a_7.json', field='data', split="train[:5000]")
# squad = load_dataset("squad", split="train[:5000]")
# squad = load_dataset('json', data_files='nodubs_t_q_a_5.json', field='data', split="train[:5000]")
print(squad)
# exit()

squad = squad.train_test_split(test_size=0.2)
#print(squad)
print(squad["train"][0])
# print(squad["train"][0:10])
# exit()
def preprocess_function(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = tokenizer(
        questions,
        examples["context"],
        max_length=384,
        truncation="only_second",
        return_offsets_mapping=True,
        padding="max_length",
    )

    offset_mapping = inputs.pop("offset_mapping")
    answers = examples["answers"]
    start_positions = []
    end_positions = []

    for i, offset in enumerate(offset_mapping):
        answer = answers[i]
        print(answer,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") # print is here >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        start_char = answer["answer_start"][0]
        print(start_char,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        end_char = answer["answer_start"][0] + len(answer["text"][0])
        print(end_char,"#########################################")
        sequence_ids = inputs.sequence_ids(i)

        # Find the start and end of the context
        idx = 0
        while sequence_ids[idx] != 1:
            idx += 1
        context_start = idx
        while sequence_ids[idx] == 1:
            idx += 1
        context_end = idx - 1

        # If the answer is not fully inside the context, label it (0, 0)
        if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
            start_positions.append(0)
            end_positions.append(0)
        else:
            # Otherwise it's the start and end token positions
            idx = context_start
            while idx <= context_end and offset[idx][0] <= start_char:
                idx += 1
            start_positions.append(idx - 1)

            idx = context_end
            while idx >= context_start and offset[idx][1] >= end_char:
                idx -= 1
            end_positions.append(idx + 1)

    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    return inputs

print(squad["train"].column_names)
tokenized_squad = squad.map(preprocess_function, batched=True, remove_columns=squad["train"].column_names)
print(tokenized_squad["train"])
exit()
from transformers import DefaultDataCollator

data_collator = DefaultDataCollator()


from transformers import AutoModelForQuestionAnswering, TrainingArguments, Trainer





training_args = TrainingArguments(
    output_dir="my_awesome_qa_model",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=5,
    weight_decay=0.01,
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_squad["train"],
    eval_dataset=tokenized_squad["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

