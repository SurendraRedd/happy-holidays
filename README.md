# Happy Holidays Streamlit App

A festive Streamlit application that generates personalized holiday greetings with animations and interactive features.

## Features

- **Personalized Greetings**: Customize the app with your name via URL parameters
- **Holiday Animations**: Multiple Lottie animations for a festive experience
- **Interactive Elements**: Buttons, expanders, and celebration effects
- **Responsive Layout**: Uses columns and latest Streamlit features for better UX

## How to Use

1. **Run the App**:
   ```bash
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```

2. **Personalize Your Experience**:
   - Add `?name=YourName` to the URL
   - Example: `http://localhost:8501/?name=Alice`

3. **Explore the App**:
   - View your personalized holiday greeting
   - Enjoy holiday animations and twinkling stars
   - Trigger celebration effects with buttons

4. **Interactive Features**:
   - Click "Send Wishes Back!" for balloons
   - Expand "More Holiday Wishes" for additional messages
   - Start the twinkling stars animation
   - Click "Celebrate Now!" for full celebration mode

## Latest Streamlit Features Used

- `st.columns()` for responsive layout
- `st.expander()` for collapsible sections
- `st.balloons()` and `st.snow()` for celebrations
- Wide layout with `layout="wide"`
- Query parameters for personalization

## Requirements

- Python 3.8+
- Streamlit >= 1.29.0
- streamlit-extras
- streamlit-lottie

## Installation

```bash
git clone <repository-url>
cd happy-holidays
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Customization

- Add more Lottie animations in the `assets/` folder
- Modify CSS in `style/style.css` for custom styling
- Add new interactive features as needed

Enjoy the holidays! 🎄✨
