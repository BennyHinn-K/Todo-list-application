import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="BennyHinn Portfolio",page_icon="B logo.png",layout="wide")


#  header section
with st.container():
    st.subheader("Hello, I am BennyHinn. :wave:")
    st.title("I am a web Developer from Kenya")
    st.write("I am passionate about solving problems and creating effective work using python")
    st.write("[Learn more->](http://bennyhinn-kariuki.kesug.com/index.html?i=1)")

    
# loading function 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl(url="https://lottie.host/fb849e9b-6c12-4206-bb99-1d542be14f85/7AlBniudLt.json")

 


#  what I do 
st. write("---") 
st.subheader("What I Do :")
with st.container():
    left_columnn, right_column = st.columns(2)
    with left_columnn:
        st.write(''' As a seasoned professional in the Streamlit framework and Python programming, I have honed my expertise in developing interactive, data-driven applications that streamline complex workflows and enhance user engagement. My extensive experience with Streamlit enables me to design and deploy intuitive dashboards and real-time data visualizations with ease, leveraging Python’s robust libraries to create scalable solutions. I excel in integrating diverse data sources, optimizing performance, and implementing advanced features that transform raw data into actionable insights. My commitment to best practices and continuous learning ensures that my projects not only meet but exceed industry standards, delivering high-quality, user-centric applications that drive informed decision-making and operational efficiency.''')
  
    with right_column:
        st_lottie(lottie_coding,height=300,key="Coding")



# projects 
with st.container():
    st.write("---")
    st.header("Projects participated ")
    st.write("##")
  
    image_column, text_column = st.columns((0.5,2))

    with image_column:
        st.image("Ai.png",width= 150)
        st.image("B logo.png",width= 150)

       
        
    with text_column:
        st.subheader("T-Antiques.")
        st.write("The app aids the users to be able to buy and sell goods of antique nature.")
        import streamlit.components.v1 as stc

        st.link_button("Visit Here ",url="https://github.com/Benkariuki/PROJECT-ANTIQUES.git")


        st.subheader("My Portfolio")
        st.write("This website is a axiom of my portfoilo,a sublime embodiment of who I am and the skills gagnered.")
       
        import streamlit.components.v1 as stc

        st.link_button("Visit Here ",url="http://bennyhinn-kariuki.kesug.com/index.html?i=2")



st.header("Contact Me :")

st.write("---")


with st.container():
    with st.form(key="Complete"):
        st.header("Kindly the contact list below.")

        st.text_input ("Enter your name:")
        st.text_input ("Enter your Email:")
        st.number_input ("Enter your Contacts:",min_value=+254000000000)
        st.number_input ("Enter your age:", max_value=40, min_value= 5)

        st.form_submit_button("Submit")


