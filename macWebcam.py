import pyautogui
import cv2
import numpy as np
from ultralytics import YOLOWorld

# Initialize the YOLO model
model = YOLOWorld('yolov8s-worldv2.pt')
model.set_classes(["lane marking", "road barrier", "wall", "Car", "vehicle", "truck", "motorcycle", "human", "traffic sign", "stoplight", "building"])

# Function to capture a specific region of the screen
def capture_screen_region(x, y, width, height):
    # Capture the specified region of the screen
    image = pyautogui.screenshot(region=(x, y, width, height))
    # Convert the captured image to an OpenCV format
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Define the region of the screen you want to capture (x, y, width, height)
x, y, width, height = 100, 100, 600, 400  # Example values

# Loop to continuously capture and process the screen region
try:
    while True:
        # Capture the image from the defined screen region
        captured_image = capture_screen_region(x, y, width, height)

        # Apply the model to the captured image
        # Ensure to preprocess the image as required by your specific model implementation
        results = model(captured_image)

        # Process the results (this might include displaying the detections, logging, etc.)
        # Example: print(results) or use cv2.imshow() to display the frame with detections

        # Break the loop by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    cv2.destroyAllWindows()
