from llama_index import  GPTSimpleVectorIndex, ServiceContext


def load_index(index_path:str):
    index = GPTSimpleVectorIndex.load_from_disk(index_path)
    return index

def qurey(txt:str,index):
    '''end indexed data to larg language model to answer questions'''
    res=index.query(query_str=txt,)
    
    
    return res
