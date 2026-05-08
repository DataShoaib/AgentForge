from langchain_community.embeddings import HuggingFaceEmbeddings
from app.utils.logger import logger

def get_embedding(model_name:str="BAAI/bge-small-en-v1.5"):
    logger.info(f"Loading embedding model: {model_name}")
    embeddings=HuggingFaceEmbeddings(model_name=model_name,model_kwargs={"device":"cpu"},encode_kwargs={"normalize_embeddings":True})
    logger.info("Embedding model loaded successfully")
    return embeddings