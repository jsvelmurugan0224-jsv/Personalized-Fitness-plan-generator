🎯 Objective of the Milestone:

The objective of this milestone is to integrate an AI language model into the FitPlan AI application to generate personalized workout plans based on user-provided fitness details.

This milestone aims to:

Collect structured fitness data (name, gender, height, weight, fitness goal, level, and equipment).
Calculate Body Mass Index (BMI) using user inputs.
Classify BMI into standard health categories (Underweight, Normal, Overweight, Obese).
Design and construct an effective prompt using user data.
Connect the application to a pre-trained language model via the Hugging Face Inference API.
Generate personalized 5-day workout plans through model inference.
Deploy the fully functional AI-enabled application on Hugging Face Spaces.
The milestone establishes the foundation for intelligent fitness recommendations using prompt engineering and large language model integration.

🤖 Model Name Used:

Model: Qwen/Qwen2.5-7B-Instruct
Provider: Hugging Face Inference API (via InferenceClient)

🧠 Prompt Design Explanation:

The prompt is carefully structured to guide the language model in generating a safe, personalized, and well-organized workout plan.

1️⃣ Role Assignment

The prompt begins with:
"You are a certified professional fitness trainer."
This assigns a professional identity to the model, encouraging expert-level, structured, and responsible output.

2️⃣ Clear Task Definition

The instruction:
"Create a structured 5-day personalized workout plan."

clearly defines:

*Output format (5-day plan)
*Personalization requirement
*Structured presentation

This reduces vague or unstructured responses.

3️⃣ Context-Rich User Profile

The prompt includes detailed user information:
*Name
*Age
*Gender
*Height & Weight
*BMI (calculated dynamically)
*BMI Category
*Fitness Goal
*Fitness Level
*Available Equipment

Including BMI and BMI category improves personalization because:

*Underweight → moderate intensity muscle gain
*Overweight → fat-loss focus
*Obese → low-impact safe exercises
*Normal → balanced programming

This ensures context-aware generation.

4️⃣ Explicit Output Formatting Instructions

The prompt explicitly instructs the model to:

1.Divide clearly into Day 1 to Day 5
2.Include exercise name
3.Include sets and reps
4.Include rest period
5.Adjust intensity based on BMI category
6.Avoid unsafe exercises for beginners
7.Keep the plan professional and easy to follow

These numbered instructions act as control constraints, improving:

1.Structure consistency
2.Safety
3.Professional formatting
4.Readability

5️⃣ Dynamic Personalization

The prompt dynamically inserts:

- BMI: {bmi:.2f} ({bmi_status})
- Goal: {goal}
- Fitness Level: {fitness_level}
- Available Equipment: {equipment_list}

This allows the same template to generate different workout plans for different users without changing the core structure.

⚙️ Steps Performed(model loading, prompt creation, inference testing):

1️⃣ Model Loading

*Imported InferenceClient from huggingface_hub.
*Retrieved the Hugging Face API token securely using:

os.getenv("HF_TOKEN")

*Initialized the model client with:

InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=HF_TOKEN
)

*Configured chat-based completion using:
 *System role: "You are a certified professional fitness trainer."
 *User role: dynamically generated fitness prompt
 *Temperature: 0.7 (balanced creativity and control)
 *Max tokens: 2000 (to allow full 5-day plan generation)

This step ensures the model is properly connected and ready for inference.

2️⃣ Prompt Creation

*Collected user inputs through the Streamlit interface:

 *Name
 *Age
 *Gender
 *Height (cm)
 *Weight (kg)
 *Fitness Goal
 *Fitness Level
 *Available Equipment

*Converted height from centimeters to meters.
*Calculated BMI using:

BMI = weight / (height in meters)^2

*Rounded BMI to two decimal places.

*Classified BMI into:
 *Underweight
 *Normal Weight
 *Overweight
 *Obese

*Built a structured prompt using build_prompt() that:
 *Assigns a professional trainer role
 *Includes detailed user profile
 *Specifies formatting instructions (Day 1–Day 5)
 *Adds safety and intensity guidance

This step ensures contextual and personalized AI generation.

3️⃣ Inference Testing

*Sent the generated prompt to the model using:

client.chat_completion()

*Passed both:
 *System message (role definition)
 *User message (structured prompt)

*Retrieved model output from:

response.choices[0].message.content

*Displayed the generated workout plan in the Streamlit interface.
*Verified:
 *Correct structure (Day 1–Day 5)
 *Inclusion of exercises, sets, reps, and rest
 *Personalization based on BMI and goal

This confirms that the AI inference pipeline works successfully end-to-end.

📊 Sample Generated Outputs

Below is an example of the AI-generated workout plan based on user inputs.

🧾 Example User Input

Name: Rahul
Age: 24
Gender: Male
Height: 175 cm
Weight: 78 kg
BMI: 25.47 (Overweight)
Goal: Lose Weight
Fitness Level: Intermediate
Available Equipment: Dumbbells, Treadmill

🤖 Example Generated Workout Plan

Day 1: Upper Body Fat Burn
Warm-up:
- Treadmill brisk walk – 5 minutes

Workout:
- Dumbbell Chest Press – 4 sets × 12 reps (Rest: 45 seconds)
- Dumbbell Shoulder Press – 3 sets × 12 reps (Rest: 45 seconds)
- Push-ups – 3 sets × 15 reps (Rest: 30 seconds)
- Plank – 3 sets × 40 seconds (Rest: 30 seconds)

Day 2: Lower Body Conditioning
Warm-up:
- Bodyweight Squats – 2 sets × 15 reps

Workout:
- Dumbbell Lunges – 4 sets × 12 reps per leg (Rest: 45 seconds)
- Goblet Squats – 3 sets × 12 reps (Rest: 45 seconds)
- Calf Raises – 3 sets × 20 reps (Rest: 30 seconds)
- Treadmill Incline Walk – 10 minutes

Day 3: Core & Cardio
- Mountain Climbers – 3 sets × 30 seconds
- Russian Twists – 3 sets × 20 reps
- Leg Raises – 3 sets × 15 reps
- Treadmill Jog – 15 minutes

Day 4: Full Body Circuit
Perform circuit 3 rounds:
- Dumbbell Deadlift – 12 reps
- Push-ups – 15 reps
- Jump Squats – 15 reps
- Plank – 45 seconds
(Rest: 1 minute between rounds)

Day 5: Active Recovery & Mobility
- Light Treadmill Walk – 15 minutes
- Hamstring Stretch – 30 seconds per leg
- Shoulder Mobility Drills – 10 minutes
- Deep Breathing Exercises – 5 minutes

🔗Hugging Face Space Deployment Link:

Live Application link:
https://huggingface.co/spaces/js02vel/Module2/tree/main
