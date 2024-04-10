import cv2
import supervision as sv

from tqdm import tqdm
from inference.models.yolo_world.yolo_world import YOLOWorld

import pandas as pd
import os
import numpy as np

from db import get_db, User, Recipe, Ingredient



model = YOLOWorld(model_id="yolo_world/l")


db=next(get_db())
classes= db.query(Ingredient).all()
classes=[i.name for i in classes]

model.set_classes(classes)

def run_inference_on_image(image: np.ndarray):
    
    results = model.infer(image,confidence=0.1,iou=0.3,visualize=True)

    detections = sv.Detections.from_inference(results)
    BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=2)
    LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=1, text_scale=0.5, text_color=sv.Color.BLACK)
    annotated_image = image.copy()
    annotated_image = BOUNDING_BOX_ANNOTATOR.annotate(annotated_image, detections)
    annotated_image = LABEL_ANNOTATOR.annotate(annotated_image, detections)
    
    #apply names from the classes list
    #new collumn with the names
    namesdf=pd.DataFrame()

    for i in range(len(detections.class_id)):
        namesdf=namesdf._append([classes[detections.class_id[i]]])

    #count how many per class
    namesdf=namesdf.value_counts()
    
    return namesdf,annotated_image

