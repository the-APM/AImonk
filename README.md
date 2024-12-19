# AImonk Data Scientist Assignment

# Object Detection Microservice

This project consists of two main components:

1. **AI Backend**: Uses YOLOv5 for object detection.
2. **UI Backend**: Accepts image uploads from the user and forwards them to the AI Backend for processing.

## Prerequisites
- Git
- Docker
- Docker Compose
- Python (for testing locally without Docker)

## Setup
- Clone the repo.
- Build using the docker-compose file.
    ```bash
  docker-compose up --build
- This will start both the microservices with the UI_backend service working at <mark>http://localhost:5001</mark>.

## Endpoint
- The AI_backend microservice is called from the UI_backend and the image file is passed along for object detection using a pretrained YOLOv5 model.
- Access the UI_backend by sending a POST request at <mark>http://localhost:5001/upload </mark>. The body of the request would require the image file to be passed with the key "image".
- On successful execution, A json object would be returned with the list of detections.

## Example
### Detection output

![results_1.jpg](output%2Fresults_1.jpg)
### Json reponse
```json
{
    "detections": [
        {
            "class": 0,
            "confidence": 0.9271733164787292,
            "name": "person",
            "xmax": 651.8099975585938,
            "xmin": 566.7919921875,
            "ymax": 382.7475891113281,
            "ymin": 139.59620666503906
        },
        {
            "class": 2,
            "confidence": 0.9187636971473694,
            "name": "car",
            "xmax": 390.26116943359375,
            "xmin": 65.77389526367188,
            "ymax": 357.4227294921875,
            "ymin": 163.9805145263672
        },
        {
            "class": 16,
            "confidence": 0.8239849209785461,
            "name": "dog",
            "xmax": 438.2268371582031,
            "xmin": 388.6556091308594,
            "ymax": 394.4292907714844,
            "ymin": 343.7625732421875
        },
        {
            "class": 27,
            "confidence": 0.7577967643737793,
            "name": "tie",
            "xmax": 627.0595703125,
            "xmin": 613.6806640625,
            "ymax": 230.87982177734375,
            "ymin": 180.4173583984375
        }
    ],
    "status": "success"
}
```
## References

The project uses YoloV5 because of it's versatile and light-weight nature.
All details about the model can be found on it's official github page:
https://github.com/ultralytics/yolov5

