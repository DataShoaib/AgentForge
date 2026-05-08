from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utils.logger import logger

def chunk_documents(documents,chunk_size=300,chunk_overlap=50):
    logger.info('Chunking Documents started...')
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    chunks=text_splitter.create_documents([doc.page_content for doc in documents])
    logger.info('Documents chunked successfully.')
    return chunks