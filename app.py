import streamlit as st
from PIL import Image

with open('style.css') as f :
    st.markdown('<style>{}</style>'.format(f.read()) , unsafe_allow_html = True)

#header


st.write('''
# Amit Kumar Jaiswal, Ph.D.
##### *Resume* 
''')

image = Image.open('profile-pic.png')
st.image(image , width = 300 ,)

st.markdown('## Summary' , unsafe_allow_html = True)

st.info('''
- A Data scientist / Data Analyst with self experienced skilled demostrated by several self projects.
- I have worked on many self projects like data cleaning , data preprocessing , feature handling , model building / model utilizing.
- strong EDA analysis with finding outliers and fixing it.
- Strong verbal and communation skills as demonstrated by presentation of different task and works.

''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Amit Kumar Jaiswal <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#self-projects">Self Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#research-papers-published">Research Papers Published</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#communication-skills">Communication Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contacts">Contact Me</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

def txt1(a , b) :
    col1 , col2 = st.columns([4 , 1])

    with col1 :
        st.markdown(a)

    with col2 :
        st.markdown(b)

def txt2(a , b) :
    col1 , col2 = st.columns([4 , 1])

    with col1 :
        st.markdown(a)

    with col2 :
        st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt4(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt5(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt6(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt7(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

st.markdown('''**Doctor of Philosophy** (Cyber Security with Data Science), *Moscow Institute of Physics and Technology* , Moscow , Russia ,
2023-2026''')
st.markdown('''
- Currently pursuing
- Research thesis entitled `Models and methods of artificial intelligence for a monitoring cluster for identifying and preventing cyber attacks`.
- Received Russian Government Ph.D. Scholarship covering tuition and stipend.
''')

st.markdown('''**Master of Science** (Cyber Security with Data Science), *Moscow Institute of Physics and Technology* , Moscow , Russia ,
2021-2023''')
st.markdown('''
- GPA: `5/5`
- Graduated with First Class Honors.
- Received Russian Government Ph.D. Scholarship covering of ('1 million rubles') as tuition and stipend.
''')

st.markdown('''**Bachelors of Science** (Computer Science), *Lovely Professional University*, India',
'2015-2018''')
st.markdown('''
- GPA: `4/5`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

st.markdown('''
- JUNIOR DATA ANALYST, WORK FROM HOME `(2021 - PRESENT) – FREELANCING–`
● Developed and implemented machine learning models to predict datasets, resulting in an
analysis and predictions.
● Created interactive dashboards and reports to visualize key business metrics, leading to
improved decision-making.
● Performed data analysis and cleaning for market research studies, contributing to
successful product launches.
● Utilized Python (Pandas, NumPy, Scikit-learn) and SQL for data manipulation and analysis.
''')


#####################
st.markdown('''
## Skills
''')

st.markdown('''
- Database Tools : `SQL (SQL Server, MySQL) , Mongodb`
- Data Science / Data Analysis Libraries : `Python (Pandas, NumPy, MatPlotLib, seaborn, scikit-learn , pytorch)`
- Machine learning algorithms : `Logistic Regression , Linear regression, KNN , Random Forest , Decision Tree , Naive Bayesian etc`
- Unix based OS and Tools : `Linux, kali Linux, bash scripting, vs code, git desktop, github, streamlit`
- Data Science / Data Analysis Tools : `Anaconda , Jupiter notebook , web scraping`
- Web Scrapping Tools : `BeautifulSoup , prompt engineering (gradient AI)`
- Cyber Security Skills : `Wireshark Monitoring , Network Scanning , Bug Analysis , `
- Micilleneous Skills : `Powerpoint Presentation , Latex (Research paper building), Microsoft Exel , Microsoft word`
''')

st.markdown('''
## Self Projects
''')

st.markdown('''
- I R I S &nbsp; F L O W E R &nbsp; C L A S S I F I C A T I O N &nbsp; U S I N G  &nbsp; M A C H I N E  &nbsp; L E A R N I N G – `Personal Project – K A G G L E D A T A S E T S` 
● Used a logistic regression model to classify Iris flowers into three species (Setosa,
Versicolor, Virginica) based on petal and sepal measurements. Utilized various techniques
including data cleaning, feature engineering, and model selection. Achieved an accuracy of 95%
with the chosen model. 
● Collected and preprocessed Iris flower dataset.
● Performed `exploratory data analysis` and visualized key features. 
● Aggregated and visualized the data by using `pandas, matplotlib and seaborn` to compile a professional report.
● Used Machine Leraning classification models (`Logistic Regression , Decision Tree Classifier , Random Forest Classifier`)

- C U S T O M E R &nbsp; S A L E S &nbsp; C L A S S I F I C A T I O N – `Virtual Client’s Project – I N D I A , New Delhi February 2022`
● Collected and cleaned customer sales data, handling missing values and inconsistencies.
● Performed exploratory data analysis, identifying key features and patterns in customer behavior
● Predicted customer purchase behavior and classify them into high-value, medium-value, and low-value categories based on historical sales data and customer attributes.
● Informed client about fluctuation in customer sales behavior.
● Consulted the client on future outcomes and possiblity.

- W E B S C R A P I N G &nbsp; A N D &nbsp; D A T A &nbsp; C L E A N I N G &nbsp; P R O C E S S – `Personal Project , December 2021`
● Choosen the website and specific data I wanted to extract.
● Depending on the website complexity, I have used tools like:
● Browser Extensions: Simple scraping for beginner-friendly websites.
● Parsing and Structuring: Converted the extracted data into a readable and consistent
format. These tasks involved parsing text, handling missing values, and standardizing units.
● Duplication Removal: Identify and remove duplicate entries to ensure data integrity.
● Error Correction: Fix any errors like typos, inconsistencies, or invalid values.
● Check if the cleaned data meets my intended use and analysis requirements.
''')



st.markdown('''
## Research Papers Published
''')

st.markdown('''
- DOS attack Network Traffic Monitoring in Software Defined Networking using Mininet and RYU Controller.
`Dec 2022`

https://doi.org/10.21203/rs.3.rs-2282189/v1

- APACHE LOG4J SHELL VULNERABILITY ANALYSIS. `Oct 2022`

https://doi.org/10.33564/IJEAST.2022.v07i06.047



''')




st.markdown('''
## Communication Skills
''')

st.markdown('''
- English - `C2 level professional and proficient`
- Russian - `A2 level conversational`
- Hindi - `Native language`
''')



st.markdown('''
## Social Media
''')
st.markdown('''LinkedIn : www.linkedin.com/in/amit-jaiswal-5bbb59156''')
st.markdown('''GitHub : https://github.com/Amit-Kumar-Jaiswal/''')

st.markdown('''
## Contacts
''')
st.markdown('''
- Home : `Pervomayskaya line, 32 korpus 3, 141701, Dolgoprudney, Russia`
- Gender: `Male `
- Date of birth: `09/09/1995`
- Nationality: `Indian`''')
st.markdown('''Email: `amitjaiswallpu@yahoo.in`''' )
st.markdown('''Phone: `(+7) 9850133375`''' )
 
