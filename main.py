from pickle import NONE
import cv2 #for image processsing
import numpy as np
import face_recognition
import os #for loading images
import streamlit as st
from face_rec_web import *
from show_stats import *
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px




st.set_page_config(page_title="Student Records")

choice = st.sidebar.selectbox("Choose your preferred action:",("Record Your Attendance", "View Attendance Analysis","---Select an option---"),index=2)
if choice=="---Select an option---":
    st.title("Welcome to Student Records")
    st.write("""Greetings for the day!
 
 
 Kindly select your preferred action by heading to the side panel of this page. 
 
 Thanks for using our site. Have a good day! """)
elif choice=="Record Your Attendance":
    record_attendance()
elif choice=="View Attendance Analysis":
    st.title("Attendance Analysis")
    st.warning('''Attention to the viewer:
    The analysis is based on records calculated upto the last month with respect to the month in which this data is viewed!''')
    df=pd.read_csv('stats.csv')
    fig=px.bar(df,x="Average No. of Days Students Were Present",y="Month",title="Attendance Analysis")
    st.plotly_chart(fig)
    
        