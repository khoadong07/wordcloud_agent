from pydantic import BaseModel
from typing import List, Optional

class AnalyzeItem(BaseModel):
    id: str
    title: Optional[str] = None
    description: Optional[str] = None
    content: str
    type: Optional[str] = None
    sentiment: Optional[str] = "neutral"
    topic: Optional[str] = None
    topic_id: Optional[str] = None
    site_name: Optional[str] = None
    site_id: Optional[str] = None
    category: Optional[str] = None
    spam: Optional[bool] = None
    lang: Optional[str] = None

class AnalyzeRequest(BaseModel):
    data: List[AnalyzeItem]

class WordCloudItem(BaseModel):
    word: str
    frequency: int

class AnalyzeResult(BaseModel):
    id: str
    word_cloud: List[WordCloudItem]

class AnalyzeResponse(BaseModel):
    results: List[AnalyzeResult]
