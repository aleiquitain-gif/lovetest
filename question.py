import streamlit as st
import random

st.set_page_config(page_title="For My Baby", page_icon="❤️", layout="centered")

if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False
if "btn_top" not in st.session_state:
    st.session_state.btn_top = 60  # Initial vertical position (%)
if "btn_left" not in st.session_state:
    st.session_state.btn_left = 55 # Initial horizontal position (%)

# List of guilt-trip complaints that loop indefinitely
no_prompts = [
    "No?", 
    "Why? 🥺", 
    "Are you sure? 💔", 
    "You don't really love me?", 
    "Think again! 😭"
]

# Calculate the text for the No button based on click count
current_no_text = no_prompts[st.session_state.no_clicks % len(no_prompts)]

# --- PAGE STYLING & LAYOUT ---
# Sweet, pink pastel aesthetic styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffeef2;
    }
    .title-text {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #d63384;
        text-align: center;
        font-size: 3rem;
        margin-top: 50px;
    }
    .sub-text {
        font-family: Arial, sans-serif;
        color: #6c757d;
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SCENARIO 1: YES IS CLICKED ---
if st.session_state.yes_clicked:
    st.markdown('<h1 class="title-text">YAAAAYYY! I love you more! 🥰❤️</h1>', unsafe_allow_html=True)
    st.balloons()
    
    # Add a reset button to start over if wanted
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Celebrate Again? ✨", type="secondary"):
        st.session_state.no_clicks = 0
        st.session_state.yes_clicked = False
        st.session_state.btn_top = 60
        st.session_state.btn_left = 55
        st.rerun()

# --- SCENARIO 2: DEFAULT SCREEN ---
else:
    st.markdown('<h1 class="title-text">Hello, baby ko ❤️</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Do you love me?</p>', unsafe_allow_html=True)

    # Stationary YES Button Container
    col1, col2 = st.columns([1, 1])
    with col1:
        # Pushes down slightly to align horizontally with the initial NO button area
        st.write("<br><br><br>", unsafe_allow_html=True)
        if st.button("Yes", type="primary", use_container_width=True):
            st.session_state.yes_clicked = True
            st.rerun()

    # Absolute Position Styling for the RUNAWAY NO Button
    # This overrides the typical layout grid to let the button fly anywhere!
    runaway_btn_style = f"""
    <style>
    div.element-container:has(button:contains("{current_no_text}")) {{
        position: fixed !important;
        top: {st.session_state.btn_top}% !important;
        left: {st.session_state.btn_left}% !important;
        z-index: 9999 !important;
        width: auto !important;
    }}
    div.element-container:has(button:contains("{current_no_text}")) button {{
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15) !important;
        transition: all 0.1s ease !important;
    }}
    </style>
    """
    st.markdown(runaway_btn_style, unsafe_allow_html=True)

    with col2:
        # The Runaway Button itself
        if st.button(current_no_text):
            # Advance the complaint index
            st.session_state.no_clicks += 1
            
            # Teleport the button to a completely new random area on the screen
            # Kept within 20%-80% range so it doesn't run off the screen entirely
            st.session_state.btn_top = random.randint(20, 80)
            st.session_state.btn_left = random.randint(20, 80)
            st.rerun()
