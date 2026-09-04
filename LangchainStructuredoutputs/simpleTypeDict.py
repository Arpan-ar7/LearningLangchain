# from typing import TypedDict

# class person(TypedDict):

#     name:str
#     age:int

# new_person: person={'name':"sfsf",'age':45}

# print(new_person)
# --------------------------------------------------------------------------------

from typing import TypedDict
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model="inclusionai/ling-3.0-flash-fin:free"
)

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

review = """
I recently purchased these wireless headphones and I am very impressed
with the sound quality. The battery lasts for a long time and they are
comfortable to wear. However, the microphone quality could be better.
Overall, I am happy with my purchase and would recommend them.
"""

result = structured_model.invoke(review)

print(result)