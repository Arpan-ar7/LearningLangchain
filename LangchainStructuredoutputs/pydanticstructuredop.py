from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = "Ronaldo"  #Defaukt value
    age: int = 34 
    email:EmailStr
    # cgpa:Field(gt=0,lt=10,default=5,description="Adecimal value represetnitng college marks ")

new_student = {
    "name": "Arpan"
}

student = Student(**new_student)

print(student)

# With_structured_output