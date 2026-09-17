import streamlit as st

# Set page title and a cute icon
st.set_page_config(page_title="For My Baby", page_icon="❤️")

st.title("Hello, baby ko ❤️")

# Initialize session states for tracking choices
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "show_yes" not in st.session_state:
    st.session_state.show_yes = False

# List of guilt-trip prompts for the No button
no_prompts = [
    "No", 
    "No?", 
    "Why?", 
    "Are you sure?", 
    "You don't really love me? 🥺", 
    "Think again! 💔"
]

# Calculate current prompt and size
current_no_text = no_prompts[st.session_state.no_clicks % len(no_prompts)]
# Button scales up with clicks, maxing out before resetting
button_size = 14 + (st.session_state.no_clicks * 15) 

# Check if they clicked Yes
if st.session_state.show_yes:
    st.balloons()
    st.success("YAAAAYYY! I love you more! 🥰")
    if st.button("Restart ❤️"):
        st.session_state.no_clicks = 0
        st.session_state.show_yes = False
        st.rerun()
else:
    st.write("Do you love me?")
    
    # Create columns to place buttons side-by-side
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if st.button("Yes", type="primary"):
            st.session_state.show_yes = True
            st.rerun()
            
    with col2:
        # Use custom HTML/CSS to dynamically size the No button safely
        no_btn_style = f"""
        <style>
        div.stButton > button:last-child {{
            font-size: {button_size}px !important;
            padding: {button_size/2}px {button_size}px !important;
            background-color: #ff4b4b !important;
            color: white !important;
        }}
        </style>
        """
        st.markdown(no_btn_style, unsafe_allow_html=True)
        
        if st.button(current_no_text):
            st.session_state.no_clicks += 1
            # If it gets way too big (e.g., 6 clicks), reset it back to 0
            if st.session_state.no_clicks >= 6:
                st.session_state.no_clicks = 0
            st.rerun()
