from src.helper import load_pdf, text_splinting , download_hugging_face_embeddings
import os 
from  dotenv import load_dotenv
from langchain_pinecone import Pinecone as PineconeStor
import pinecone

docs =load_pdf('data')

chunks =text_splinting(docs)

embedding = download_hugging_face_embeddings()



#---------------------------------------------------------#
#---------- Load the environment variable ----------------#
#---------------------------------------------------------#
load_dotenv()
key = os.getenv("PINION_KEY")
environment = os.getenv("PINECONE_ENVIRONMENT")
os.environ['PINECONE_API_KEY'] = key
os.environ['PINECONE_API_ENV'] = environment


#---------------------------------------------------------#
#---------- Initializing Pinecone dataset ----------------#
#---------------------------------------------------------#
pc=pinecone.Pinecone(api_key =key, environment=environment)
index_name="medicalchatbot"


#---------------------------------------------------------#
#--------------- put data in dataset ---------------------#
#---------------------------------------------------------#
if index_name in pc.list_indexes().names():
    docserach = PineconeStor.from_texts([t.page_content for t in chunks], embedding, index_name=index_name)
else :
    print("not in ")
    



