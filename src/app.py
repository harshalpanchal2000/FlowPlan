import streamlit as st

# Title and Description
st.title("FlowPlan: Seamlessly Navigate Your Day, Every Day.")
st.write("Too much to do? Too little time? Meet FlowPlan: Your AI task-scheduling assistant. Get a personalized schedule daily, effortlessly. FlowPlan takes your tasks, prioritizes, and optimizes your schedule automatically. Perfect plans, always."")

# Collecting User Input
st.header("Input your daily tasks and goals:")

user_input = st.text_area("Please list your daily tasks and goals here. For example:\n1. 8:00 AM - Breakfast\n2. 9:00 AM - Work on project X\n3. 12:30 PM - Lunch\n4. 3:00 PM - Gym session")

# Generating Schedule
st.header("Your Personalized Schedule:")

tasks_and_goals = user_input.split("\n")



