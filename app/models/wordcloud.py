from pydantic import BaseModel

class WordCloudRequest(BaseModel):
    content: str

class WordCloudResponse(BaseModel):
    word: str
    frequency: int
