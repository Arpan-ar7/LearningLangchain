from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-VL-Embedding-2B"
)

docs = [
    "Cristiano Ronaldo is the GOAT",
    "I do not like fanbase of Messi",
    "Cristiano Ronaldo is from Portugal",
    "Ferran Torres is from Spain. He also plays football",
    "My friend is a fan of Harry Potter",
    "I do not like Harry Potter"
]

query = "Who is from Portugal?"

doc_embeddings = embeddings.embed_documents(docs)

query_embedding = embeddings.embed_query(query)

similarity = cosine_similarity(
    [query_embedding],
    doc_embeddings
)

print(similarity)