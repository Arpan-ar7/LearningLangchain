# ============================================================
# CHROMADB + OPENROUTER EMBEDDINGS
# ============================================================
#
# Flow:
#
# Documents
#     ↓
# OpenRouter Embedding Model
#     ↓
# Vectors
#     ↓
# ChromaDB
#
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTS
# ------------------------------------------------------------

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
import os


# ------------------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------------
#
# Your .env file should contain:
#
# OPENROUTER_API_KEY=your_api_key
#
# ------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------
# 3. CREATE OPENROUTER EMBEDDING MODEL
# ------------------------------------------------------------
#
# OpenRouter provides an OpenAI-compatible API.
#
# We use OpenAIEmbeddings as the LangChain interface,
# but the actual model is running through OpenRouter.
#
# ------------------------------------------------------------

embeddings = OpenAIEmbeddings(
    model="liquid/lfm-2.5-embedding-350m:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# ------------------------------------------------------------
# 4. CREATE DOCUMENTS
# ------------------------------------------------------------

doc1 = Document(
    page_content=(
        "Virat Kohli is one of the most successful and consistent "
        "batsmen in IPL history. Known for his aggressive batting "
        "style and fitness, he has led the Royal Challengers Bangalore "
        "in multiple seasons."
    ),
    metadata={
        "team": "Royal Challengers Bangalore",
        "role": "Batsman"
    }
)

doc2 = Document(
    page_content=(
        "Rohit Sharma is the most successful captain in IPL history, "
        "leading Mumbai Indians to five titles. He's known for his "
        "calm demeanor and ability to play big innings under pressure."
    ),
    metadata={
        "team": "Mumbai Indians",
        "role": "Batsman"
    }
)

doc3 = Document(
    page_content=(
        "MS Dhoni, famously known as Captain Cool, has led Chennai "
        "Super Kings to multiple IPL titles. His finishing skills, "
        "wicketkeeping, and leadership are legendary."
    ),
    metadata={
        "team": "Chennai Super Kings",
        "role": "Wicketkeeper"
    }
)

doc4 = Document(
    page_content=(
        "Jasprit Bumrah is considered one of the best fast bowlers "
        "in T20 cricket. Playing for Mumbai Indians, he is known for "
        "his yorkers and death-over expertise."
    ),
    metadata={
        "team": "Mumbai Indians",
        "role": "Bowler"
    }
)

doc5 = Document(
    page_content=(
        "Ravindra Jadeja is a dynamic all-rounder who contributes "
        "with both bat and ball. Representing Chennai Super Kings, "
        "his quick fielding and match-winning performances make him "
        "a key player."
    ),
    metadata={
        "team": "Chennai Super Kings",
        "role": "All-rounder"
    }
)


docs = [doc1, doc2, doc3, doc4, doc5]


# ------------------------------------------------------------
# 5. CREATE / CONNECT TO CHROMADB
# ------------------------------------------------------------
#
# persist_directory:
#     This is where ChromaDB stores the database on your disk.
#
# collection_name:
#     Think of this like a table/group containing your documents.
#
# embedding_function:
#     The embedding model used to convert text → vectors.
#
# ------------------------------------------------------------

vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="my_chroma_db"
)


# ============================================================
# 6. ADD DOCUMENTS
# ============================================================
#
# add_documents() converts each document into embeddings
# and stores them inside ChromaDB.
#
# ------------------------------------------------------------

vector_store.add_documents(docs)

print("Documents added successfully!")


# ============================================================
# 7. ADD DOCUMENTS WITH YOUR OWN IDs
# ============================================================
#
# IDs are useful when you later want to update or delete
# specific documents.
#
# ------------------------------------------------------------

new_docs = [
    Document(
        page_content="Hardik Pandya is an explosive all-rounder.",
        metadata={"team": "Mumbai Indians", "role": "All-rounder"}
    ),
    Document(
        page_content="Ruturaj Gaikwad is a talented opening batsman.",
        metadata={"team": "Chennai Super Kings", "role": "Batsman"}
    )
]

ids = [
    "player_hardik",
    "player_ruturaj"
]

vector_store.add_documents(
    documents=new_docs,
    ids=ids
)

print("Documents with IDs added!")


# ============================================================
# 8. SIMILARITY SEARCH
# ============================================================
#
# This is one of the MOST IMPORTANT operations in RAG.
#
# We give Chroma a question.
#
# Question → embedding → compare with stored vectors
#          → return most similar documents
#
# ------------------------------------------------------------

query = "Who is a famous fast bowler?"

results = vector_store.similarity_search(
    query,
    k=2
)

