from flask import Flask , render_template ,jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import Pinecone as PineconeStor
import pinecone
# from langchain.vectorstores import Pinecone
from  langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os 


app=Flask(__name__)

#---------------------------------------------------------#
#---------- Load the environment variable ----------------#
#---------------------------------------------------------#
load_dotenv()
key = os.getenv("PINION_KEY")
environment = os.getenv("PINECONE_ENVIRONMENT")
print(key, environment)
#---------------------------------------------------------#
#---------------------------------------------------------#


os.environ['PINECONE_API_KEY'] = key
os.environ['PINECONE_API_ENV'] = environment

pc=pinecone.Pinecone(api_key =key, environment=environment)
index_name="medicalchatbot"
embedding = download_hugging_face_embeddings()


"""
--------------------- Retrive data from dataset -----------------
"""
docsearch = PineconeStor.from_existing_index(index_name, embedding)


"""
---------------------- Create My Prompt -------------------------
"""
PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}
    
llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)


@app.route("/")
def index():
    return render_template('chat.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)