import re, json, hashlib
from pyvi import ViTokenizer
from app.models.wordcloud import WordCloudResponse
from app.core.cache import redis_client

def _cache_key(content: str) -> str:
    return "wc:" + hashlib.md5(content.encode("utf-8")).hexdigest()

def generate_word_cloud(content: str):
    tokenized_content = ViTokenizer.tokenize(content)
    words = re.findall(r'\w+', tokenized_content.lower())

    # meaningful words: có "_" và có ít nhất 1 ký tự chữ hoặc số
    meaningful_words = [
        word for word in words
        if "_" in word and re.search(r"[a-zA-Z0-9\u00C0-\u1EF9]", word)
    ]

    word_cloud_dict = {}
    for word in meaningful_words:
        word_cloud_dict[word] = word_cloud_dict.get(word, 0) + 1

    word_cloud = [WordCloudResponse(word=w, frequency=f) for w, f in word_cloud_dict.items()]
    word_cloud.sort(key=lambda x: x.frequency, reverse=True)
    return word_cloud

def generate_word_cloud_cached(content: str):
    key = _cache_key(content)
    if redis_client.exists(key):
        return [WordCloudResponse(**item) for item in json.loads(redis_client.get(key))]

    result = generate_word_cloud(content)
    redis_client.setex(key, 1800, json.dumps([r.dict() for r in result]))
    return result