print("\nSimilarity Search Results:")

for doc in results:
    print("--------------------")
    print(doc.page_content)
    print(doc.metadata)


# ============================================================
# 9. SIMILARITY SEARCH WITH SCORES
# ============================================================
#
# This gives us:
#
#     (Document, similarity/distance score)
#
# ------------------------------------------------------------

results_with_scores = vector_store.similarity_search_with_score(
    "Who is a good batsman?",
    k=3
)

print("\nResults With Scores:")

for doc, score in results_with_scores:
    print("--------------------")
    print("Score:", score)
    print("Document:", doc.page_content)
    print("Metadata:", doc.metadata)


# ============================================================
# 10. SEARCH USING METADATA FILTER
# ============================================================
#
# We can restrict the search to documents belonging
# to a particular team.
#
# ------------------------------------------------------------

results = vector_store.similarity_search(
    "Who is a good player?",
    k=3,
    filter={"team": "Mumbai Indians"}
)

print("\nMumbai Indians Players:")

for doc in results:
    print("--------------------")
    print(doc.page_content)
    print(doc.metadata)


# ============================================================
# 11. SEARCH USING ROLE
# ============================================================

results = vector_store.similarity_search(
    "Who is a batsman?",
    k=3,
    filter={"role": "Batsman"}
)

print("\nBatsmen:")

for doc in results:
    print("--------------------")
    print(doc.page_content)
    print(doc.metadata)


# ============================================================
# 12. RETRIEVER
# ============================================================
#
# Instead of directly calling similarity_search(),
# we can turn Chroma into a Retriever.
#
# Retriever is very important for RAG.
#
# ------------------------------------------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

results = retriever.invoke(
    "Tell me about Chennai Super Kings players"
)

print("\nRetriever Results:")

for doc in results:
    print("--------------------")
    print(doc.page_content)


# ============================================================
# 13. GET DOCUMENTS
# ============================================================
#
# If you supplied IDs, you can retrieve them directly.
#
# ------------------------------------------------------------

data = vector_store.get(
    ids=["player_hardik"]
)

print("\nGet Document:")

print(data)


# ============================================================
# 14. GET ALL DOCUMENTS
# ============================================================
#
# Be careful with this for a large database.
#
# ------------------------------------------------------------

data = vector_store.get()

print("\nAll Stored Data:")

print(data)


# ============================================================
# 15. UPDATE A DOCUMENT
# ============================================================
#
# update_documents() replaces the document associated
# with an existing ID.
#
# ------------------------------------------------------------

updated_doc = Document(
    page_content=(
        "Hardik Pandya is an explosive Indian all-rounder "
        "known for his batting, bowling and leadership."
    ),
    metadata={
        "team": "Mumbai Indians",
        "role": "All-rounder"
    }
)

vector_store.update_documents(
    ids=["player_hardik"],
    documents=[updated_doc]
)

print("\nDocument updated!")


# ============================================================
# 16. DELETE A DOCUMENT
# ============================================================
#
# Delete using its ID.
#
# ------------------------------------------------------------

vector_store.delete(
    ids=["player_ruturaj"]
)

print("\nRuturaj document deleted!")


# ============================================================
# 17. CHECK WHETHER DOCUMENT EXISTS
# ============================================================
#
# get() can be used to check a specific ID.
#
# ------------------------------------------------------------

data = vector_store.get(
    ids=["player_hardik"]
)

print("\nChecking Hardik document:")

print(data)


# ============================================================
# 18. DATABASE PERSISTENCE
# ============================================================
#
# Because we specified:
#
#     persist_directory="my_chroma_db"
#
# Chroma stores the database on your disk.
#
# Therefore, when your Python program stops, the data
# remains inside:
#
#     my_chroma_db/
#
# You can later create another Chroma object pointing
# to the same directory and collection.
#
# ------------------------------------------------------------

vector_store_2 = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="my_chroma_db"
)

print("\nConnected to existing ChromaDB!")


# ============================================================
# 19. SEARCH THE RELOADED DATABASE
# ============================================================

results = vector_store_2.similarity_search(
    "Who is Captain Cool?",
    k=2
)

print("\nSearch after reloading database:")

for doc in results:
    print("--------------------")
    print(doc.page_content)
    print(doc.metadata)


# ============================================================
# 20. DELETE THE ENTIRE COLLECTION
# ============================================================
#
# WARNING:
# This removes the collection and its documents.
#
# Don't run this unless you actually want to delete
# your Chroma collection.
#
# ------------------------------------------------------------

# vector_store.delete_collection()