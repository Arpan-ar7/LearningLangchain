# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id="openai-community/gpt2",
#     task="text-generation",
#     pipeline_kwargs={
#         "temperature": 0.5,
#         "max_new_tokens": 100
#     }
# )

# model = ChatHuggingFace(
#     llm=llm
# )

# result = model.invoke("Who is Cristiano Ronaldo?")

# print(result.content)

# I am commenting all the code bcs i do not want to downld the model 
# ------------------------------------------------------------------------

# For change the path to downldes 
# import os

# os.environ["HF_HOME"] = "D:/huggingface_cache"

# ------------------------------------------------------------------------
# import os

# os.environ["HF_HOME"] = "D:/huggingface_cache"

# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id="openai-community/gpt2",
#     task="text-generation",
#     pipeline_kwargs={
#         "temperature": 0.5,
#         "max_new_tokens": 100
#     }
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("Who is Cristiano Ronaldo?")

# print(result.content)