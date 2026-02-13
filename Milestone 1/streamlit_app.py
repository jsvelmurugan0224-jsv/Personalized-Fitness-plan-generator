import streamlit as st

# 1. Basic Configuration
st.set_page_config(page_title="FitPlan AI", page_icon="💪", layout="centered")

# 2. Enhanced CSS
st.markdown("""
<style>
    /* Full Page Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), 
                    url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Hide the "Press Enter to submit form" hint globally */
    [data-testid="InputInstructions"] {
        display: none !important;
    }

    /* Form Container Polish */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.98) !important;
        padding: 3rem !important;
        border-radius: 20px !important;
        border: none !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }

    /* --- FONT SIZE UPDATES --- */
    /* Main Title (FitPlan AI) */
    .main-title {
        color: #FFFFFF !important;
        font-size: 60px !important;
        font-weight: 850 !important;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Subtitle (Your personalized gym companion) */
    .sub-title {
        color: #E0E0E0 !important;
        font-size: 24px !important;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 40px;
        font-style: italic;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }

    /* Form Section Headers (Orange) */
    .form-header {
        color: #f97316 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Labels for inputs */
    label p {
        font-size: 18px !important;
        color: #1e293b !important;
        font-weight: 600 !important;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #f97316, #ea580c) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        height: 3.5rem !important;
        border-radius: 12px !important;
        border: none !important;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# UI Header Section
# --------------------------------------------------
st.markdown('<p class="main-title">💪 FitPlan AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your personalized gym companion</p>', unsafe_allow_html=True)

# --------------------------------------------------
# Fitness Profile Form
# --------------------------------------------------
with st.form("fitness_form", clear_on_submit=False):
    st.markdown('<p class="form-header">🧍‍♂️ 1. PERSONAL INFORMATION</p>', unsafe_allow_html=True)
    
    name = st.text_input("Full Name *", placeholder="Enter your full name")

    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("Height (cm) *", min_value=0.0, step=1.0, value=0.0)
    with col2:
        weight = st.number_input("Weight (kg) *", min_value=0.0, step=0.1, value=0.0)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="form-header">🏋️ 2. FITNESS DETAILS</p>', unsafe_allow_html=True)
    
    goal = st.selectbox("Fitness Goal", ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"])
    
    equipment = st.multiselect("Available Equipment", 
                               ["Dumbbells", "Resistance Band", "Yoga Mat", "Kettlebell", "Pull-up Bar", "No Equipment"],
                               default=["No Equipment"])
    
    level = st.radio("Fitness Level", ["Beginner", "Intermediate", "Advanced"], horizontal=True)

    # Submission Button
    submit = st.form_submit_button("GENERATE MY PLAN")

# --------------------------------------------------
# Logic & Calculation
# --------------------------------------------------
if submit:
    if not name.strip() or height <= 50 or weight <= 10:
        st.error("🚨 Please provide a valid name, height, and weight.")
    else:
        # BMI Calculation
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            cat, color = "Underweight", "blue"
        elif 18.5 <= bmi < 25:
            cat, color = "Normal", "green"
        elif 25 <= bmi < 30:
            cat, color = "Overweight", "orange"
        else:
            cat, color = "Obese", "red"

        # Results Display
        st.balloons()
        st.success(f"✅ Profile created for {name}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Calculated BMI", bmi)
        with c2:
            st.markdown(f"### Status: :{color}[{cat}]")
        
        st.info(f"**Goal:** {goal} | **Experience:** {level}")