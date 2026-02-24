from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Nhận văn bản từ yêu cầu HTTP, phân tích cảm xúc và trả về kết quả định dạng chuỗi.
    """
    # Lấy văn bản người dùng nhập từ ô 'textToAnalyze' trên web
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Gọi hàm phân tích cảm xúc đã viết ở các Task trước
    response = emotion_detector(text_to_analyze)
    
    # Trích xuất các giá trị cảm xúc
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Trả về câu thông báo theo đúng định dạng yêu cầu của bài Lab
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Hiển thị giao diện chính của ứng dụng (file index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Chạy ứng dụng trên cổng 5000
    app.run(host="0.0.0.0", port=5000)
