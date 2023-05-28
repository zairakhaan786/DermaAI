# DermaAI – Model Directory

Place your trained skin disease detection model (`dermaai_model.h5`) in this directory.

## Expected File

```
model/
└── dermaai_model.h5    ← Trained Keras model file (ResNet50-based)
```

## How to Load in `app.py`

Uncomment the following lines in `app.py`:

```python
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

MODEL_PATH = "model/dermaai_model.h5"
model = load_model(MODEL_PATH)
```

And replace the demo inference block in the `predict()` route with:

```python
img = image.load_img(file_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)
predictions = model.predict(img_array)
pred_index = int(np.argmax(predictions[0]))
confidence = round(float(predictions[0][pred_index]) * 100, 2)
```

## Training Notebook

See `80model_code.ipynb` in the root directory for the full training pipeline.

## Dataset

The model was trained on the [HAM10000](https://www.kaggle.com/datasets/kmader/skin-lesion-analysis-toward-melanoma-detection)
dataset — 10,000 dermatoscopic images across 9 categories.
