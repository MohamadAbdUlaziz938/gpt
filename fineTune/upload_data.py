import json

import openai


def upload_data_set():
    with open("data.json", "r") as f:
        data = json.load(f)
        
    
    dataset = openai.File.create(
    file=open("data2_prepared.jsonl", "rb"),
    purpose="fine-tune"
    
    )
    return dataset