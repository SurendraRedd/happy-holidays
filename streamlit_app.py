from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import time

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]


# Page configuration
st.set_page_config(page_title="Happy Holidays", page_icon="🎄", layout="wide")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar for usage instructions
with st.sidebar:
    st.header("How to Use This App")
    st.markdown("""
    **Welcome to the Happy Holidays App!**

    This app generates personalized holiday greetings with festive animations.

    **Features:**
    - Personalized messages based on your name
    - Multiple holiday animations
    - Interactive elements

    **How to personalize:**
    - Add `?name=YourName` to the URL
    - Example: `http://localhost:8501/?name=Alice`

    **Latest Features:**
    - Responsive layout with columns
    - Tabbed interface for better organization
    - Expandable sections for more details
    - Celebration effects
    """)

# Main content with tabs
tab1, tab2, tab3 = st.tabs(["Greeting", "Animations", "Celebrate"])

with tab1:
    # Display header with personalized name
    PERSON_NAME = get_person_name()
    st.header(f"Happy Holidays, {PERSON_NAME}! 🎄", anchor=False)

    # Personalized holiday message
    st.markdown(
        f"Dear {PERSON_NAME}, wishing you a wonderful holiday season filled with joy and peace. 🌟"
    )

    # Add some interactive elements
    if st.button("Send Wishes Back!"):
        st.balloons()
        st.success("Wishes sent! 🎉")

    with st.expander("More Holiday Wishes"):
        st.markdown("""
        - May your days be merry and bright!
        - Here's to new beginnings and cherished memories.
        - Warmest wishes for a joyful holiday season.
        """)

with tab2:
    st.header("Holiday Animations")

    # Layout with columns for multiple animations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Main Animation")
        lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
        st_lottie(lottie_animation, key="lottie-main", height=300)

    with col2:
        st.subheader("Secondary Animation")
        # For now, reuse the same animation; in a real app, you'd have different ones
        lottie_animation2 = load_lottie_animation(LOTTIE_ANIMATION)
        st_lottie(lottie_animation2, key="lottie-secondary", height=300)

    # Add more animations in rows
    st.subheader("More Festive Elements")
    col3, col4, col5 = st.columns(3)
    with col3:
        st.markdown("🎄 **Christmas Tree**")
        # Placeholder for tree animation
        st.markdown("🌟 Twinkling lights animation would go here")
    with col4:
        st.markdown("🎁 **Gift Box**")
        st.markdown("🎀 Wrapping animation would go here")
    with col5:
        st.markdown("⭐ **Star**")
        st.markdown("✨ Shining star animation would go here")

    # Add a simple animated twinkling stars
    st.subheader("Twinkling Stars")
    if st.button("Start Twinkling Animation"):
        twinkling_placeholder = st.empty()
        import time
        for _ in range(6):
            twinkling_placeholder.markdown("⭐ ✨ 🌟 ⭐ ✨ 🌟")
            time.sleep(0.5)
            twinkling_placeholder.markdown("✨ 🌟 ⭐ ✨ 🌟 ⭐")
            time.sleep(0.5)
        twinkling_placeholder.markdown("⭐ ✨ 🌟 ⭐ ✨ 🌟")

with tab3:
    st.header("Celebrate!")
    st.markdown("Click below to celebrate the holidays!")

    if st.button("Celebrate Now! 🎊"):
        st.balloons()
        st.snow()  # Note: st.snow is deprecated, but keeping for now
        time.sleep(1)
        st.success("Happy Holidays! 🎄✨")

# Chat input outside tabs
st.header("Leave a Message")
user_message = st.chat_input("Type your holiday message here...")
if user_message:
    st.write(f"You said: {user_message}")
    st.markdown("Thanks for sharing! 🎉")