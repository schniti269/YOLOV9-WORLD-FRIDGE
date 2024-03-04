import pyautogui
import cv2
import numpy as np
from ultralytics import YOLOWorld

# Initialize the YOLO model
model = YOLOWorld('yolov8s-worldv2.pt')
# Assuming the set_classes method exists and sets the classes for detection
model.set_classes(["lane marking", "road barrier", "wall", "Car", "vehicle", "truck", "motorcycle", "human", "traffic sign", "stoplight", "building"])

# Function to draw bounding boxes and labels on the frame
def draw_detections(frame, detections):
    for det in detections:
        x1, y1, x2, y2 = int(det['x1']), int(det['y1']), int(det['x2']), int(det['y2'])
        label = det['label']
        confidence = det['confidence']
        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Put the label and confidence
        cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

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

        # Convert captured image to the format expected by your model if necessary
        # Apply the model to the captured image
        results = model(captured_image)  # This step is hypothetical and depends on your actual model API

        # Process the results to match the expected format for draw_detections
        # This is a placeholder and needs to be adapted based on your model's output
        detections = [{"x1": det.x1, "y1": det.y1, "x2": det.x2, "y2": det.y2, "label": det.label, "confidence": det.confidence} for det in results]

        # Draw detections on the image
        draw_detections(captured_image, detections)

        # Display the frame
        cv2.imshow('Screen Capture with Detections', captured_image)

        # Break the loop by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    cv2.destroyAllWindows()
