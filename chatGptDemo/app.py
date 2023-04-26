import os
import openai

import yaml
from chat_completion import chat_completion

from completion import get_model_reply


if __name__=="__main__":
    with open('../cred.yaml') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        
    openai.api_key  = data["OPENAI_API_KEY"]
    #query = 'Which is the largest country by area in the world?'
    query = 'I want to ask you'
    responses, context = get_model_reply(query, context=[])

    print('<USER> ' + responses[-1][0])
    print('<BOT> ' + responses[-1][1])