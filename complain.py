import streamlit as st

# Set up page configurations with a cute icon
st.set_page_config(page_title="For My Baby", page_icon="❤️", layout="centered")

# Custom Styles for the Cute Palette
st.markdown("""
    <style>
    /* Light pastel purple/blue background */
    .stApp {
        background-color: #f0f4ff;
    }
    
    /* Main Layout Container */
    .container {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-top: 10vh;
    }
    
    .title-text {
        color: #4b0082; /* Deep Indigo/Purple */
        font-size: 3rem;
        margin-bottom: 10px;
    }
    
    .sub-text {
        color: #555;
        font-size: 1.5rem;
        margin-bottom: 40px;
    }
    
    /* Interactive Button Framework Area */
    .button-box {
        position: relative;
        width: 100%;
        height: 400px;
        margin: 0 auto;
    }
    
    /* Standardized Base Button Styling (Both same size) */
    .custom-btn {
        width: 140px;
        height: 50px;
        font-size: 1.1rem;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.1s ease, background 0.3s ease;
    }
    
    .custom-btn:active {
        transform: scale(0.95);
    }
    
    /* Blue Yes Button */
    .yes-btn {
        background: linear-gradient(135deg, #007bff, #0056b3);
        color: white;
        position: absolute;
        left: calc(50% - 160px);
        top: 20px;
    }
    
    /* Purple No Button (Initial position right next to Yes) */
    .no-btn {
        background: linear-gradient(135deg, #8a2be2, #4b0082);
        color: white;
        position: absolute;
        left: calc(50% + 20px);
        top: 20px;
        z-index: 999;
    }
    
    /* Success Celebration Screen Styling */
    .celebrate-card {
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        display: inline-block;
        margin-top: 5vh;
        border: 2px solid #8a2be2;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State to track if they successfully clicked YES
if "loved" not in st.session_state:
    st.session_state.loved = False

# Action handler if Yes is clicked
if st.session_state.loved:
    st.balloons()
    st.markdown("""
        <div style="text-align: center;">
            <div class="celebrate-card">
                <h1 style="color: #8a2be2; font-size: 3rem; margin-bottom: 20px;">
                    YAAAAYYY! I love you more! 🥰❤️
                </h1>
                <p style="font-size: 1.2rem; color: #555;">You finally admitted it! ✨</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Reset Game 🔄"):
        st.session_state.loved = False
        st.clear_cache()
        st.rerun()

else:
    # Header Elements
    st.markdown("""
        <div class="container">
            <h1 class="title-text">Hello, baby ko ❤️</h1>
            <p class="sub-text">Do you love me?</p>
        </div>
    """, unsafe_allow_html=True)

    # Invisible Streamlit components to bridge UI buttons with Streamlit's back-end logic
    col1, col2 = st.columns([1, 1])
    with col1:
        # Secret hidden Streamlit button triggered via JS click when they tap "Yes"
        yes_trigger = st.button("Confirm Yes", key="hidden_yes", help="Hidden system flag")
        if yes_trigger:
            st.session_state.loved = True
            st.rerun()

    # The actual Interactive HTML/JavaScript Sandbox
    # Contains both identical size buttons and the script to make the No button run away instantly
    html_button_system = """
    <div class="button-box" id="arena">
        <button class="custom-btn yes-btn" id="yesBtn">Yes</button>
        <button class="custom-btn no-btn" id="noBtn">No</button>
    </div>

    <script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');
    const arena = document.getElementById('arena');
    
    let clickCount = 0;
    const complaints = [
        "No?", 
        "Why? 🥺", 
        "Are you sure? 💔", 
        "You don't really love me?", 
        "Think again! 😭"
    ];

    // Function to run away randomly inside the dedicated arena area
    function teleportNoButton() {
        clickCount++;
        
        // Loop through the complaints array indefinitely
        noBtn.innerText = complaints[(clickCount - 1) % complaints.length];
        
        // Calculate bounds so it stays within the screen visibility area
        const maxWidth = arena.clientWidth - noBtn.clientWidth;
        const maxHeight = arena.clientHeight - noBtn.clientHeight;
        
        // Generate random placements
        const randomX = Math.floor(Math.random() * maxWidth);
        const randomY = Math.floor(Math.random() * maxHeight);
        
        // Apply position styles
        noBtn.style.left = randomX + 'px';
        noBtn.style.top = randomY + 'px';
    }

    // Teleports on Click / Tap
    noBtn.addEventListener('click', (e) => {
        e.preventDefault();
        teleportNoButton();
    });
    
    // Also runs away if they try to hover over it on desktops!
    noBtn.addEventListener('mouseover', () => {
        teleportNoButton();
    });

    // Wire up the custom HTML Yes button to click the hidden Streamlit framework button
    yesBtn.addEventListener('click', () => {
        // Targets Streamlit's native button generation structure
        const nativeButtons = window.parent.document.querySelectorAll('button');
        for (let btn of nativeButtons) {
            if (btn.innerText === "Confirm Yes") {
                btn.click();
                break;
            }
        }
    });
    </script>
    """
    
    # Render the interactive system into the app frame
    st.components.v1.html(html_button_system, height=450)

    # Hide the ugly backend infrastructure buttons from view using clean CSS overrides
    st.markdown("""
        <style>
        button[kind="secondary"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
