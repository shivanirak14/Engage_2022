import sqlite3
from datetime import datetime
import streamlit as st
from show_stats import *

def store_attendance(name): 
    conn=sqlite3.connect("STUDENT_RECORDS.db")
    cursor=conn.cursor()
    #creating the table first
    #table="""Create table Attendance(Name varchar(80), Time time);"""
    #cursor.execute(table)
    #delete=cursor.execute('''DELETE FROM attendance''')
    #data=cursor.execute('''SELECT Name FROM Attendance ''')
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    cursor.execute("Insert into attendance \
    select * from( Select ?,?) as temp \
    where not exists \
    (Select Name from attendance where Name=?) LIMIT 1",(name,current_time,name)) #to avoid data redundancy
    alldata=cursor.execute('''SELECT* FROM Attendance''')    #printing data into console
    for row in alldata:
            print(row)
    st.write("Your attendance has been recorded.Data recorded is: Name:", name)        
    conn.commit()
    conn.close()

    
  



