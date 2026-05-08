from langchain_community.vectorstores import FAISS
from app.utils.logger import logger

def create_vectorstore(documents, embeddings):
    logger.info('Creating vectorstore...')
    vectorstore=FAISS.from_documents(documents, embeddings)
    logger.info('Vectorstore created successfully.')
    return vectorstore
