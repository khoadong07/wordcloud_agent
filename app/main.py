from fastapi import FastAPI
from app.api import routes_wordcloud, routes_analyze

def create_app() -> FastAPI:
    app = FastAPI(title="WordCloud & Analyze API", version="1.0.0")
    app.include_router(routes_wordcloud.router, prefix="/api")
    app.include_router(routes_analyze.router, prefix="/api")
    return app

app = create_app()
