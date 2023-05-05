import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pickle

#LOAD ASSETS-----------------------------------
img_home = Image.open("images/My Project.png")
diabetes_model = pickle.load(open('C:/Users/nihal/saved models/diabetes_model.sav', 'rb'))


st.set_page_config(layout='wide')

with st.container():
    st.title("Disease prediction")

with st.container():
    st.write("------")

selected = option_menu(
    menu_title = None,
    options = ["Home","BMI Calculator","Diseases"],
    orientation = "horizontal"
)

if selected == "Home":
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.title("")
        st.image(img_home)
    with text_column:
        st.subheader("Abstract")
        st.write('''Our point is to anticipate the various sorts of illness in a single stage by utilizing the inbuilt python module.To implement multiple disease analysis using machine learning algorithms, Streamlit and python
pickling is utilized to save the model behavior. In this article we analyze Diabetes analysis, Heart disease and Parkinson’s
disease by using some of the basic parameters such as Pulse Rate, Cholesterol, Blood Pressure, Heart Rate, etc., and
also the risk factors associated with the disease can be found using prediction model with good accuracy and Precision.
Further we can include other kinds of chronic diseases, skin diseases and many others. The significance of this analysis is to analyze the
maximum diseases to screen the patient's condition and caution the patients ahead of time to diminish mortality
proportion. We have considered three diseases for now that are Heart, Liver, and Diabetes and in the future, many more diseases can be added.This project can help a lot of people as one can monitor the persons’ condition and take the necessary precautions
thus increasing the life expectancy.''')


if selected == "BMI Calculator":
    st.title("Welcome to BMI Calculator")
    st.write(''' BMI is a useful measure of overweight and obesity. It is calculated from your height and weight. BMI is an estimate of body fat and a good gauge of your risk for diseases that can occur with more body fat. The higher your BMI, the higher your risk for certain diseases such as heart disease, high blood pressure, type 2 diabetes, gallstones, breathing problems, and certain cancers. ''')
    
    weight = st.number_input("Enter your weight (in kgs)")
    status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
    if(status == 'cms'):
    # take height input in centimeters
        height = st.number_input('Centimeters')
 
        try:
            bmi = weight / ((height/100)**2)
        except:
            st.text("Enter some value of height")

    elif(status == 'meters'):
    # take height input in meters
        height = st.number_input('Meters')
 
        try:
            bmi = weight / (height ** 2)
        except:
            st.text("Enter some value of height")
    
    else:
    # take height input in feet
        height = st.number_input('Feet')
 
    # 1 meter = 3.28
        try:
            bmi = weight / (((height/3.28))**2)
        except:
            st.text("Enter some value of height")
    
    if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
        st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
        if(bmi < 16):
            st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif(bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif(bmi >= 30):
            st.error("Extremely Overweight")

if selected == "Diseases":
    st.title("Welcome To Disease Predictor")

    with st.sidebar:
        select = option_menu(
            menu_title="Main Menu",options=["Diabetes","Heart","pakinsons"]
        )
    
    if select == "Heart":
        st.subheader("hello")
    
    if select == "Diabetes":
        col1,col2,col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        
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
        
        diab_diagnosis = ''

        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        
        st.success(diab_diagnosis)

