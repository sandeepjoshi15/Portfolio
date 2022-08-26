import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
image = Image.open('images/mypict.png')
img1 = Image.open('images/SKILLS.PNG')
img2 = Image.open('images/skills.gif')
    
with st.sidebar:
    st.title("Other Info")
    embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="sandeep-joshi-271509161" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/sandeep-joshi-271509161?trk=profile-badge"></a></div>"""}
    components.html(embed_component['linkedin'],height=310)
    
col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("<h2 style='text-align: center; color: Grey;'>Hi! I am</h2>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Cursive;font-size:400%;text-align: center; color: Black;text-shadow: 0 0 10px #ccffcc, 0 0 20px #ccffd9, 0 0 30px #ccffe6, 0 0 40px #ccfff2;'>Sandeep Joshi</p></b>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center;color: Grey;'>Inquisitive and motivated individual, agog to learn, experience and create something new. I have found that nothing satisfies me more than meeting new people, developing new relationships, solving problems and contributing to the overall growth of a business. Sports and travel enthusiast who loves to play, partake in outdoor activities and find new adventures along the way.</p>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Cursive;font-size:200%;text-align: center; color: #262626;text-shadow: 0 0 10px #f2ffcc;'>Work Experience</p></b>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Sans Serif;font-size:140%; color: Grey;'>ZS Associates</p></b>", unsafe_allow_html=True)
    st.caption("<p color: Grey;'>I have been working in ZS Associate since July 2021. During this period, I had learned a lot through various projects. Projects I had worked on are listed below: </p><p style='font-family:Sans Serif;font-size:100%; color: Grey;'><b>Incentive Compensation Design Project</p></b>", unsafe_allow_html=True)
    st.caption("<h6 color: Grey;'>o Assessed the program’s alignment with strategic objectives through stakeholder interviews and sales force surveys. <br>o Analyzed the program for fairness, pay for performance, biases and fiscal responsibility<br>o Benchmarked the design and performance against key industry standards (e.g. plan type, metrics, leverage, mix)<br>o Synthesized results to create actionable insights to enhance sales compensation program performance</p>", unsafe_allow_html=True)

with st.expander("My Skills"):    
    st.image(img1,use_column_width = 'always')
    
with st.expander("Certification"):
    cola, colb, colc = st.columns(3)
    cola.subheader("Data Analysis with Python")
    cola.write("Jovian")
    cola.image("images/Data analysis.PNG")
    colb.subheader("SQL for Data Science")
    colb.subheader("")
    colb.write("Coursera")
    colb.image("images/SQL.PNG")
    colc.subheader("Excel Skills for Business: Advanced")
    colc.write("Coursera")
    colc.image("images/Excel.jpg")
    cola.subheader("Intro to Machine Learning")
    cola.write("Kaggle")
    cola.image("images/ML.png")
    colb.subheader("Python")
    colb.subheader("")
    colb.write("Hackerrank")
    colb.image("images/python.png")
    colc.subheader("Getting Started with Power BI Desktop")
    colc.write("Coursera")
    colc.image("images/powerBI.PNG")
    
with col2:
    st.image(image, use_column_width = 'always')
