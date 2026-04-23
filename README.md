# 🌊 Ocean Heatwave Detection Challenge (AI-Based System)

## 📌 Project Overview

This project implements an AI-based system to detect marine heatwaves using oceanographic and environmental data.
It also includes a **live leaderboard system** where participants can submit their models and compare performance automatically.

---

## 🎯 Objective

* Detect marine heatwave conditions from ocean data
* Analyze environmental patterns affecting oceans
* Build machine learning models from scratch
* Compete using a real-time leaderboard

---

## 🏆 Live Leaderboard

🚀 Track model performance in real-time:

👉 **[🌐 View Leaderboard](https://praptikate.github.io/Ocean_Heatwave_Detection/)**

---

## 🚀 How to Participate

### 1️⃣ Fork the Repository

Click the **Fork** button (top right) to create your own copy.

---

### 2️⃣ Add Your Model

Add your model inside the `submissions/` folder:

```
submissions/your_name_model.py
```

---

### 3️⃣ Create a Pull Request (PR)

* Go to your forked repo
* Click **Compare & Pull Request**
* Submit your PR

---

### 4️⃣ Automatic Evaluation

Once your PR is created:

* Your model is evaluated automatically
* Accuracy & F1 Score are calculated
* Your name is added to the leaderboard

---

## 📂 Submission Format

Your submission must include this function:

```
def predict(X_train, y_train, X_test):
    return predictions
```

---

## 📜 Rules

* Do not modify `evaluate.py`
* Use the provided dataset only
* Follow the submission format strictly
* Submit only one model per PR

---

## ⚙️ Evaluation Process

Each Pull Request triggers an automated workflow:

1. Dataset is loaded
2. Your model is loaded
3. `predict()` function is executed
4. Performance metrics are calculated:

   * Accuracy
   * F1 Score
5. Leaderboard is updated automatically

---

## 📊 Dataset

Dataset used:
**Shifting Seas – Ocean Climate and Marine Life Dataset**

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Scikit-learn
* GitHub Actions
* GitHub Pages

---

## 🤝 Contributing

* Fork the repository
* Add your model
* Submit a Pull Request
* Check leaderboard for results

---

## 💡 Note

The leaderboard updates automatically after each Pull Request submission.
