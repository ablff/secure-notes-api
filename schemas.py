from pydantic import BaseModel, Field, ConfigDict

class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=10000)

class NoteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)



    id: int
    title: str
    content: str
        
        