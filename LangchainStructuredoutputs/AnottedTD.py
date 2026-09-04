from typing import TypedDict,Annotated,Optional
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model="inclusionai/ling-3.0-flash-fin:free"
)

class Review(TypedDict):
    key_themes:Annotated[str,"Writedown ll the key themes discussed in the review "]
    summary: Annotated[str,"Brief summary of the review"]
    sentiment:Annotated[str,"Return sentiment of the review either negative positive or neutral "]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list "]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list "]

structured_model = model.with_structured_output(Review)

review = """
I recently purchased these wireless headphones and I am very impressed
with the sound quality. The battery lasts for a long time and they are
comfortable to wear. However, the microphone quality could be better.

The headphones have excellent sound quality, great battery life, and are
very comfortable. The microphone is not very good.

Overall, I am happy with my purchase and would recommend them.
"""

result = structured_model.invoke(review)

print(result)

# There is a prob tht we can not do data validatation as here str is mention but we can still pass number in some cases it wil generate error
#  so for tht we will use pydantic data validatatation