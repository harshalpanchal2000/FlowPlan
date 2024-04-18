import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

# Title and Description
st.title("FlowPlan: Seamlessly Navigate Your Day, Every Day.")
st.write("Too much to do? Too little time? Meet FlowPlan: Your AI task-scheduling assistant. Get a personalized schedule daily, effortlessly. FlowPlan takes your tasks, prioritizes, and optimizes your schedule automatically. Perfect plans, always.")

# Collecting User Input
#st.header("Input your daily tasks and goals:")
#user_input = st.text_area("Please list your daily tasks and goals here. For example:\n1. 8:00 AM - Breakfast\n2. 9:00 AM - Work on project X\n3. 12:30 PM - Lunch\n4. 3:00 PM - Gym session")

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/codegemma-7b-it")
model = AutoModelForCausalLM.from_pretrained("google/codegemma-7b-it")

# Function to generate responses
def flowplan(message: str, 
              history: list,
              max_new_tokens: int
             ) -> str:
    """
    Generate a streaming response using the FlowPlan model.
    Args:
        message (str): The input message.
        history (list): The conversation history.
        max_new_tokens (int): The maximum number of new tokens to generate.
    Returns:
        str: The generated response.
    """
    conversation = [{"role": "user", "content": msg} for msg in history]
    conversation.append({"role": "user", "content": message})

    input_ids = tokenizer.apply_chat_template(conversation, return_tensors="pt").to(model.device)
    streamer = TextIteratorStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    generate_kwargs = {
        "input_ids": input_ids,
        "streamer": streamer,
        "max_new_tokens": max_new_tokens,
        "do_sample": True,
    }

    t = Thread(target=model.generate, kwargs=generate_kwargs)
    t.start()

    outputs = []
    for text in streamer:
        outputs.append(text)
        return "".join(outputs)

# Streamlit components
st.markdown(DESCRIPTION, unsafe_allow_html=True)
message = st.text_input("You:", value="", help="Type your message here")
max_new_tokens = st.slider("Max New Tokens", min_value=128, max_value=4096, step=1, value=512)

if st.button("Send"):
    st.text_area("FlowPlan:", value=flowplan(message, [], max_new_tokens), height=200)



