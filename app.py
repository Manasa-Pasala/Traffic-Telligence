from flask import Flask, render_template, request
from predict import predict_traffic
import os

app = Flask(_name_)

UPLOAD_FOLDER = 'Data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded."
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    result = predict_traffic(filepath)
    return render_template('result.html', prediction=result)

if _name_ == '_main_':
    app.run(debug=True)
