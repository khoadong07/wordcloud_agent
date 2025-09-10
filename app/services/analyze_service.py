from app.services.wordcloud_service import generate_word_cloud
from app.services.inference_client import call_inference

async def analyze_item(item: dict):
    id_ = item.get("id")
    title = item.get("title", "")
    description = item.get("description", "")
    content = item.get("content", "")
    item_type = item.get("type", "")

    is_meaningless = not any(c.isalnum() for c in content)

    if is_meaningless:
        if item_type.upper() in ["fbPageTopic", "fbGroupTopic", "fbUserTopic"]:
            text = f"{title} {description} {content}"
        else:
            text = content
    else:
        text = content

    word_cloud = generate_word_cloud(text)

    return {
        "id": id_,
        "word_cloud": [w.dict() for w in word_cloud]
    }
