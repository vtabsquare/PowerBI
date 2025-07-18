import streamlit as st
import base64
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="VTAB Square Private Limited", layout="wide", page_icon="📊")

# ------------------ BACKGROUND IMAGE ------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;  /* Ensures the image scrolls with the page */
            background-position: top center;
        }}
        </style>
    """, unsafe_allow_html=True)


#___________hover__________
import streamlit as st

st.markdown("""
    <style>
    .card:hover {
        box-shadow: 0 0 12px #003399;
        transform: scale(1.02);
        transition: 0.3s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)




set_bg("bg.JPEG")# --------------------- Set Logo ---------------------
def get_logo_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_base64 = get_logo_base64("Logo.JPEG")  # Corrected filename

# --------------------- Convert Background Image to Base64 ---------------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Encode your bg.JPEG image
bg_base64 = get_base64("bg.JPEG")

# --------------------- Sidebar Styling & Layout ---------------------
st.markdown(f"""
    <style>
    .sidebar-container {{
        padding: 25px 20px;
        font-family: 'Segoe UI', sans-serif;
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), url("data:image/jpeg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        border-radius: 10px;
    }}

    .sidebar-logo {{
        text-align: center;
        margin-bottom: 25px;
        transition: transform 0.3s ease-in-out;
    }}

    .sidebar-logo img {{
        border-radius: 12px;
        max-width: 180px;
        width: 100%;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }}

    .sidebar-logo:hover img {{
        transform: scale(1.05);
    }}

    .sidebar-title {{
        font-weight: 600;
        font-size: 20px;
        color: #222;
        margin: 20px 0 15px 0;
        border-bottom: 1px solid #ccc;
        padding-bottom: 8px;
        text-align: center;
    }}

    .timeline {{
        list-style: none;
        padding-left: 0;
        margin-top: 10px;
    }}

    .timeline li {{
        margin-bottom: 14px;
        position: relative;
        padding: 10px 15px 10px 18px;
        border-left: 3px solid #3498db;
        border-radius: 6px;
        transition: all 0.3s ease;
        background-color: rgba(255, 255, 255, 0.65);
        cursor: pointer;
    }}

    .timeline li span {{
        font-weight: bold;
        color: #111;
    }}

    .timeline li:hover {{
        background-color: #e6f4ff;
        padding-left: 22px;
        border-left-color: #1d6fa5;
    }}
    </style>
""", unsafe_allow_html=True)

