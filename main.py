from flask import Flask, request, render_template, jsonify  # Import jsonify
import numpy as np
import pandas as pd
import pickle

# flask app
app = Flask(__name__)

# load databasedataset===================================
sym_des = pd.read_csv("/Medicine_Recommendation/Medicine/trainingdataset/symtoms_df.csv")
precautions = pd.read_csv("/Medicine_Recommendation/trainingdataset/precautions_df.csv")
workout = pd.read_csv("/Medicine_Recommendation/trainingdataset/workout_df.csv")
description = pd.read_csv("/Medicine_Recommendation/trainingdataset/description.csv")
medications = pd.read_csv('/Medicine_Recommendation/trainingdataset/medications.csv')
diets = pd.read_csv("/Medicine_Recommendation/training/dataset/diets.csv")

# load model===========================================
svc = pickle.load(open('/Medicine_Recommendation/svc.pkl','rb'))

#============================================================
# custome and helping functions
#==========================helper funtions================
def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [med for med in med.values]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [die for die in die.values]

    wrkout = workout[workout['disease'] == dis] ['workout']

    return desc,pre,med,die,wrkout

symptoms_dict = {...}  # ...existing code...
diseases_list = {...}  # ...existing code...

# Model Prediction function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        input_vector[symptoms_dict[item]] = 1
    return diseases_list[svc.predict([input_vector])[0]]

# creating routes========================================

@app.route("/")
def index():
    return render_template("/Medicine_Recommendation/frontend/index.html")

@app.route('/predict', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        print(symptoms)
        if symptoms =="Symptoms":
            message = "Please either write symptoms or you have written misspelled symptoms"
            return render_template('/Medicine_Recommendation/frontend/index.html', message=message)
        else:
            user_symptoms = [s.strip() for s in symptoms.split(',')]
            user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
            predicted_disease = get_predicted_value(user_symptoms)
            dis_des, precautions, medications, rec_diet, workout = helper(predicted_disease)

            my_precautions = []
            for i in precautions[0]:
                my_precautions.append(i)

            return render_template('/Medicine_Recommendation/frontend/index.html', predicted_disease=predicted_disease, dis_des=dis_des,
                                   my_precautions=my_precautions, medications=medications, my_diet=rec_diet,
                                   workout=workout)

    return render_template('/Medicine_Recommendation/frontend/index.html')

@app.route('/about')
def about():
    return render_template("/Medicine_Recommendation/frontend/about.html")

@app.route('/contact')
def contact():
    return render_template("/Medicine_Recommendation/frontend/contact.html")

@app.route('/developer')
def developer():
    return render_template("/Medicine_Recommendation/frontend/developer.html")

@app.route('/blog')
def blog():
    return render_template("/Medicine_Recommendation/frontend/blog.html")

if __name__ == '__main__':
    app.run(debug=True)