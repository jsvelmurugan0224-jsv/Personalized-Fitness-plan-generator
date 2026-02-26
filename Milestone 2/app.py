import streamlit as st
from model_api import query_model
from prompt_builder import build_prompt

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(page_title="FitPlan AI", layout="centered")

st.title("🏋️ FitPlan AI – Personalized Workout Generator")

# ---------------- INPUT ---------------- #

name = st.text_input("Enter Your Name")

age = st.number_input(
    "Age (years)",
    min_value=10,
    max_value=100,
    step=1
)

gender = st.radio("Gender", ["Male", "Female"])

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=250.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=30.0,
    max_value=200.0
)

goal = st.selectbox(
    "Fitness Goal",
    ["Build Muscle", "Lose Weight", "Improve Endurance", "General Fitness"]
)

fitness_level = st.radio(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect(
    "Available Equipment",
    [
        "No Equipment", "Dumbbells", "Barbell",
        "Pull-up Bar", "Resistance Bands",
        "Treadmill", "Kettlebells", "Full Gym"
    ]
)

# ---------------- GENERATE ---------------- #

if st.button("Generate Workout Plan"):

    # -------- Validation --------
    if not name.strip():
        st.warning("Please enter your name.")

    elif age <= 0:
        st.warning("Please enter a valid age.")

    elif height <= 0 or weight <= 0:
        st.warning("Please enter valid height and weight.")

    else:
        # build_prompt now includes age
        prompt, bmi, bmi_status = build_prompt(
            name,
            age,
            gender,
            height,
            weight,
            goal,
            fitness_level,
            equipment
        )

        with st.spinner("Generating your personalized plan..."):
            response = query_model(prompt)

        # -------- Output --------
        st.subheader("📋 Your Personalized Workout Plan")
        st.write(response)

        st.info(
            f"""
            **Profile Summary**
            - Name: {name}
            - Age: {age}
            - Gender: {gender}
            - BMI: {bmi:.2f} ({bmi_status})
            - Goal: {goal}
            - Level: {fitness_level}
            """
        )
