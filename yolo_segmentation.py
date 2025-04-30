from ultralytics import YOLO
import numpy as np


class YOLO_SEGMENTATION:
    def __init__(self, path_model):
        self.model = YOLO(path_model)
        
    def detection(self, image):
        height, width, channels = image.shape
    
        results = self.model.predict(source=image.copy(), save=False, save_txt=False)
        result = results[0]
        l = len(result)

        segmentation_contours_idx = []

        if l > 0:
            for seg in result.masks.xy:  # Use `xy` for pixel coordinates
                # contours
                seg[:, 0] *= width
                seg[:, 1] *= height

                segment = np.array(seg, dtype=np.int32)
                segmentation_contours_idx.append(segment)

        bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")

        # Get class ids
        classes_id = np.array(result.boxes.cls.cpu(), dtype="int")

        # Get scores
        scores = np.array(result.boxes.conf.cpu(), dtype="float").round(3)

        return bboxes, classes_id, scores, segmentation_contours_idx
