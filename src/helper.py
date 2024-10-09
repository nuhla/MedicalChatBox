"""" ---------------------------------------------------------
-------------- Import Necessary Libraries --------------------
--------------------------------------------------------------
"""
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone as PineconeStor
#import pinecone
from langchain.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter




"""" ------------------------------------------------------------
-----------------------------------------------------------------
- function name : load_pdf
- function description :Load PDF files 
- arguments data:  is the directory where we saved the pfd files 
- returned value : all documents in this folder  
----------------------------------------------------------------
----------------------------------------------------------------
"""
def load_pdf(data):
    loader=DirectoryLoader(data, 
                    glob="*.pdf",
                    loader_cls=PyMuPDFLoader)
    documents= loader.load()

    return documents


"""" ------------------------------------------------------------
-----------------------------------------------------------------
- function name : text_splinting
- function description :splits text iin the document wee got into 
  chunks so we can vectorized it to dataset 
- arguments data:  documents we loaded from folder 
- returned value : chunks of text 
----------------------------------------------------------------
----------------------------------------------------------------
"""
def text_splinting(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks 


"""" ------------------------------------------------------------
-----------------------------------------------------------------
- function name : download_hugging_face_embeddings
- function description :download embedding Model we uses to 
  vectoring our data
- arguments data:  The Model name from HuggingFace - ini value 
  will be {sentence-transformers/all-MiniLM-L6-v2}
- returned value : embeddings Model
----------------------------------------------------------------
----------------------------------------------------------------
"""
def download_hugging_face_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings=HuggingFaceEmbeddings(model_name=model_name)
    return embeddings