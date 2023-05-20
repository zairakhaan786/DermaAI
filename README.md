<div align="center">
  <img src="assets/homepage_screenshot_1772878799510.png" width="800" alt="DermaAI Banner">
  <br>
  <h1>DermaAI</h1>
  <p><strong>AI Skin Disease Detection and Recommendation System</strong></p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg" alt="Flask">
  <img src="https://img.shields.io/badge/TensorFlow-Keras-orange.svg" alt="Tensorflow">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg" alt="OpenCV">
</p>

---

## 🚀 Project Overview

**DermaAI** is an advanced artificial intelligence healthcare application designed to classify skin conditions, assess their severity, and provide tailored skincare recommendations. Built upon a custom-trained ResNet-50 Convolutional Neural Network, it empowers users with rapid, accessible, and highly accurate preliminary skin diagnostics.

This repository serves as a complete portfolio-ready template for deploying deep-learning vision models into a sleek, modern, user-friendly frontend.

---

## ✨ Key Features

- **🧠 Deep Learning Classification**: Detects 9 distinct skin conditions (Actinic Keratosis, Atopic Dermatitis, Benign Keratosis, Dermatofibroma, Melanocytic Nevus, Melanoma, Squamous Cell Carcinoma, Ringworm, and Vascular Lesions).
- **📊 Severity Assessment**: Automatically assigns a color-coded severity level (Mild, Moderate, Severe) to the diagnosed condition.
- **⚕️ AI Skincare Recommendations**: Generates immediate follow-up care instructions, including treatment options, prevention tips, and a recommended daily skincare routine.
- **📸 Real-Time Camera Scanner**: Capture skin images directly from a webcam instantly through the UI using web APIs and OpenCV integration—no file upload required.
- **🎨 Modern Aesthetic UI**: Features a beautiful glassmorphic design, dynamic mesh gradients, dark mode toggle, and micro-animations for a premium user experience.

---

## 💻 Tech Stack

- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism UI), JavaScript, Bootstrap 5
- **Backend**: Python 3, Flask framework, Werkzeug
- **Machine Learning**: TensorFlow, Keras, ResNet-50, Scikit-learn, Numpy, Pillow, OpenCV

---

## 📸 Screenshots

<div align="center">
  <h3>The Scan Interface</h3>
  <img src="assets/upload_scanner_1772878816471.png" width="600" alt="Scanner UI">
  <br><br>
  <h3>AI Analysis Result Card</h3>
  <img src="assets/result_card_1772878831306.png" width="600" alt="Results UI">
</div>

---

## ⚙️ Installation Guide

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zairakhaan786/DermaAI.git
   cd DermaAI
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the Model:**
   Ensure your trained `skin_model.h5` file is placed inside the `model/` directory.

---

## ▶️ How to Run the Project

1. **Start the Flask Server:**
   ```bash
   python app.py
   ```
2. **Access the App:**
   Open your browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```text
/DermaAI
│
├── app.py                 # Core Flask application & routing
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── /model                 # Contains the trained neural network (e.g., skin_model.h5)
│
├── /utils                 # Helper scripts
│   └── recommendations.py # Logic for severity & skincare advice
│
├── /templates             # HTML Views
│   ├── index.html         # Landing page
│   ├── prediction.html    # Upload & Result dashboard
│   └── ...
│
├── /static                # Static frontend assets
│   ├── css/style.css      # Modern Glassmorphic Styles
│   ├── js/main.js         # Camera & UI Logic
│   └── uploads/           # Temporarily saved user scans
│
└── /assets                # High-quality UI mockups for documentation
```

---

## 🔮 Future Improvements

- [ ] Connect a PostgreSQL or MongoDB database to store past user scans and diagnoses securely.
- [ ] Implement user authentication (OAuth) for personalized dashboard history.
- [ ] Expand the classification model to support more rare skin conditions.
- [ ] Deploy the application to a cloud provider like AWS, Heroku, or Render.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<p align="center">
  <i>Developed at UPES, Dehradun, India | © 2023 Zaira Khan</i>
</p>
