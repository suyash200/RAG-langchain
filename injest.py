from langchain.document_loaders import PDFMinerLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings import SentenceTransformerEmbeddings 
from langchain.vectorstores import Chroma 
import os 
from constants import CHROMA_SETTINGS
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.document_loaders import UnstructuredMarkdownLoader

persist_directory = "db"

def main():

    for root, dirs, files in os.walk("docs"):
        for file in files:
            print(file)
            if file.endswith(".md"):
                            print(file)
                            loader = UnstructuredMarkdownLoader(os.path.join(root, file))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=500)
    texts = text_splitter.split_documents(loader)
    #create embeddings here
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    #create vector store here
    db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory, client_settings=CHROMA_SETTINGS)
    db.persist()
    db=None 

if __name__ == "__main__":
    main()