import streamlit as st

# Title and Description
st.title("FlowPlan: Personalized Schedule Planner")
st.write("FlowPlan helps you organize your daily tasks and long-term goals effortlessly.")

# Collecting User Input
st.header("Input your daily maintenance tasks:")

with st.beta_expander("Bath Time"):
    bath_time = st.radio("Do you have a specific time for bath or is it flexible?", ["I have a specific time", "It's flexible"])
    if bath_time == "I have a specific time":
        bath_duration = st.slider("How long do you spend on bath? (minutes)", min_value=5, max_value=120, step=5, value=30)
    else:
        bath_duration = st.slider("Maximum duration for bath? (minutes)", min_value=5, max_value=120, step=5, value=60)

with st.beta_expander("Breakfast Time"):
    breakfast_time = st.radio("Do you have a specific time for breakfast or is it flexible?", ["I have a specific time", "It's flexible"])
    if breakfast_time == "I have a specific time":
        breakfast_duration = st.slider("How long do you spend on breakfast? (minutes)", min_value=5, max_value=120, step=5, value=30)
    else:
        breakfast_duration = st.slider("Maximum duration for breakfast? (minutes)", min_value=5, max_value=120, step=5, value=60)

with st.beta_expander("Work Time"):
    work_time = st.radio("Do you have a specific time for work or is it flexible?", ["I have a specific time", "It's flexible"])
    if work_time == "I have a specific time":
        work_duration = st.slider("How long do you work? (minutes)", min_value=30, max_value=600, step=30, value=240)
    else:
        work_duration = st.slider("Maximum duration for work? (minutes)", min_value=30, max_value=600, step=30, value=240)

with st.beta_expander("Gym Time"):
    gym_time = st.radio("Do you have a specific time for gym or is it flexible?", ["I have a specific time", "It's flexible"])
    if gym_time == "I have a specific time":
        gym_duration = st.slider("How long do you spend at the gym? (minutes)", min_value=30, max_value=180, step=15, value=60)
    else:
        gym_duration = st.slider("Maximum duration for gym? (minutes)", min_value=30, max_value=180, step=15, value=60)

with st.beta_expander("Hobbies Time"):
    hobbies_time = st.radio("Do you have a specific time for hobbies or is it flexible?", ["I have a specific time", "It's flexible"])
    if hobbies_time == "I have a specific time":
        hobbies_duration = st.slider("How long do you spend on hobbies? (minutes)", min_value=30, max_value=240, step=15, value=60)
    else:
        hobbies_duration = st.slider("Maximum duration for hobbies? (minutes)", min_value=30, max_value=240, step=15, value=60)

with st.beta_expander("Family Time"):
    family_time = st.radio("Do you have a specific time for family time or is it flexible?", ["I have a specific time", "It's flexible"])
    if family_time == "I have a specific time":
        family_duration = st.slider("How long do you spend with family? (minutes)", min_value=30, max_value=240, step=15, value=60)
    else:
        family_duration = st.slider("Maximum duration for family time? (minutes)", min_value=30, max_value=240, step=15, value=60)

st.header("Input your weekly goals:")
weekly_goals = st.text_area("Weekly Goals", "1. Finish project X\n2. Exercise 3 times a week\n3. Read one book")

st.header("Input your monthly goals:")
monthly_goals = st.text_area("Monthly Goals", "1. Learn new skill\n2. Plan vacation\n3. Complete online course")

# Generating Schedule
st.header("Your Personalized Schedule:")

st.subheader("Daily Planner:")
st.write("- Bath Time:", bath_time)
if bath_time == "I have a specific time":
    st.write(f"  - Duration: {bath_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {bath_duration} minutes")

st.write("- Breakfast Time:", breakfast_time)
if breakfast_time == "I have a specific time":
    st.write(f"  - Duration: {breakfast_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {breakfast_duration} minutes")

st.write("- Work Time:", work_time)
if work_time == "I have a specific time":
    st.write(f"  - Duration: {work_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {work_duration} minutes")

st.write("- Gym Time:", gym_time)
if gym_time == "I have a specific time":
    st.write(f"  - Duration: {gym_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {gym_duration} minutes")

st.write("- Hobbies Time:", hobbies_time)
if hobbies_time == "I have a specific time":
    st.write(f"  - Duration: {hobbies_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {hobbies_duration} minutes")

st.write("- Family Time:", family_time)
if family_time == "I have a specific time":
    st.write(f"  - Duration: {family_duration} minutes")
else:
    st.write(f"  - Maximum Duration: {family_duration} minutes")

st.subheader("Weekly Goals:")
st.write(weekly_goals)

st.subheader("Monthly Goals:")
st.write(monthly_goals)
