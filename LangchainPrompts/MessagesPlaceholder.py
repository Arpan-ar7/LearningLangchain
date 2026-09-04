from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# Chat Template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Chat history
chat_history = []

# Load chat history
with open("chat_history.txt") as f:
    chat_history.append(f.readline())

print(chat_history)

# Create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my food?"
})

print(prompt)