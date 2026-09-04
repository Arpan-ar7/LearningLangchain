from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template1=PromptTemplate(
    template='tell me the name of out planets in ur solar system aslon with their ' \
    'moon names mininum mooon nmaes should be 2  {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt=template1.format()

result=model.invoke(prompt)
print(result)