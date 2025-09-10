from fastapi import APIRouter
from app.models.wordcloud import WordCloudRequest, WordCloudResponse
from app.services.wordcloud_service import generate_word_cloud_cached

router = APIRouter()

@router.post("/wordcloud", response_model=list[WordCloudResponse])
async def wordcloud_api(request: WordCloudRequest):
    return generate_word_cloud_cached(request.content)
