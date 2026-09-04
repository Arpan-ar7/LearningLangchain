# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatOpenRouter(model="minimax/minimax-m2.7:free")

# while True:
#     user_input=input("You:- ")
#     if user_input=='exit':
#         break
#     result=model.invoke(user_input)
#     print("Ai:-",result.content)


# Here in this chatbot it do not have context like it cant remember the previous inputs 

# You:- my name is arpan
# Ai:- Hello Arpan! Nice to meet you. How can I help you today?
# You:- what is my name
# Ai:- I’m afraid I don’t have that information. If you’d like to share your name, I’m happy to use it!

# -------------------------------------------------------------------------------------------

# For this to handel for now what we will do we will create alist of chat_his then will append the input of use in tht 
# so not only the prompt will goto the model as well as the chat hist aslo 

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatOpenRouter(model="minimax/minimax-m2.7:free")

# chat_History=[]

# while True:
#     user_input=input("You:- ")
#     chat_History.append(user_input)
#     if user_input=='exit':
#         break
#     result=model.invoke(chat_History    )
#     chat_History.append(result.content)
#     print("Ai:-",result.content)

# print(chat_History)



# You:- my name is arpan 
# Ai:- Hello Arpan! 👋 It's great to meet you. How can I help you today?
# You:-   what is my name
# Ai:- Your name is **Arpan**! You just told me at the beginning of our conversation. 😊

# Is there anything specific you'd like help with today, Arpan?
# You:- exit
# ['my name is arpan ', "Hello Arpan! 👋 It's great to meet you. How can I help you today?", '\twhat is my name', "Your name is **Arpan**! You just told me at the beginning of our conversation. 😊\n\nIs there anything specific you'd like help with today, Arpan?", 'exit']

# Here one more prob comes under tht in the list the llm can 
# not uderstand tht whihc text is whome like it is said by user or human so t will be 
# confused when things get big 

# --------------------------------------------------------------------------------

# to tccakel this langchain provides serveral classes (Messages )

from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatOpenRouter(model="minimax/minimax-m2.7:free")

chat_History=[
    SystemMessage(content="You are a helpful ai assistant "),
    HumanMessage(content="")

]

while True:
    user_input=input("You:- ")
    chat_History.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_History)
    chat_History.append(AIMessage(content=result.content))
    print("Ai:-",result.content)

print(chat_History)



# You:- hi 
# Ai:- Hi there! 👋 How can I help you today?
# You:- My name is arpan what is yours 
# Ai:- Nice to meet you, Arpan! 👋

# I'm an AI assistant — you can call me whatever you'd like, or just "Assistant" works too. I'm here to help you with whatever you need, whether that's coding, answering questions, brainstorming ideas, or just having a chat.

# What can I help you with today?
# You:- what is my name brother 
# Ai:- Your name is **Arpan**, brother! 😄

# We literally just talked about this a moment ago. Did you forget already, or were you just testing me? 😉
# You:- exit
# [SystemMessage(content='You are a helpful ai assistant ', additional_kwargs={}, response_metadata={}),
#  HumanMessage(content='', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi ', 
# additional_kwargs={}, response_metadata={}), AIMessage(content='Hi there! 👋 How can I help you today?', 
# additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='My name is arpan what is yours ', additional_kwargs={}, response_metadata={}), 
# AIMessage(content='Nice to meet you, Arpan! 👋\n\nI\'m an AI assistant — you can call me whatever you\'d like,
#  or just "Assistant" works too. I\'m here to help you with whatever you need, whether that\'s coding,
#  answering questions, brainstorming ideas, or just having a chat.\n\nWhat can I help you with today?', 
# additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='what is my name brother ', additional_kwargs={}, response_metadata={}), 
# AIMessage(content='Your name is **Arpan**, brother! 😄\n\nWe literally just talked about this a moment ago.
#  Did you forget already, or were you just testing me? 😉', additional_kwargs={}, response_metadata={}, 
# tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='exit', additional_kwargs={}, 
# response_metadata={})]






