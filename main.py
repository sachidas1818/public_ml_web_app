import pickle
import streamlit as st
from streamlit_option_menu import option_menu

with open( "app\style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# # import warnings filter
# from warnings import simplefilter
# # ignore all future warnings
# simplefilter(action='ignore', category=FutureWarning)

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
kstone_model = pickle.load(open('kstone_model.sav', 'rb'))
lung_model = pickle.load(open('lung_model.sav', 'rb'))
breast_model = pickle.load(open('breast_cancer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Kidney Stone Prediction',
                           'Lung Cancer Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person','app','asterisk','app-indicator'],
                          default_index=0)




# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐏𝐫𝐞𝐠𝐧𝐚𝐧𝐜𝐢𝐞𝐬')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)




# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



# Kidney Stone Prediction Page
if (selected == 'Kidney Stone Prediction'):
    
    # page title
    st.title('Kidney Stone Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gravity = st.text_input('Gravity')
        
    with col2:
        ph = st.text_input('PH')
    
    with col3:
        osmo = st.text_input('OSMO')
    
    with col1:
        cond = st.text_input('COND')
    
    with col2:
        urea = st.text_input('UREA')
    
    with col3:
        calc = st.text_input('CALC')
    
    
    
    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("kidney stone Test Result"):
        kidney_prediction = kstone_model.predict([[gravity, ph, osmo, cond, urea, calc]])                          
        
        if (kidney_prediction[0] == 0):
          kidney_diagnosis = "The person does not have Kidney Stone disease"
        else:
          kidney_diagnosis = "The person has Kidney Stone disease "
        
    st.success(kidney_diagnosis)
    
    
# Diabetes Prediction Page
if (selected == 'Lung Cancer Prediction'):
    
    # page title
    st.title('Lung Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        AGE = st.text_input('Age of the patient')
        
    with col2:
        SMOKING = st.text_input('Smoking: YES=2 , NO=1')
    
    with col3:
        YELLOW_FINGERS = st.text_input('Yellow fingers: YES=2 , NO=1')
    
    with col1:
        ANXIETY = st.text_input('Anxiety: YES=2 , NO=1')
    
    with col2:
        PEER_PRESSURE = st.text_input('Peer_pressure: YES=2 , NO=1')
    
    with col3:
        CHRONIC_DISEASE = st.text_input('Chronic Disease: YES=2 , NO=1')
    
    with col1:
        FATIGUE = st.text_input('Fatigue: YES=2 , NO=1')
    
    with col2:
        ALLERGY = st.text_input('Allergy: YES=2 , NO=1')

    with col3:
        WHEEZING = st.text_input('Wheezing: YES=2 , NO=1')

    with col1:
        ALCOHOL_CONSUMING = st.text_input('Consume Alcohol: YES=2 , NO=1')
    
    with col2:
        COUGHING = st.text_input('Coughing: YES=2 , NO=1')

    with col3:
        SHORTNESS_OF_BREATH = st.text_input('Shortness of Breath: YES=2 , NO=1')

    with col1:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing Difficulty: YES=2 , NO=1')
    
    with col2:
        CHEST_PAIN = st.text_input('Chest pain: YES=2 , NO=1')

    
    # code for Prediction
    lung_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Lung Cancer Test Result'):
        lung_prediction = lung_model.predict([[AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        
        if (lung_prediction[0] == 1):
          lung_diagnosis = 'The person has lung cancer'
        else:
          lung_diagnosis = 'The Person does not have lung Cancer'
        
    st.success(lung_diagnosis)




#breast cancer


# breast cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        mean_radius = st.text_input('Mean_radius: mean of distances from center to points on the perimeter')
        
    with col2:
        mean_texture = st.text_input('Mean_texture: standard deviation of gray-scale values')
    
    with col1:
        mean_perimeter = st.text_input('Mean_perimeter: mean size of the core tumor')
    
    with col2:
        mean_area = st.text_input('Mean_area: mean area of the core tumor')
    
    with col1:
        mean_smoothness = st.text_input('Mean_smoothness: mean of local variation in radius lengths')
    
    
    
    # code for Prediction
    breast_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        Breast_Cancer_prediction = breast_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
        
        if (Breast_Cancer_prediction[0] == 1):
          breast_diagnosis = 'The person has breast cancer'
        else:
          breast_diagnosis = 'The Person does not have breast Cancer'
        
    st.success(breast_diagnosis)  
