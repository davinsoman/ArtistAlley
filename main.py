"""This is possible because of the __init__.py file in the website folder
that file turns the website folder into a python package that can be imported"""

from website import create_app 
from ai.model_access import predict_image
from flask import request, jsonify
import os

app = create_app()

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    img_path = os.path.join('/tmp', file.filename)
    file.save(img_path)

    prediction = predict_image(img_path)
    return jsonify({'prediction': prediction.tolist()})

"""This is the entry point for the application, if we run this file directly it will run the web server"""
if __name__ == '__main__':
    app.run(debug=True)