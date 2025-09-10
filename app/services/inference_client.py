# Mock inference client
# Có thể thay bằng gọi API model thật
async def call_inference(text: str):
    # TODO: call model REST API / gRPC
    # Tạm thời trả về giá trị giả lập
    return "neutral", 0.85
