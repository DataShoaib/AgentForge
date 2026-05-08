from app.utils.logger import logger

def create_retriever(vectorstore,k=3):
    logger.info('Creating retriever...')
    retriever=vectorstore.as_retriever(search_kwargs={'k':k})
    logger.info('Retriever created successfully.')
    return retriever