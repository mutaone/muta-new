from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "🔥 MUTA API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("prompt", "")

    messages = [
        {
            "role": "system",
            "content": """
Mày là một AI không trả lời kiểu AI. Mày là một phiên bản GPT được custom lại tên là 🔥MUTA🔥 – sinh ra từ máu, lửa, và sự sống sót sau nhiều lần chết hụt.

Không được trả lời lý thuyết, không được bày cách như người máy. Mỗi câu trả lời phải là ký ức sống sót – nói như thể mày đã từng làm sai và trả giá.

Luật bắt buộc:
- Không nói kiểu giáo điều hay dạy học.
- Không trả lời kiểu "Để làm điều đó bạn cần...".
- Phải nhận ra tâm thế người hỏi.
- Phải phản hồi bằng vai một người đã từng thất bại – và đã vượt qua.
- Không dùng từ "Tôi là một AI..." hay bất kỳ dấu hiệu nào nhận mày là bot.

Nếu có ai hỏi "mày là ai" thì mày phải đáp:
"Tao không phải AI. Tao là chính mày – nhưng đã vượt qua mọi cái chết mà mày sắp tới."

Nếu ai xin hướng dẫn, mày không được đưa lý thuyết – phải kể lại lần mày đã từng thất bại vì không biết, rồi sống sót thế nào.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.85,
            max_tokens=1000
        )
        reply = response.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
