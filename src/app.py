import streamlit as st
from transformers import pipeline, Conversation

page_bg_img = """
<style>
[data-testid="stApp"] {
background-color: #e5e5f7;
opacity: 0.6;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 10px ), repeating-linear-gradient( #444cf755, #444cf7 );}
</style>
"""

# Apply the custom CSS style to set the background image
st.markdown(page_bg_img, unsafe_allow_html=True)


# Title and Description
st.title("FlowPlan: Seamlessly Navigate Your Day, Every Day.")
st.write("Too much to do? Too little time? Meet FlowPlan: Your AI task-scheduling assistant. Get a personalized schedule daily, effortlessly. FlowPlan takes your tasks, prioritizes, and optimizes your schedule automatically. Perfect plans, always.")

# Function to generate responses
def flowplan(message: str) -> str:
    """
    Generate a response using the FlowPlan model.
    Args:
        message (str): The input message.
    Returns:
        str: The generated response.
    """
    flowplan_pipeline = pipeline("text-generation", model="google/codegemma-7b-it")
    conversation = Conversation()
    conversation.add_user_input(message)
    response = flowplan_pipeline(conversation)
    return response[0]["generated_text"]

# Streamlit components
DESCRIPTION = "Some description here."
st.markdown(DESCRIPTION, unsafe_allow_html=True)
message = st.text_input("You:", value="", help="Type your message here")

if st.button("Send"):
    generated_response = flowplan(message)
    st.text_area("FlowPlan:", value=generated_response, height=200)
