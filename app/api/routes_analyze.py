from fastapi import APIRouter
from app.models.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.analyze_service import analyze_item

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_api(request: AnalyzeRequest):
    results = []
    for item in request.data:
        result = await analyze_item(item.dict())
        results.append(result)
    return {"results": results}
