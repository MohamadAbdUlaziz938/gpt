import os

import yaml
from finetune import save_index
from queryIndex import load_index, qurey
if __name__ == '__main__':
    with open('cred.yaml') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        
    os.environ["OPENAI_API_KEY"] = data["OPENAI_API_KEY"]
    #save_index()
    index=load_index()
    prompt="I'm  machine learning developer"
    while prompt!="exit":
        prompt=input("prompt >> ")
        response=qurey(txt=prompt,index=index)
        print(response)
    