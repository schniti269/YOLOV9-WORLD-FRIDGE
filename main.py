import cv2
import supervision as sv

from tqdm import tqdm
from inference.models.yolo_world.yolo_world import YOLOWorld

import pandas as pd
import os

# Path to the image
#get the  newest .jpg file in the folder
files=os.listdir()
files.sort(key=os.path.getmtime)
images=[]
for file in files:
    if file.endswith(".jpeg"):
        images.append(file)
        break

SOURCE_IMAGE_PATH = images[-1]

model = YOLOWorld(model_id="yolo_world/s")


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
    "onion","packaged food","egg","coconut","cucumber"
]

classes= kitchen_items

model.set_classes(classes)

image = cv2.imread(SOURCE_IMAGE_PATH)
results = model.infer(image,confidence=0.1,iou=0.3,visualize=True)

detections = sv.Detections.from_inference(results)
BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=2)
LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=2, text_scale=1, text_color=sv.Color.BLACK)
annotated_image = image.copy()
annotated_image = BOUNDING_BOX_ANNOTATOR.annotate(annotated_image, detections)
annotated_image = LABEL_ANNOTATOR.annotate(annotated_image, detections)
sv.plot_image(annotated_image, (10, 10))




#apply names from the classes list
#new collumn with the names
namesdf=pd.DataFrame()

for i in range(len(detections.class_id)):
    namesdf=namesdf._append([classes[detections.class_id[i]]])

#count how many per class
namesdf=namesdf.value_counts()
print(namesdf)
