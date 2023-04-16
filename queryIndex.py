from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex,LLMPredictor,PromptHelper,QueryMode

def load_index():
    index = GPTSimpleVectorIndex.load_from_disk('indexData/index.json')
    return index

def qurey(txt:str,index):
    '''end indexed data to larg language model to answer questions'''
    res=index.query(query_str=txt,)
    return res
