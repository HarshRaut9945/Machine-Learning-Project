import streamlit as st
import pandas as pd



st.sidebar.title("upload dataset")

upload_file=st.sidebar.file_uploader("choose Csv file",type='csv')

if upload_file is not None:
    df=pd.read_csv(upload_file)

    #Sidebar code
    no_event=len(df)
    citizenship_counts = df['citizenship'].value_counts()
    event_location_region = df['event_location_region'].value_counts()
    hostilities_counts = df[df['took_part_in_the_hostilities'] == 'Yes']['citizenship'].value_counts()
    no_hostilities_counts = df[df['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()

    st.sidebar.write("No of Event :",no_event)

    col1,col2,col3,col4=st.sidebar.columns(4)

    with col1:
        st.sidebar.subheader("citizenship_counts")
        st.sidebar.write(citizenship_counts)
    with col2:
        st.sidebar.subheader("event_location_region")
        st.sidebar.write(event_location_region)
    with col3:
        st.sidebar.subheader("hostilities_counts")
        st.sidebar.write(hostilities_counts)
    with col4:
        st.sidebar.subheader(" no_hostilities_counts")
        st.sidebar.write( no_hostilities_counts)


    weapons_counts=df['ammunition'].value_counts()
    st.sidebar.write(weapons_counts)

    # Data analysis part