import sqlite3
#from storage import *
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def stats(name):
    conn=sqlite3.connect("STUDENT_RECORDS.db")
    cursor=conn.cursor()
    #creating table related to attendance table
    #cursor.execute("CREATE TABLE Monthly_Stats(Name varchar(80),January int(2), Febreuary int(2), March int(2), April int(2), May int(2))")
    #table created
    #inserting data into table for previous months
    #cursor.execute("INSERT INTO Monthly_Stats VALUES('ANUSKA RAY_S1',28,27,31,24,0)")
    #cursor.execute("INSERT INTO Monthly_Stats VALUES('NACHIKETA_S2',30,26,30,28,0)")
    #cursor.execute("INSERT INTO Monthly_Stats VALUES('NIRNIMES_S3',27,27,30,26,0)")
    #cursor.execute("INSERT INTO Monthly_Stats VALUES('SHIVANI RAKESH_S4',31,28,29,27,0)")
    #cursor.execute("INSERT INTO Monthly_Stats VALUES('TAHA HUSSAIN_S5',29,28,31,27,0)")

    #increasing the monthly stat attendance count
    count=0
    cursor.execute("UPDATE Monthly_Stats SET May=? WHERE Name=?",(count+1,name))

    #printing the monthly stats of person in front of camera
    cmd="SELECT * FROM Monthly_Stats WHERE Name=?"
    alldata=cursor.execute(cmd,(name,))
    
    st.write ('''Your monthly statistics(Days of presence in each month are as follows) are as follows:
    ''')
    for row in alldata:
        st.info('''Student Name, January, February, March, April, May
        ''')
        st.info(row)
        months=[' ','January','February','March','April','May']
        fig = go.Figure(
        go.Pie(
        labels = months,
        values = row,
        hoverinfo = "label+percent",
        textinfo = "value"
        ))
        st.plotly_chart(fig)    
    conn.commit()
    conn.close()


    


