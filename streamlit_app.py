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


# Page configuration
st.set_page_config(page_title="Happy Holidays", page_icon="🎄", layout="wide")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main content
# Display header with personalized name
st.header("Happy Holidays, Everyone! 🎄", anchor=False)

# Personalized holiday message
st.markdown(
    "Wishing you a wonderful holiday season filled with joy and peace. 🌟"
)

st.header("Holiday Animations")

# Main holiday animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-main", height=300)

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

st.header("Celebrate!")
st.markdown("Click below to celebrate the holidays!")

if st.button("Celebrate Now! 🎊"):
    st.balloons()
    st.snow()  # Note: st.snow is deprecated, but keeping for now
    time.sleep(1)
    st.success("Happy Holidays! 🎄✨")