import streamlit as st
import numpy as np
import pandas as pd
import pickle
import visualization

st.title("Penguin Prediction App")
st.write("This app predicts the **Palmer Penguin** species")

# side bar
st.sidebar.header("User Input Features")
uploaded_file = st.sidebar.file_uploader("Upload your csv file", type=['csv'])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else: 
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Torgersen','Biscoe','Dream'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Culmen Length (mm)', 32.1, 59.6, 43.9)
        bill_depth_mm = st.sidebar.slider('Culmen Depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)' , 2700.0, 6300.0, 4207.0)
        
        sex = 0 if sex =='male' else 1
        if island == 'Torgersen':
            island = 0
        elif island == 'Biscoe':
            island = 1
        else:
            island = 2
        
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return data, features

# tab
tab1, tab2 = st.tabs(["Visualization", "Prediction"])

with tab1:
    visualization.viz()
    
with tab2:
    # Load user input data
    data, features = user_input_features()
    st.subheader("User Input Parameters")
    st.write(data)
    
    features = np.array(features)
    st.write(features)
    
    # Predict
    st.subheader("Probability of Classes")
    model = pickle.load(open('model.pickle', 'rb'))
    res = model.predict(features)
    st.write(res)
    
    st.subheader("Model's Prediction")
    y_transfer = np.argmax(res, axis = 1)
    species = ['Adelie', 'Chinstrap', 'Gentoo']
    index = y_transfer[0]
    st.write(species[index])
    