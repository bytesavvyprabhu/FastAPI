from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    password : str
    email : str
    
    
    
class Result(BaseModel):
    result : str
    coding_lang : str
    grammer : str
    filler_words : str