from langchain_community.document_loaders import TextLoader
from app.utils.logger import logger


def load_documents(file_path='D:\\projects shoaib\\Ai-agent\\data.txt'):
    logger.info(f'Loading documents from {file_path}...')
    loader=TextLoader(file_path)
    logger.info('Documents loaded successfully.')
    return loader.load()
