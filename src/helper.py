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
- function description :Load PDF files 
- arguments data:  is the directory where we saved the pfd files 
- returned value : all documents in this folder  
----------------------------------------------------------------
----------------------------------------------------------------
"""