import streamlit as st
from transformers import pipeline, Conversation

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
    model_path = "https://github.com/your_username/your_repository/raw/main/model-00001-of-00004.safetensors"  # Replace with the Git LFS URL to your model
    config_path = "https://github.com/your_username/your_repository/raw/main/config.json"  # Replace with the Git LFS URL to your model configuration file

    # Generate response
    flowplan_pipeline = pipeline("text-generation", model=model_path)
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
