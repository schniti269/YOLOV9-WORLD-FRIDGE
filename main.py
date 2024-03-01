import cv2
import supervision as sv

from tqdm import tqdm
from inference.models.yolo_world.yolo_world import YOLOWorld

import os
HOME = os.getcwd()

SOURCE_IMAGE_PATH = r'C:\Users\ian-s\Repositories\YOLOV9-WORLD-FRIDGE\FridgeCam_Lifestyle2_800x.webp'

model = YOLOWorld(model_id="yolo_world/l")


kitchen_items = [
    "Bananas", "Blueberries", "Citrus (Lemons, Oranges)", "Grapes", "Mangoes",
    "Leafy Greens (Spinach, Lettuce)", "Tomatoes", "Mushrooms", "Zucchini", "Potatoes",
    "Chicken meat", "Beef meat", "Fish meat", "Pork meat", "Eggs",
    "Milk", "Cheese", "Butter", "Yogurt", "Cream",
    "Water", "Juices", "Soft Drinks", "Beer", "Wine",
    "Bread", "Cereal", "Pasta", "Rice", "Flour",
    "Sugar", "Salt", "Pepper", "Spices", "Oil",
    "Tomato Sauce", "Mayonnaise", "Mustard", "Ketchup", "Soy Sauce",
    "paprika","pak choi","peas","pepper","pineapple","pomegranate","potato","pumpkin","radish","raspberry",
    "onion","packaged food"
]

classes= kitchen_items

model.set_classes(classes)

image = cv2.imread(SOURCE_IMAGE_PATH)
results = model.infer(image,confidence=0.1,iou=0.1)

print(results)
detections = sv.Detections.from_inference(results)
BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=2)
LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=2, text_scale=1, text_color=sv.Color.BLACK)
annotated_image = image.copy()
annotated_image = BOUNDING_BOX_ANNOTATOR.annotate(annotated_image, detections)
annotated_image = LABEL_ANNOTATOR.annotate(annotated_image, detections)
sv.plot_image(annotated_image, (10, 10))