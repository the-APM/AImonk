import os
import cv2
import torch
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify


app = Flask(__name__)

# Load YOLOv3 model (running on CPU)
device = torch.device('cpu')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Object detection function
def detect_objects(image_path, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Perform object detection
    results = model(img)

    # Get detection results (bounding boxes, labels, and confidences)
    #detections = results.pandas().xywh[0].to_dict(orient='records')
    detections = results.pandas().xyxy[0].to_dict(orient='records')

    # Draw bounding boxes on the image
    for detection in detections:
        x_min, y_min, x_max, y_max = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
        label = detection['name']
        confidence = detection['confidence']
        # Draw rectangle around detected object
        cv2.rectangle(img_array, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=2)
        # Add label and confidence score
        text = f"{label}: {confidence:.2f}"
        cv2.putText(img_array, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=1)

    # Save the image with bounding boxes
    cv2.imwrite(output_path, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

    return detections

# Route to handle object detection
@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']
    image_path = os.path.join('uploads', image.filename)
    image.save(image_path)
    output_path = os.path.join('outputs',"results.jpg")
    # Perform detection
    detections = detect_objects(image_path, output_path)

    # Prepare output response
    response = {
        "status": "success",
        "detections": detections
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
