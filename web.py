import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

def model_prediction(test_image):
    try:
        model = tf.keras.models.load_model("trained_plant_disease_model.keras")
        st.write("Model loaded successfully")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

    try:
        image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])
        st.write("Image preprocessed successfully")
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

    try:
        predictions = model.predict(input_arr)
        st.write(f"Predictions: {predictions}")
        return np.argmax(predictions)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

st.sidebar.title("Plant Disease Detection System for Sustainable Agriculture")
app_mode = st.sidebar.selectbox('Select page', ['Home', 'Disease Recognition'])

img = Image.open('Diseases.png')
st.image(img)

if app_mode == 'Home':
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System for Sustainable Agriculture</h1>", unsafe_allow_html=True)
elif app_mode == 'Disease Recognition':
    st.header('Plant Disease Detection System For Sustainable Agriculture')

test_image = st.file_uploader('Choose an image:')
if test_image is not None:
    if st.button('Show Image'):
        st.image(test_image, use_column_width=True)
    if st.button('Predict'):
        st.snow()
        st.write('Our prediction')
        result_index = model_prediction(test_image)
        if result_index is not None:
            class_name = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
            st.success(f'Model is predicting it\'s a {class_name[result_index]}')
        else:
            st.error("Prediction failed. Please check the inputs and try again.")
else:
    st.write('Please upload an image file.')
