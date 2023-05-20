<div align="center">

![DermaAI Banner](static/Images/dermaai_banner.png)

# DermaAI – AI Skin Disease Detection & Recommendation System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

**A complete AI dermatology assistant that detects skin conditions, assesses severity, and delivers personalised skincare recommendations.**

*Developed as an Academic Research Project at the University of Petroleum and Energy Studies (UPES), Dehradun, Uttarakhand, India.*

[🔬 Try a Scan](#installation) · [📸 Screenshots](#screenshots) · [🧠 How It Works](#how-it-works)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **AI Disease Detection** | Classifies 9 skin conditions using a ResNet50 deep learning model |
| 📊 **Severity Assessment** | Each prediction includes a severity level: **Mild · Moderate · Severe** |
| 💊 **Skincare Recommendations** | Personalised treatment advice, preventive tips & daily routines |
| 📁 **Drag-and-Drop Upload** | Drop an image directly onto the upload zone |
| 📷 **Live Camera Capture** | Use your device camera for real-time skin image capture |
| 🕑 **Scan History** | Saves your 5 most recent predictions (with severity) locally |
| 🌙 **Dark / Light Mode** | Toggle between themes for comfort |
| 📱 **Responsive Design** | Optimised for mobile, tablet, and desktop |

---

## 🦠 Detectable Skin Conditions

| # | Condition | Severity |
|---|---|---|
| 1 | Actinic Keratosis | 🟡 Moderate |
| 2 | Atopic Dermatitis (Eczema) | 🟢 Mild |
| 3 | Benign Keratosis | 🟢 Mild |
| 4 | Dermatofibroma | 🟢 Mild |
| 5 | Melanocytic Nevus (Moles) | 🟢 Mild |
| 6 | **Melanoma** | 🔴 **Severe** |
| 7 | **Squamous Cell Carcinoma** | 🔴 **Severe** |
| 8 | Tinea Ringworm Candidiasis | 🟡 Moderate |
| 9 | Vascular Lesion | 🟡 Moderate |

---

## 🧠 How It Works

```
1. Upload Image  →  2. AI Analysis (ResNet50)  →  3. Disease + Confidence
                                                   4. Severity Level
                                                   5. Skincare Recommendations
```

1. **Upload or Capture** a clear photo of the affected skin area
2. The **ResNet50 model** analyses the image across 9 disease categories
3. Results include the **predicted disease**, **confidence %**, and **severity level**
4. The built-in **recommendation engine** provides treatment advice, prevention tips, and a skincare routine

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Backend** | Python 3, Flask |
| **ML Engine** | TensorFlow / Keras, ResNet50 |
| **Recommendation Engine** | Custom Python module (`utils/recommendations.py`) |
| **Dataset** | HAM10000 (10,000 dermatoscopic images, 9 classes) |

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/zairakhaan786/DermaAI.git
cd DermaAI

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and set a strong SECRET_KEY

# 5. Run the application
python app.py
```

Open **http://localhost:5000** in your browser.

> **Note:** The AI model requires TensorFlow. To use real predictions, place your trained `.h5` model at `model/dermaai_model.h5` and follow the instructions in [`model/README.md`](model/README.md).

---

## 📂 Project Structure

```
DermaAI/
├── app.py                      # Flask app — routes, validation, inference
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── runtime.txt                 # Python runtime specification
├── LICENSE                     # MIT License
├── utils/
│   ├── __init__.py
│   └── recommendations.py      # Severity levels + skincare recommendation engine
├── model/
│   └── README.md               # Instructions for loading the trained model
├── frontend/                   # Redesigned Medical UI (UPES Theme)
│   ├── assets/
│   │   ├── css/style.css       # Global styles (light/dark themes, medical palette)
│   │   ├── js/main.js          # Frontend logic (theme, camera, scan history)
│   │   ├── images/             # Static images and banner
│   │   └── uploads/            # Uploaded images (auto-created at runtime)
│   └── templates/
│       ├── index.html          # UPES Home / landing page
│       ├── prediction.html     # Scan, results, and recommendations page
│       ├── about.html          # About DermaAI project
│       ├── diseases.html       # Skin disease reference guide
│       └── contact.html        # Contact page
└── 80model_code.ipynb          # ResNet50 model training notebook
```

---

## 🚀 Usage

1. Go to the **Scan Now** page
2. **Drag & Drop** a skin image onto the upload zone, click **Browse File**, or click **Open Camera** for a live capture
3. Click **Analyse Now**
4. View your results:
   - 🏷️ **Predicted Condition** (disease name)
   - 📊 **Confidence Score** (animated percentage bar)
   - 🔴 **Severity Level** (colour-coded chip: Mild / Moderate / Severe)
   - 💊 **Recommendations** — treatment, prevention, skincare routine accordion
5. Consult a qualified dermatologist for a professional diagnosis

> ⚠️ **Disclaimer:** DermaAI is an educational tool only. It is not a substitute for professional medical advice.

---

## 📸 Screenshots

| Home Page | Scan Interface |
|:---:|:---:|
| ![Home Page](static/Images/home_page.png) | ![Prediction Page](static/Images/prediction_page.png) |

---

## 🔮 Future Improvements

- [ ] Integrate trained ResNet50 model for live predictions
- [ ] PDF report generation for scan results
- [ ] User authentication and persistent scan history (database)
- [ ] Multi-image batch upload and comparison
- [ ] Cloud deployment (Render / Railway / AWS)
- [ ] Multilingual interface support

---

## 👩‍💻 Author

**Zaira Khan**

- 📧 [Zaira.khan0304@gmail.com](mailto:Zaira.khan0304@gmail.com)
- 🐙 [GitHub – zairakhaan786](https://github.com/zairakhaan786)

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by Zaira Khan &nbsp;·&nbsp; Developed at UPES, Dehradun, India &nbsp;·&nbsp; DermaAI © 2026
</div>
