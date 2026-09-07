from langchain_community.tools import tool

# def multiply(a,b):
#     """""Multiply 2 numbers """
#     return a*b

# # STEP 2 ADD TYPE HINT 

# def multiply( a:int,b:int)->int:
#     """""Multiply 2 numbers """
#     return a*b

# # Add tool decorator 

def multiply( a:int,b:int)->int:
    """""Multiply 2 numbers """
    return a*b
