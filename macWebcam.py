import pyautogui
import cv2
import numpy as np
from ultralytics import YOLOWorld

# Initialize the YOLO model
model = YOLOWorld('yolov8s-worldv2.pt')
model.set_classes(["lane marking", "road barrier", "wall", "Car", "vehicle", "truck", "motorcycle", "human", "traffic sign", "stoplight", "building"])

# Function to draw bounding boxes and labels on the frame
def draw_detections(frame, detections):
    # Loop through each detection in the result
    for det in detections:
        # Example: Assuming each 'det' has 'x1', 'y1', 'x2', 'y2', 'label', and 'confidence'
        x1, y1, x2, y2, label, confidence = det['x1'], det['y1'], det['x2'], det['y2'], det['label'], det['confidence']
        
        # Draw a bounding box rectangle and label on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Function to capture a specific region of the screen
def capture_screen_region(x, y, width, height):
    image = pyautogui.screenshot(region=(x, y, width, height))
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

x, y, width, height = 100, 100, 600, 400  # Example values

try:
    while True:
        captured_image = capture_screen_region(x, y, width, height)

        # Apply the model to the captured image (adjust according to your model's input requirements)
        results = model(captured_image)

        # Draw detections on the image (this step will vary based on your results object structure)
        # Example: draw_detections(captured_image, results.detections)

        # Display the frame
        cv2.imshow('Screen Capture with Detections', captured_image)

        # Break the loop by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    cv2.destroyAllWindows()
