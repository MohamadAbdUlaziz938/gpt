import os

import yaml
from finetune import  save_index
from queryIndex import load_index, qurey


def chat_Ai(index):
    prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    print(f'\n{prompt}\n')
    response = prompt

    while prompt != "exit":
        prompt = input("You >> ")
        txt = response+"\nHuman: "+prompt
        # print(txt)
        res = qurey(txt=txt, index=index)
        if res.response != "Empty Response":
            response = txt+"\n"+res.response

        # print(f'history: {response}')
        print(f'{res.response}\n')

def create_directory(name:str):
    try:
        os.makedirs(name=name)
    except FileExistsError:
        pass
   
def user_actions():
    try:
        while True:
            print("1- Indexing data (will read data from sourceData folder then save index.json in indexData folder).\n"
                "2- Chat with AI assistant.\n"
                "3- exit\n")
            action_number = input("Number of action: >> ")
            if action_number == "1":
                index = save_index()
            elif action_number == "2":
                index = load_index()
                chat_Ai(index=index)
            elif action_number == "3":

                exit(0)
            else:
                print("Please enter the correct action number (1,2,3).\n")
                action_number = input("Number of action: >> ")
    except Exception as e:
        print(e)
        print("\n\nSomething went wrong, please try againg.\n\n")
        user_actions()

if __name__ == '__main__':
    print('\nWelocme to AI assistant:\n')
    try:
        with open('cred.yaml') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    except Exception as e:
                print('\nPlease add cred.yaml file:\n')

    os.environ["OPENAI_API_KEY"] = data["OPENAI_API_KEY"]
    #os.environ["OPENAI_API_KEY"] = "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"
    create_directory(name="sourceData")
    create_directory(name="indexData")
    print('\nWelocme to AI assistant:\n')
    user_actions()
    
