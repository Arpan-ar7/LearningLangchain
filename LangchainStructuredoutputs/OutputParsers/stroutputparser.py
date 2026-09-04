from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
template2=PromptTemplate(
    template='summarize in 5 words summary on the following text .\n {text}',
    input_variables=['text']
)
parser=StrOutputParser()

chain=template1 | model | parser | template2 |model | parser 

result=chain.invoke({'topic':'blackhole'})

print(result)