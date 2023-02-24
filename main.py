import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from markdownlit import mdlit

st.set_page_config(layout="wide")
image = Image.open('images/mypict.png')
img1 = Image.open('images/SKILLS.PNG')
img2 = Image.open('images/skills.gif')
    
with st.sidebar:
    st.title("Other Info")
    embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="-sandeep-joshi" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/-sandeep-joshi?trk=profile-badge">Sandeep Joshi</a></div>
              """}
    components.html(embed_component['linkedin'],height=310)
    
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("<h2 style='text-align: center; color: Grey;'>Hi! I am</h2>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Cursive;font-size:400%;text-align: center; color: Black;text-shadow: 0 0 10px #ccffcc, 0 0 20px #ccffd9, 0 0 30px #ccffe6, 0 0 40px #ccfff2;'>Sandeep Joshi</p></b>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center;color: Grey;'>Inquisitive and motivated individual, agog to learn, experience and create something new. I have found that nothing satisfies me more than meeting new people, developing new relationships, solving problems and contributing to the overall growth of a business. Sports and travel enthusiast who loves to play, partake in outdoor activities and find new adventures along the way.</p>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Cursive;font-weight: bold;font-size:220%;text-align: center; color: #262626;text-shadow: 0 0 10px #f2ffcc, 0 0 20px #ffffff;'>Work Experience</p></b>", unsafe_allow_html=True)
    st.markdown("<b><p style='font-family:Sans Serif;font-size:140%; color: Grey;'>ZS Associates</p></b>", unsafe_allow_html=True)
    st.caption("<p color: Grey;'>I have been working in ZS Associate since July 2021. During this period, I had learned a lot through various projects. Projects I had worked on are listed below: </p><p style='font-family:Sans Serif;font-size:100%; color: Grey;'><b>Incentive Compensation Design Project</p></b>", unsafe_allow_html=True)
    st.caption("<h6 color: Grey;'>o Assessed the program’s alignment with strategic objectives through stakeholder interviews and sales force surveys. <br>o Analyzed the program for fairness, pay for performance, biases and fiscal responsibility<br>o Benchmarked the design and performance against key industry standards (e.g. plan type, metrics, leverage, mix)<br>o Synthesized results to create actionable insights to enhance sales compensation program performance</p>", unsafe_allow_html=True)
    st.caption("<p style='font-family:Sans Serif;font-size:100%; color: Grey;'><b>Field Suggestion Project</p></b>", unsafe_allow_html=True)
    st.caption("<h6 color: Grey;'>o Understanding requirements and brainstorming suggestions to be sent out to sales representative for greater impact and value generation <br>o Setting up business rules by connecting with different teams and client<br>o Understanding, cleaning, and analyzing large datasets (>4GB)<br>o Establishing thresholds based on the analysis to determine when a particular suggestion should be acted upon<br>o Conducting quality checks and approving deliverables</p>", unsafe_allow_html=True)

with st.expander("My Skills"):    
    st.image(img1,use_column_width = 'always')
    
with st.expander("Certification"):

    # Define the data for the table
    table_data = ["Data Analysis with Python", "SQL for Data Science", "Excel Skills for Business: Advanced","Intro to Machine Learning", "Python", "Getting Started with Power BI Desktop"]
    image_data = ["Data analysis.PNG", "SQL.PNG", "Excel.jpg","ML.png","python.png","powerBI.png"]
    link_to_validate_certificates = ["https://jovian.ml/verify/MFQTGMZSGY","https://www.coursera.org/account/accomplishments/certificate/V6X7VHAGW9XC","https://coursera.org/verify/Y27EFKLVVHBD","","https://www.hackerrank.com/certificates/a1ac93b320b7","www.coursera.org/account/accomplishments/certificate/C682J53VXQ6H"]


    # Define the clickable headings with images
    for i in range(6):
        l = []
        l.append(st.button(f"{table_data[i]}\n\n![image_data[i]](link_to_validate_certificates[i])"))
    #cell_1_content = st.button("Click me!\n\n![Image 1](https://via.placeholder.com/150)")

    # Create the table
    st.table([l])

        
