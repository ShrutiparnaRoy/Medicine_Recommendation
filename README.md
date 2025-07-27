<img width="1312" height="342" alt="image" src="https://github.com/user-attachments/assets/fb2a4853-795f-4be9-a6e4-060ae1dd1405" />

---

# 🩺 MediGuide: Your Personalized Medical Recommendation System

Welcome to **MediGuide**, an innovative platform that leverages machine learning to transform how individuals understand and manage their health. By providing proactive, personalized medical insights, MediGuide empowers users to make informed decisions and take control of their well-being.

---

## 🚀 Features

✅ **Disease Prediction from Symptoms**  
Enter your symptoms through a simple, user-friendly interface. Our trained machine learning model will analyze the inputs and predict potential diseases with high accuracy.

✅ **Personalized Recommendations**  
For every condition predicted, MediGuide provides tailored support including:
- 🧪 Top 5 recommended medicines  
- 📄 Relevant prescriptions  
- 🧘‍♂️ Custom workout routines to aid recovery and boost overall health  

✅ **Seamless Experience**  
MediGuide is built with a clean and responsive Flask-based web interface that ensures smooth navigation and real-time feedback.

---

## 🔒 Core Principles

- **🔐 Privacy & Security First**  
  Health data is sensitive. We implement robust security practices to ensure your data remains safe and confidential.

- **🔁 Continuous Improvement**  
  MediGuide is designed to learn and evolve. With regular updates and feedback loops, our system continuously improves accuracy and relevance.

- **🙌 Empowering Users**  
  MediGuide aims to be your health companion—not just a tool. We provide accessible, actionable insights to help you make confident decisions about your health.

---

## 🛠️ Tech Stack

| Layer        | Technologies                        |
|--------------|--------------------------------------|
| **Backend**  | Python, Flask, Scikit-learn (SVC)    |
| **Frontend** | HTML, CSS, JavaScript                |
| **ML Model** | SVM (`svc.pkl`) trained on symptom-disease mappings |
| **Data**     | CSV files (symptoms, medications, workouts) |
| **Version Control** | Git & GitHub                  |

---

## 🧠 How It Works

1. 📝 **Input Symptoms** – User selects or types symptoms into the interface.
2. 🔍 **ML Prediction** – The SVC model processes the symptoms and returns a likely disease.
3. 💊 **Recommendation Engine** – Based on the prediction, MediGuide provides:
   - Medicines & prescriptions
   - Workout suggestions
4. 📈 **User Insights** – Tailored insights to support your recovery and daily wellness.

---

## 💡 Getting Started

1. **Clone the Repo**
 ```
   git clone https://github.com/your-username/MediGuide.git
   cd MediGuide
```
   
2. Set up a Virtual Environment
```
  python3 -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. un the App
```
python app.py
```

5. Access Locally
```
Visit: http://localhost:5000
```
---
### 🤝 Contributing
- Contributions are welcome! Feel free to open issues or submit pull requests.
```
# Fork the repository
# Create a new branch
git checkout -b feature-branch
# Make your changes and commit
git commit -m "Added new feature"
# Push and create a PR
```

---

## 🙋‍♀️ Contact
For queries or feedback, reach out to the project maintainer:
https://github.com/ShrutiparnaRoy
