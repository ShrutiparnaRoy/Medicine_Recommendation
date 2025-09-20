# 🌟 MediGuide: Your Personalized Medical Recommendation System

Welcome to **MediGuide**, an innovative project that harnesses the power of machine learning to transform how you understand and manage your health. Our goal is to provide proactive, personalized insights directly to you, helping you navigate your health journey with greater confidence.

---

## 🚀 Features

- **Disease Prediction from Symptoms:**  
  Input your symptoms into our user-friendly interface, and our machine learning models will analyze them to predict potential diseases with high accuracy.

- **Tailored Recommendations:**  
  For each predicted condition, MediGuide provides:
  - Top 5 relevant medicines
  - Corresponding prescriptions
  - Customized workout routines
  - Diet suggestions
  - Precautionary measures

- **Seamless User Experience:**  
  Built with a sleek and intuitive Flask web application, ensuring that accessing your health insights is straightforward and hassle-free.

---

## 🛡️ Core Principles

- **Privacy and Security First:**  
  Protecting your health data is our top priority. Robust security measures ensure your privacy is always maintained.

- **Continuous Improvement:**  
  MediGuide learns and improves over time, refining its recommendations based on new data and real-world feedback.

- **Empowering Your Health Journey:**  
  MediGuide is your partner in health, providing accessible, personalized information to help you make informed decisions.

---

## 🧑‍💻 Technologies Used

| Layer      | Technologies                                   |
|------------|------------------------------------------------|
| Backend    | Python, Flask, Scikit-learn (SVC model)        |
| Frontend   | HTML, CSS, JavaScript                          |
| Data       | CSV datasets (symptoms, medications, workouts) |
| ML Model   | SVM (`svc.pkl`) trained on symptom-disease mappings |
| Version Control | GitHub                                    |

---

## 📁 Project Structure

```
Medicine_Recommendation/
│
├── frontend/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── developer.html
│   ├── blog.html
│   └── images/
│        └── MediGuide.png
│
├── trainingdataset/
│   ├── symptoms_df.csv
│   ├── precautions_df.csv
│   ├── workout_df.csv
│   ├── description.csv
│   ├── medications.csv
│   └── diets.csv
│
├── Medicine/
│   └── trainingdataset/
│        └── symtoms_df.csv
│
├── svc.pkl
├── main.py
├── README.md
└── requirements.txt
```

### **Key Folders & Files**

- **frontend/**  
  Contains all HTML templates and static assets for the web interface.

- **trainingdataset/**  
  Houses the CSV datasets used for training and recommendations:
  - `symptoms_df.csv`: Symptom data
  - `precautions_df.csv`: Precautionary measures
  - `workout_df.csv`: Workout routines
  - `description.csv`: Disease descriptions
  - `medications.csv`: Medication recommendations
  - `diets.csv`: Diet suggestions

- **Medicine/trainingdataset/**  
  Additional symptom dataset for model training.

- **svc.pkl**  
  Pre-trained SVM model for disease prediction.

- **main.py**  
  Flask application backend, handles routing, prediction logic, and rendering templates.

- **requirements.txt**  
  Lists all Python dependencies for easy setup.

---

## 📝 Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/Medicine_Recommendation.git
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Flask app:**
   ```
   python main.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000/
   ```

---

## 🤝 Contributing

We welcome contributions! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📜 License

This project is licensed under the MIT License.

---

> **MediGuide** is your companion for smarter, data-driven health decisions.  
> Stay healthy, stay informed!