# --------------------- Sidebar Layout ---------------------
with st.sidebar:
    st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)

    if 'logo_base64' in globals():
        st.markdown(f"""
            <div class="sidebar-logo">
                <img src="data:image/png;base64,{logo_base64}" alt="Company Logo">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Logo not found!")

    st.markdown("""
        <div class="sidebar-title">Our Journey</div>
        <ul class="timeline">
            <li><span>2007</span> – Vision & Idea</li>
            <li><span>2010</span> – Embracing Technology</li>
            <li><span>2015</span> – Industry Experience</li>
            <li><span>2016</span> – Process Implementation</li>
            <li><span>2017</span> – Strategic Consulting</li>
            <li><span>2019</span> – Launch of VTAB SQUARE Pvt Ltd</li>
            <li><span>2020</span> – Operational Excellence</li>
        </ul>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
# ------------------ HEADER + INTRO ENHANCED ------------------
st.markdown("""
    <style>
    .intro-box {
        background: linear-gradient(90deg, #2980b9 0%, #6dd5fa 100%);
        color: white;
        padding: 40px 50px;
        border-radius: 12px;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        font-family: 'Segoe UI', sans-serif;
        animation: fadeIn 1s ease-in-out;
        margin-bottom: 30px;
    }

    .intro-box h1 {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .intro-box h3 {
        font-size: 20px;
        font-weight: 400;
        margin-bottom: 20px;
        color: #f0f0f0;
    }

    .intro-box p {
        font-size: 22px;
        line-height: 1.6;
        margin-bottom: 0;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>

    <div class="intro-box">
        <h1>VTAB Square Private Limited</h1>
        <h3>Empowering businesses through data and innovation</h3>
        <p>
            At <strong>VTAB SQUARE</strong>, we are a dynamic and emerging IT and services provider, dedicated to delivering excellence 
            in data quality, security, and business solutions. Backed by over <strong>18 years</strong> of our founder’s industry experience, 
            we have been operating since <strong>2019</strong> with a mission to drive business transformation. Our services are designed to enhance operational efficiency and streamline processes, enabling <strong>sustainable growth</strong> 
            and measurable results for our clients.
        </p>
    </div>
""", unsafe_allow_html=True)






#------------------ VISION + SOLUTIONS UI ------------------
st.markdown("""
<style>
.vision-container {
    padding: 40px 10px 30px 10px;
    font-family: 'Segoe UI', sans-serif;
}
.vision-container h2 {
    text-align: center;
    font-size: 32px;
    margin-bottom: 10px;
    color: #1e1e1e;
}
.vision-container p {
    font-size: 20px;
    text-align: center;
    margin-bottom: 25px;
    color: #333;
}
.solutions-icons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 10px;
}
.icon-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 12px 20px;
    font-size: 18px;
    color: #222;
    font-weight: 500;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}
.icon-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}
</style>

<div class="vision-container">
    <h2>Our Vision</h2>
    <p>
        To be a global leader in data-driven innovation, empowering organizations with transformative insights and intelligent automation.
    </p>

  
""", unsafe_allow_html=True)



# ------------------ DATA ANALYTICS SECTION ------------------
st.markdown("""
<style>
.analytics-section {
    padding: 50px 20px;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #f0faff, #e6f4ff);
    border-radius: 16px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.05);
    margin-top: 30px;
}

.analytics-section h2 {
    text-align: center;
    font-size: 32px;
    color: #0a0a0a;
    margin-bottom: 10px;
}

.analytics-section p {
    text-align: center;
    font-size: 20px;
    color: #333;
    margin-bottom: 30px;
}

.solutions-icons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 25px;
}

.icon-card {
    background-color: white;
    padding: 15px 25px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    font-size: 18px;
    font-weight: 500;
    color: #222;
    transition: 0.3s ease-in-out;
    min-width: 280px;
    text-align: center;
}

.icon-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.15);
    background-color: #f9fbfd;
}
</style>

<div class="analytics-section">
    <h2>Data Analytics & AI Solutions</h2>
    <p>
        Our services focus on integrating intelligent systems, automating insights, and enabling informed decision-making
    </p>
<div style='display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; font-size: 17px;'>
    <div style="font-family: sans-serif; font-size: 20px;">📊 Business Intelligence Dashboards</div>
    <div style="font-family: sans-serif; font-size: 20px;">📡 Real-Time Data Monitoring</div>
    <div style="font-family: sans-serif; font-size: 20px;">🧠 Machine Learning Models</div>
    <div style="font-family: sans-serif; font-size: 20px;">📈 Performance & KPI Tracking</div>
    <div style="font-family: sans-serif; font-size: 20px;">🔁 Automated Forecasting</div>
</div>
</div>
""", unsafe_allow_html=True)



st.markdown("---")






# ------------------ SESSION STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = "main"
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "selected_subtopic" not in st.session_state:
    st.session_state.selected_subtopic = None

# ------------------ TOPIC DATA ------------------
topics = {
    "Analytics": {
        "image": "Analytics.JPG",
        "desc":"Provides data-driven insights through interactive visuals, enabling informed decision-making and performance tracking.",
        "subtopics": [



{"name": "All Phases Report", "image": f"subimage/All Phases Report.JPG", "iframe":" https://app.powerbi.com/view?r=eyJrIjoiZTEyZDU2ZGYtMDgzMi00MTFkLWI5ZjMtNmRlODEyOGE5YmU5IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Application Analysis Dashboard", "image":  f"subimage/Application Analysis Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiZWFkMzU3MjctZWViMC00YWQyLTg0NTMtYjdhYTA1YWM0Y2I2IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Energy Consumption Analytics", "image":  f"subimage/Energy Consumption Analytics Dashboard.JPG","iframe": "https://app.powerbi.com/view?r=eyJrIjoiMmY5ODM0NzAtOTUxOC00ZmY2LWIxNjMtM2E0ZGJkODcyMTY1IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	{"name": "E Grow Analysis Dshboard", "image":  f"subimage/E Grow Analysis Dshboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiZDQ4ZDc2M2YtZWIwYS00M2Q2LWE3ZDYtNzYwNGU5NzY2NjQyIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	    {"name": "Food inspection", "image":  f"subimage/Food inspection.JPG","iframe": "https://app.powerbi.com/view?r=eyJrIjoiOTQwNTk4MTYtYzhhMS00MmNjLThlZTctMzhiM2NkNTllZmYxIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Energy Consumption Analytics Dashboard", "image": f"subimage/Energy Consumption Analytics Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiMmY5ODM0NzAtOTUxOC00ZmY2LWIxNjMtM2E0ZGJkODcyMTY1IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	{"name": "Final Quality Inspection", "image": f"subimage/Final Quality Inspection.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOWFiNDI3OGMtNGViZi00NTdjLWI1ZGItMWVhN2I2YjcwODM3IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	{"name": "Google Analytics Dashboard", "image": f"subimage/Google Analytics Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiYzJjOWQxYWItYTA4ZS00YWQ0LTkxZDgtYzljNmZiNTA0YzQ0IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	{"name": "HVA Dashboard Summary", "image":  f"subimage/HVA Dashboard Summary.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiN2YxYzYwMDYtNTJhMC00OTdlLWExOTEtMzg4YzUwOGEzOTkxIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
]
    },
   "Billing": {
        "image": "Billing.JPG",
        "desc":"Monitors invoicing, payment cycles, and outstanding balances. Improves billing accuracy and collection efficiency.",
        "subtopics": [
   
            {"name": "Billing Apllication Dashboard", "image":  f"subimage/Billing Apllication Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiZTcyODBkMjAtZGVlOC00Y2JhLWI4NjMtZmI5MDFiMWU2ZjZhIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]
    },

"Corporate Management": {
        "image": "Corporate.JPG",
        "desc":"Provides a high-level overview of KPIs, departmental performance, and strategic alignment.",
        "subtopics": [
            {"name": "HR Analytics Dashboard", "image":  f"subimage/HR Analytics Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiN2Q5YWI0YmMtZmI1NS00ZTljLWJiMjEtNzViYzc1OGE4MGViIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "HR Management Dashboard", "image": f"subimage/HR Management Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiODg4YWI4YTMtNjQxZi00NWMyLWFhZDItMWEwNWE0MTcwZmY2IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

 	 {"name": "Technical Analysis Report", "image":  f"subimage/Technical Analysis Report.JPG","iframe": "https://app.powerbi.com/view?r=eyJrIjoiY2Y5OWRjY2QtZjMzMS00YWJmLTg0Y2UtYmI3MmRlY2Y2NmE4IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]
    },


 "Educational": {
        "image": "Educational.JPG",
        "desc":"Tracks student performance, attendance, and course completion.Supports academic planning and institutional improvement",
        "subtopics": [
            {"name": "Attendance Dashboard", "image":  f"subimage/Attendance Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNzMwNDlmNmYtMDk5ZS00OGYyLTk5ZWQtYjkyNjdmNjUxYTMyIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "College Ranking Dashboard", "image":  f"subimage/College Ranking Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiMWFkM2ZiNWQtOGU4NS00MjY3LWExNTctOTUwYjQ2OWIzN2NkIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

	{"name": "Examination Schedule Dashboard", "image":  f"subimage/Examination Schedule Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiMWVkMmU1YTYtZTI1ZS00ODU0LTg2OWItYmJiNjA3M2I0ODgxIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

           {"name": "Graduation Analysis Report", "image":  f"subimage/Graduation Analysis Report.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNTQzNWI5ZWUtNWYxMy00OTgzLWI0MzQtMzViNDQwOTdkZGIzIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

     {"name": " Naac Report", "image":  f"subimage/Naac Report.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiYThjYThjMTktYzY1Ni00MGIyLTk4YTMtNDYwODU4YzY2ZDY2IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": " Malawi Educational Dashboard", "image":  f"subimage/Malawi Educational Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNjVlOWRkNzktODNiNC00YmMxLTllOTItY2ZhNDJlMzhmZmE4IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

   {"name": "Performance Analysis Dashboard", "image":  f"subimage/Performance Analysis Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiODZhNjZmZWMtOTRlYi00MjNiLThkMjktMjkwNWY4NDEwZTkyIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},
        ]
    },

"Cost Analytics": {
        "image": "Cost.JPG",
        "desc":"Breaks down operational costs, resource usage, and budget adherence Identifies cost-saving opportunities and financial inefficiencies.",
        "subtopics": [
            {"name": "Lead Conversion", "image":  f"subimage/Lead Conversion.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiZTcyODBkMjAtZGVlOC00Y2JhLWI4NjMtZmI5MDFiMWU2ZjZhIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
            
        ]
},

"Financial": {
        "image": "Financial.JPG",
        "desc":"Analyzes revenue, expenses, profit margins, and cash flow. Supports budgeting, forecasting, and strategic financial planning.",
        "subtopics": [
            {"name": "Competitor Analysis Dashboard", "image":  f"subimage/Competitor Analysis Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhMjlmNDctYTA3Ni00MzRhLTk4NWMtZGE3M2QwZWQyY2RlIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Credit Card Analysis Dashbooard", "image":  f"subimage/Credit Card Analysis Dashbooard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOTQ3ZWYxMjktZTlmYi00NzJlLThmODItM2U5MWVlM2NhNjdlIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

 {"name": "Customer Insight Analysis Dashboard", "image":  f"subimage/Customer Insight Analysis Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOGM5OGUyNzQtNjZlZC00Mjg2LWIyYmMtZmMyYTljZTZiZDMwIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Financial Performance Dashboard", "image":  f"subimage/Financial Performance Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiYWIzZjMzODgtODFhNC00MzcxLTk3M2MtYTZhNTM3Mjc1NGQyIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

 {"name": "Loan Details Analysis Dashboard", "image":  f"subimage/Loan Details Analysis Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNmNkZmZjZDYtYTE0Yy00Mjk1LWI0N2YtYWJiMjczYTNiMjkxIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Loan Portfolio Dashboard", "image": f"subimage/Loan Portfolio Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNWNmZGJjMTItN2QzNy00ZGZlLWEyYzEtM2Y4ODA4ODUyNzM0IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": "Loan Tracking Dashboard", "image":  f"subimage/Loan Tracking Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiMjQzNjdkNjQtNmM2ZS00NzJiLTk1OGYtMGI0YTU3YmNjNDE3IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Operational Efficienecy", "image":  f"subimage/Operational Efficienecy.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNDgyMzhhYmYtMjk0MS00ODhmLWFhNzEtYmViOWVmODVmMTdkIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": "Sustainability and ESG Dashboard ", "image":  f"subimage/Sustainability and ESG Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiMzAyYWE1MzctZjI0Zi00OGU3LThhZjUtNWY2Nzg2YmU5NTI3IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]

    },


"Helpdesk Analytics": {
        "image": "Helpdesk.JPG",
        "desc":"Monitors ticket volume, resolution time, and agent productivity. Improves customer support efficiency and identifies recurring issues.",
        "subtopics": [
            {"name": "Call Center Dashboard", "image":  f"subimage/Call Center Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOTVjMzQwYTctYWYwZC00N2U0LTkyOWUtNjVjMjg3OGQ5MjdjIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Customer Care", "image":  f"subimage/Customer Care.JPG", "iframe": "https://app.powerbi.com/reportEmbed?reportId=bd1aa9f4-9915-49bd-9cdd-4f0926f682bb&autoAuth=true&ctid=d96cb34e-74be-402e-83f8-b2d504c4bcfa"},

{"name": "Job Analysis Dashboard", "image": f"subimage/Job Analysis Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOGJiNTNlMzktZWEzMy00ZTYzLTk1OTItMWEzOGFmNTZiMjg0IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Phone Call Analysis Dashboard", "image": f"subimage/Phone Call Analysis Dashboard.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOWRhODZmNmUtZmZmNy00OWE5LWI1OTktYWFmODVlYzI4NzI0IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": "SLA Analysis Report", "image":  f"subimage/SLA Analysis Report.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiYzAwMjBlNGQtZDA4NC00Nzc5LTgyODYtMDMyNmNlNzU1N2Y0IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "TAT Report ", "image":  f"subimage/TAT Report.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOGY0N2YyNjAtZjQxZC00MTgwLTliYTAtYmFkYTVjZDA3YjQ2IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]

    },
"Hospitality": {
        "image": "Hospitality.JPG",
        "desc": "Tracks bookings, guest preferences, and revenue per available room (RevPAR).Enhances guest experience and operational performance.",
        "subtopics": [
            {"name": "Tours and Travels Mangement", "image":  f"subimage/Tours and Travels Mangement.JPG",  "iframe": "https://app.powerbi.com/view?r=eyJrIjoiN2NhY2VjYmMtNGYwNS00MDcyLThlNDUtNGM2NTVmZjI4NTA4IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]

    },
"Logistics": {
        "image": "Logistics.JPG",
        "desc": "Analyzes delivery times, transportation efficiency, and route optimization.Improves supply chain visibility and cost control.",
        "subtopics": [
            {"name": "Logistics Analysis Report", "image": f"subimage/Logistics Analysis Report.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNzI4NmUzMDctYmNiNi00MThlLWIwOTctOGM1ZGEwNThhNmY2IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Production Quality Management Dashboard", "image": f"subimage/Production Quality Management.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNjFmMWM4NWUtN2M5MC00ZjJiLWJmMDUtYzE5NWNmMTc2MzY3IiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": "Subcontract Purchase and Quality Management Dashboard", "image":f"subimage/Subcontract Purchase and Quality Management.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiNzUzMDc2ODItMTc1MC00YjM0LTgzZDAtMzEwNGZjOTQ3YTgwIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

            {"name": "Supplier Purchase and Quality Manageme", "image": f"subimage/Supplier Purchase and Quality Manageme.JPG", "iframe": "https://powerbi.com/iframe5"},

         {"name": "Supplychain and Management Dashboard", "image": f"subimage/Supplychain and Management Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOTRkZmZjM2UtNmJiNC00OTFhLTk3MzAtMTE3MGI3MmQ2MjExIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"},

{"name": "Warehouse Dashboard", "image": f"subimage/Warehouse Dashboard.JPG", "iframe": "https://app.powerbi.com/view?r=eyJrIjoiOWI5MGIzZTYtOGZmMy00YTUzLThmNWEtNmRkMmY3ZWM2NzhmIiwidCI6ImQ5NmNiMzRlLTc0YmUtNDAyZS04M2Y4LWIyZDUwNGM0YmNmYSJ9"}
        ]

    },

"Medical": {
        "image": "Medical.JPG",
        "desc": "Evaluates patient data, treatment outcomes, and resource utilization.Supports better decision-making in patient care and hospital operations.",
        "subtopics": [
            {"name": "Hospital Management Dashboard", "image": f"subimage/Hospital Management Dashboard.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Hospital Performance Dashboard", "image": f"subimage/Hospital Performance Dashboard.JPG", "iframe": "https://powerbi.com/iframe5"},

{"name": "Patient Details Dashboard", "image":f"subimage/Patient Details Dashboard.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Patient Healthcare Dashboard", "image":f"subimage/Patient Healthcare Dashboard.JPG" , "iframe": "https://powerbi.com/iframe5"},

  {"name": "USA Hospital Report", "image": f"subimage/USA Hospital Report.JPG", "iframe": "https://powerbi.com/iframe5"}
        ]

    },
"Presentation": {
        "image": "Presentation.JPG",
        "desc": "Tracks viewer engagement, content reach, and presentation performance.Offers insights into audience interest and delivery effectiveness.",
        "subtopics": [
            {"name": "Categorization", "image": f"subimage/Categorization.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Demography", "image": f"subimage/Demography.JPG", "iframe": "https://powerbi.com/iframe5"},

        {"name": "Maps", "image": f"subimage/Maps.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Detail View", "image": f"subimage/Detail View.JPG", "iframe": "https://powerbi.com/iframe5"},

        {"name": "Forecasting", "image": f"subimage/Forecasting.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Trend", "image": f"subimage/Trend.JPG", "iframe": "https://powerbi.com/iframe5"},
        ]

    },

"Property": {
        "image": "Property.JPG",
        "desc": "Monitors property occupancy, rental income, and lease cycles.Enables data-driven investment, maintenance, and property value insights.",
        "subtopics": [
            {"name": "Magic Bricks Real Estate", "image": f"subimage/Magic Bricks Real Estate.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Real Estate Analysis Dashboard", "image":f"subimage/Real Estate Analysis Dashboard.JPG", "iframe": "https://powerbi.com/iframe5"}
        ]

    },

"Retail": {
        "image": "Retail.JPG",
        "desc": "Analyzes customer behavior, sales patterns, and inventory turnover.Supports demand forecasting and store-level performance optimization.",
        "subtopics": [
            {"name": "E Commerce Dashboard", "image": f"subimage/E Commerce Dashboard.JPG", "iframe": "https://powerbi.com/iframe4"},

            {"name": "Jewellery Sales and Stock Analysis Dashboard", "image": f"subimage/Jewellery Sales and Stock Analysis Dashboard.JPG", "iframe": "https://powerbi.com/iframe5"},

 {"name": "Red Shift dashbaord", "image": f"subimage/Red Shift dashbaord.JPG", "iframe": "https://powerbi.com/iframe5"}
        ]

    },


"Sales": {
        "image": "Sales.JPG",
        "desc": "Provides real-time tracking of sales performance, revenue, and customer acquisition trends.Helps identify top-selling products.",
        "subtopics": [
            {"name": "Adventure Works Sales Dashboard", "image": f"subimage/Adventure Works Sales Dashboard.JPG", "iframe": "https://powerbi.com/iframe4"}
        ]

    },
}

# ------------------ IMAGE ENCODER WITH INLINE PLACEHOLDER ------------------
placeholder_img_base64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAAAM1BMVEUAAAD////f39/m5ubk5OTq6urZ2dnW1tb19fXm5ufo6OjV1dXb29vPz8/X19fR0dGjo6PGxsa2trYn2SCDAAAAX0lEQVRoge3NMQ0AIBDAwP3/p9vRQYFwZQ2Z83iBJkiRJkiRJkiRJkiRJkiRJkiRJkiRJ0osQXGeB7d2O+eGz6m7fZy9qrbvbpc+rl7f3t3un+7P1o8Oj+M1JJkiRJkiRJkiRJkiRJkiRJkiRJkrT+BFt0pMfMjE54AAAAAElFTkSuQmCC"
)

def encode_image(file_path):
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return placeholder_img_base64

# ------------------ MAIN PAGE ------------------
if st.session_state.page == "main":
    st.markdown("<h2 style='text-align: center;'>Power BI Portfolios</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (topic, data) in enumerate(topics.items()):
        with cols[i % 3]:
            img_base64 = encode_image(data["image"])
            st.markdown(f"""
                <div class='card' style='border:1px solid #ddd; border-radius: 12px; overflow: hidden; text-align: center; margin-bottom: 20px;'>
                    <img src="data:image/jpg;base64,{img_base64}" style='width:100%; height:200px; object-fit: cover;'>
                    <div style='padding: 10px;'>
                        <h4>{topic}</h4>
                        <p>{data['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open {topic}"):
                st.session_state.page = "subtopics"
                st.session_state.selected_topic = topic

# ------------------ SUBTOPICS ------------------
elif st.session_state.page == "subtopics":
    topic = st.session_state.selected_topic
    st.markdown(f"<h2>{topic} - Subtopics</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([8, 2])
    with col1:
        st.button("⬅️ Back", on_click=lambda: st.session_state.update({"page": "main"}))
    with col2:
        search_query = st.text_input("", placeholder="Search Subtopics")

    subtopics = topics[topic]["subtopics"]
    filtered = [s for s in subtopics if search_query.lower() in s["name"].lower()]

    cols = st.columns(3)
    for i, sub in enumerate(filtered):
        with cols[i % 3]:
            img_base64 = encode_image(sub["image"])
            st.markdown(f"""
                <div class='card' style='border:1px solid #ddd; border-radius: 12px; overflow: hidden; text-align: center; margin-bottom: 20px;'>
                    <img src="data:image/jpg;base64,{img_base64}" style='width:100%; height:180px; object-fit: cover;'>
                    <div style='padding: 10px;'>
                        <h5>{sub['name']}</h5>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"View {sub['name']}"):
                st.session_state.selected_subtopic = sub
                st.session_state.page = "dashboard"

# ------------------ DASHBOARD ------------------
elif st.session_state.page == "dashboard":
    sub = st.session_state.selected_subtopic
    st.button("⬅️ Back to Subtopics", on_click=lambda: st.session_state.update({"page": "subtopics", "selected_subtopic": None}))
    st.markdown(f"<h2>{sub['name']} Dashboard</h2>", unsafe_allow_html=True)
    st.components.v1.iframe(sub["iframe"], height=900, width=5000 )

# ------------------ FOOTER ------------------



st.markdown("""
---  
<div style='text-align: center; font-size: 22px;'>
    © 2025 VTAB Square Private Limited. All rights reserved.
</div>
""", unsafe_allow_html=True)
