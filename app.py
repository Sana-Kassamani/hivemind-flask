from flask import Flask,request
from model import predict

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World"

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    imagePath =f"./uploads/{file.filename}"
    file.save(imagePath)
    result = predict(imagePath=imagePath)
    print(result)
    return result, 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
