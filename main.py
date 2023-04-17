import os

import yaml
from finetune import configureLongChain, save_index
from queryIndex import load_index, qurey
if __name__ == '__main__':
    with open('cred.yaml') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        
    os.environ["OPENAI_API_KEY"] = data["OPENAI_API_KEY"]
    #save_index()
    #configureLongChain()
    
    index=load_index()
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    response=prompt
    
    while prompt!="exit":
        prompt=input("prompt >> ")
        txt=response+"\nHuman: "+prompt
        #print(txt)
        res=qurey(txt=txt,index=index)
        if res.response!="Empty Response":
            response=txt+"\n"+res.response

        #print(f'history: {response}')
        print(f'{res.response}')
    