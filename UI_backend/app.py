import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

AI_BACKEND_URL = "http://ai-backend:5000/detect"  # URL of the AI Backend


# Route to handle image upload and forward to AI backend
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']
    files = {'image': image.read()}

    # Send image to AI Backend for object detection
    response = requests.post(AI_BACKEND_URL, files=files)

    if response.status_code != 200:
        return jsonify({"error": "Error from AI Backend"}), 500

    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
