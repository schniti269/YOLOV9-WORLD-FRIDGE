import pyautogui
import cv2
import numpy as np
import torch
from ultralytics import YOLOWorld  # This should be adjusted to the correct import for YOLOv8

# Initialize the YOLO model
model = YOLOWorld('yolov8s-worldv2.pt')  # Adjust the model path and initialization as needed

# Function to capture a specific region of the screen
def capture_screen_region(x, y, width, height):
    image = pyautogui.screenshot(region=(x, y, width, height))
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Function to draw bounding boxes and labels on the frame
def draw_detections(frame, detections, classes):
    height, width, _ = frame.shape
    for *xyxy, conf, cls in detections:
        label = classes[int(cls)]
        x1, y1, x2, y2 = [int(xy) for xy in xyxy]  # Scale coordinates if necessary
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

x, y, width, height = 100, 100, 600, 400  # Example region coordinates

try:
    while True:
        captured_image = capture_screen_region(x, y, width, height)
        # Convert BGR to RGB
        captured_image_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
        # Convert to tensor and add batch dimension
        img_tensor = torch.from_numpy(captured_image_rgb).permute(2, 0, 1).unsqueeze(0).float()
        img_tensor /= 255.0  # Normalize to [0, 1]

        # Apply the model to the captured image
        results = model(img_tensor)

        # Extract detections (adjust indexing based on your model's output structure)
        detections = results.xyxy[0]  # Detections in xyxy format

        # Draw detections on the image
        draw_detections(captured_image, detections, model.names)

        # Display the frame
        cv2.imshow('Screen Capture with Detections', cv2.cvtColor(captured_image, cv2.COLOR_RGB2BGR))

        # Break the loop by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    cv2.destroyAllWindows()
