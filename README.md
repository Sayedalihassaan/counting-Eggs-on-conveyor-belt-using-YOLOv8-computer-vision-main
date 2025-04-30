
---

# 🧠 AI Safety & Vision Projects Collection

This repository contains multiple computer vision projects using **YOLOv5 and YOLOv8**, including:

1. 🦺 **Helmet & Vest Detection**
2. 🤟 **Sign Language Recognition**
3. 🟦 **YOLOv8 Segmentation Wrapper**

---

## 📁 Repository Structure

```
📦 AI-Safety-Vision-Projects/
├── Helmet_Vest_Detection/
│   └── vest and helmet.ipynb
├── Sign_Language_Detection/
│   └── Sign_Language_Detection.ipynb
├── Segmentation_Module/
│   └── yolo_segmentation.py
└── README.md
```

---

## 1️⃣ Helmet & Vest Detection

Detects construction workers and identifies whether they’re wearing **helmets and safety vests** using a custom-trained YOLOv5 model.

**Features:**
- Detects `Helmet`, `Vest`, and `Worker`
- Identifies safety violations and saves violator snapshots
- Processes and annotates video (`output.mp4`)

**Usage:**
- Place video and model in the correct path
- Run `vest and helmet.ipynb`

---

## 2️⃣ Sign Language Detection

Recognizes **A-Z alphabet signs** from hand gestures using YOLOv8.

**Features:**
- Uses YOLOv8 for high-accuracy detection
- Trained on hand sign datasets
- Real-time or image-based predictions

**Run With:**
```bash
pip install ultralytics==8.0.196
```
Open `Sign_Language_Detection.ipynb` and follow the steps.

---

## 3️⃣ YOLOv8 Segmentation Module

A reusable Python class for performing **object detection and segmentation** with YOLOv8.

**`yolo_segmentation.py`**:
```python
from yolo_segmentation import YOLO_SEGMENTATION

model = YOLO_SEGMENTATION("path_to_model.pt")
bboxes, class_ids, scores, masks = model.detection(image)
```

**Returns**:
- Bounding boxes
- Class IDs
- Confidence scores
- Polygon masks (in pixel coordinates)

---

## 🧰 Installation

Install common dependencies:

```bash
pip install ultralytics opencv-python numpy
```

---

## 🤝 Contributing

Feel free to fork, open issues, or submit pull requests if you'd like to contribute or improve the models/modules.

---

## 📝 License

These projects are released for educational and non-commercial use. Contact the author for commercial licensing.

---
