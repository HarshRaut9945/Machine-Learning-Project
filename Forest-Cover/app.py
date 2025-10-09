import streamlit as st
import numpy as np
import pandas as pd
import pickle 
from  PIL import Image

#loading trained model
rfc= pickle.load(open('Notebook and dataset/rfc.pkl','rb'))


# creating web app

st.title("forest cover Tupe Prediction")
image=Image.open('./img/img.png')
st.image(image,caption='myimage',use_column_width=True)

user_input=st.text_input('Enter all cover type Features')

if user_input:
    user_input=user_input.split(',')
    features=np.array([user_input],dtype=np.float64)
    prediction =rfc.predict(features).reshape(1,-1)
    prediction=  int(prediction[0])
    st.write(prediction)

    cover_type_dict={
      1:{"name":"Spruce/fir", "image":"./img/img_2.png"},
      2:{"name":"Lodgepole Pine", "image":"./img/img_2.png"},
      3:{"name":"Ponderosa Pine", "image":"./img/img_3.png"},
      4:{"name":"Cottonwood/Willow", "image":"./img/img_2.png"},
      5:{"name":"Aspen/fir", "image":"./img/img_3.png"},
      6:{"name":"Douglas-fir", "image":"./img/img_6.png"},
      7:{"name":"Krummholz", "image":"./img/img_7.png"}
   }
     
    cover_type_info= cover_type_dict.get(prediction)

    if   cover_type_info is not None:
        forest_name=cover_type_info['name']
        forest_image=cover_type_info['image']

        col1,col2=st.columns([2,3])
        with col1:
            st.write('this is predicted cover type')
            st.write(f"<h1 style='font-size:50px; font-weight:bold;'>{forest_name}</h1>",unsafe_allow_html=True)

        with col2:
            final_image=Image.open(forest_image)
            st.image(final_image,caption=forest_name,use_column_width=True)