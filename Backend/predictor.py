import cv2
import supervision as sv

from tqdm import tqdm
from inference.models.yolo_world.yolo_world import YOLOWorld

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from db import get_db, User, Recipe, Ingredient

print("loading model")

model = YOLOWorld(model_id="yolo_world/l")
db=next(get_db())
ingredients = db.query(Ingredient).all()
classes=[ingredient.name for ingredient in ingredients]



model.set_classes(classes)

print("model loaded")
def run_inference_on_image(image):
    
    results = model.infer(image,confidence=0.01,iou=0.3)

    detections = sv.Detections.from_inference(results)
    BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=2)
    LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=1, text_scale=0.5, text_color=sv.Color.BLACK)
    annotated_image = image.copy()
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
    annotated_image = BOUNDING_BOX_ANNOTATOR.annotate(annotated_image, detections)
    annotated_image = LABEL_ANNOTATOR.annotate(annotated_image, detections)

    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    
    
    #apply names from the classes list
    #new collumn with the names
    namesdf=pd.DataFrame()

    for i in range(len(detections.class_id)):
        namesdf=namesdf._append([classes[detections.class_id[i]]])

    #count how many per class
    namesdf=namesdf.value_counts()

    #make it set
    myDict = namesdf.to_dict()

    
    return myDict,annotated_image

