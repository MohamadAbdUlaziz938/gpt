from llama_index  import SimpleDirectoryReader, GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain.chat_models import ChatOpenAI
from langchain.chains  import ChatVectorDBChain
from langchain.llms import OpenAI

from queryIndex import load_index

def construct_index():
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))   
    
    return llm_predictor,prompt_helper

def save_index(source_data:str,save_index_to:str):
    loaded_content = SimpleDirectoryReader(source_data).load_data()
    
    '''fine tuning '''
    output_index = GPTSimpleVectorIndex.from_documents(documents=loaded_content,)
    
    output_index.save_to_disk(save_path=save_index_to,)
    return output_index
    

def configureLongChain():
    vectordb=load_index()
    romeoandjuliet_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0, model_name="gpt-3.5-turbo"), vectordb, return_source_documents=True)
    
    result = romeoandjuliet_qa({"question": "Hi", "chat_history": []})


