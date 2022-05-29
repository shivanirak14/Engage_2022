<h1> Attendance Tracking System using Face Recognition Technology </h1>

This a web based application built as a project for Microsoft Engage 2022.

Demo Video: 

<h1>Problem Statement</h1>
The problem statement for this project involves recording attendance of a student with the help of a web application that takes the live image of a person as an input.

<h1>Project Description</h1>
A web based application that activates a webcam in order to take user’s face as input and:<br>
  (i)displays the name of person whose attendance is being recorded through webcam.<br>
  (ii)stores this name in a database that contains the Attendance Records.<br>
  (iii)displays monthly statistics of Attendance recorded of the user.<br>
  (iv)displays Attendance analysis of all the students based on the data recorded <br>

<h1>Tools, Libraries and Packages</h1>
<h3>Tools:</h3>
<ul>
 <li>Visual Studio Code</li>
<li>Chrome Browser</li></ul>
<h3>Programming Language,Libraries and Packages:</h3>
<ul>
  <li>Python</li>
<li>Streamlit</li>
<li>OpenCV</li>
<li>Python’s Face Recognition package</li>
<li>Pandas</li>
<li>SQLite3</li>
<li>Plotly</li></ul>

<h1>Project Structure and Composition</h1>
The entire project is based on the dataset which is stored in the "images" folder.

The code of the project is divided into the following files:<p>
<ol type=1>  
  <li><b>"main.py"</b> :This is the main page of the web application and can be executed using the command "streamlit run main.py". This leads to the main page of the web application.
             <p>It imports functions from the following file:
               <ol type=a>
               <li>face_rec_web.py= the file that contains the code to recognise user's face and record attendance.</li></ol><br>
  </li>                
  <li><b>"face_rec_web.py"</b> : This file contains the code to recognise and record user's data. In order to store and display the user's data, this program imports functions from the following two files:
  <p> a)storage.py b)show_stats.py</li>
                      
  <li><b>"storage.py"</b>: This file contains the code to store user attendance data into a sql table called "Attendance" which is stored in the database "Student_records".</li>

  <li><b>"show_stats.py"</b>: This file contains the code to update the monthly stats of the user whose data is being recorded by the web app. The data is updated in a sql table "Monthly_stats"(stored in "Student_records" Database.
                   This file also contains the code to extract user data from the sql table and depict monthly statistics of the user as a pie chart.</li>

  <li><b>"stats.csv"</b>: This file contains data prepared from the "Monthly_stats" table and is used to display overall attendance statistics.</li></ol>

 <h1> Instructions to run on local machine </h1>                    
 <ul>
 <li> Ensure dlib and cmake are installed before installing Face_Recognition package on your machine.<br> Visit the following link to successfully download and           install dlib and cmake : https://www.geeksforgeeks.org/how-to-install-face-recognition-in-python-on-windows/ <br>
      For Pyhton 3.9 and above: the whl file for dlib has been provided in the repository.    
  </li>
  <li> Ensure that all the required tools and packages,as mentioned in the requirements file are downloaded and installed on your machine.
    <br>Go to the directory where the files are stored and use the following command in the command prompt to install all the requirements: pip install -r requirements.txt
  </li>
  <li> Use the following command in the command prompt : streamlit run main.py</li>
  </ul>
<h1>Note:</h1>
<ul>
 
