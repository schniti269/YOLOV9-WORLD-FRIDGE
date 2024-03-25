import cv2
import supervision as sv
import pandas as pd
import os
from inference.models.yolo_world.yolo_world import YOLOWorld
from mss import mss
from PIL import Image
import numpy as np

# Initialize the YOLO World model
model = YOLOWorld(model_id="yolo_world/s")

# Define the classes for detection
kitchen_items = [
    "Banana","Lemon","Orange","Grapes", "Mango","Apple","Pineapple",
    "Avocado","Cherry","Strawberry","Watermelon","Peach",

    "Lettuce", "Tomato", "Mushroom", "Zucchini", "Potato",
    "Carrot", "Cucumber", "Bell Pepper", "Onion", "Garlic",
    "Eggplant", "Broccoli", "Cauliflower", "Spinach", "Cabbage",
    "Asparagus", "Green Beans", "Peas", "Corn", "Celery",


    "Chicken-meat", "Beef-meat", "Fish-meat", "Pork-meat",
    "Bacon", "Sausage", "Ham", "Salami", "Turkey meat",
    "ground-meat",

    "Milk", "Cheese", "Butter", "Yogurt", "Sour Cream",


    "Water bottle", "Juice bottle", "Soft Drink bottle","Beer bottle", "Wine bottle",
    "Liquor bottle", "Tea", "Coffee can", "Energy Drink can", "Soda can",


    "Bread", "Cereal", "Pasta", "Rice", "Flour",


    "Sugar", "Salt", "Pepper", "Spices", "Oil",


    "Mayonnaise", "Mustard", "Ketchup", "Soy Sauce", "Vinegar",
]
kitchen_items=[item.lower() for item in kitchen_items]

#kitchen_items=["lane marking","road barrier","wall","Car","vehicle","truck","motorcycle","human","traffic sign","stoplight","building"]
model.set_classes(kitchen_items)
# MSS setup for capturing a specific window
sct = mss()

# You need to know the title of the window or some part of it to capture its content
# This is a placeholder; you'd need to find the title of your window


# This function is a placeholder. On Linux, finding a window by its title and getting its coordinates
# is not straightforward with mss alone. You may need additional tools or libraries,
# such as `wmctrl` (for window management) and parsing its output to find your window.
def find_window_coordinates():
    # Implement the logic to find your window's coordinates here
    # Example return format: {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    #return {'top': 280, 'left': 30, 'width': 850, 'height': 500}
    return {'top': 400, 'left': 20, 'width': 800, 'height': 650}
# Attempt to find the window and its coordinates (you'll need to implement this)
window_coordinates = find_window_coordinates()

try:
    while True:
        # Capture the window content
        sct_img = sct.grab(window_coordinates)
        # Convert to an array that OpenCV can use
        frame = np.array(Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb))

        # Convert RGB to BGR format which OpenCV expects
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Perform inference
        results = model.infer(frame, confidence=0.1, iou=0.03, visualize=True)

        # Convert results to detections
        detections = sv.Detections.from_inference(results)

        # Annotate the frame with detections
        BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=1)
        LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=1, text_scale=0.5, text_color=sv.Color.BLACK)
        
        annotated_frame = BOUNDING_BOX_ANNOTATOR.annotate(frame, detections)
        annotated_frame = LABEL_ANNOTATOR.annotate(annotated_frame, detections)

        # Display the resulting frame
        cv2.imshow('YOLOv9 World Detection', annotated_frame)

        # Break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cv2.destroyAllWindows()