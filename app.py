import streamlit as st
import random

st.set_page_config(page_title="Stock Image Prompt Generator", layout="centered")

st.title("📸 Stock Prompt Generator")

lifeless_subjects = ['flower', 'tree', 'sunrise', 'mountain']

# Dropdown options
subjects = ['child', 'elderly person', 'group of people', 'flower', 'person with disability',
            'tree', 'sunrise', 'mountain', 'animal', 'family', 'healthcare worker',
            'schoolgirl', 'volunteer', 'teacher', 'protester', 'scientist', 'mother and child',
            'person in wheelchair', 'smiling teenager']

locations = ['mountain village', 'urban rooftop', 'desert', 'refugee camp', 'beach at sunrise',
             'abandoned playground', 'city park', 'flooded area', 'schoolyard', 'busy marketplace',
             'isolated road', 'community garden', 'hospital corridor', 'forest trail',
             'burnt landscape', 'train station platform']

actions = ['looking toward the sky', 'walking alone', 'holding a candle', 'reaching for the sun',
           'standing still with eyes closed', 'raising a flag', 'offering a helping hand',
           'carrying a backpack', 'hugging another person', 'sitting peacefully']

details = ['misty morning air', 'sunset in background', 'flowers blooming nearby', 'ruins of a building',
           'birds flying overhead', 'scattered leaves on the ground', 'dewdrops on grass',
           'colorful graffiti wall', 'wind gently blowing', 'overgrown plants and vines']

lightings = ['warm golden hour', 'soft morning light', 'dramatic shadows', 'moody overcast',
             'sunbeam breaking through clouds', 'glowing candlelight', 'cool twilight hues',
             'harsh midday sun']

emotions = ['hope', 'resilience', 'peace', 'unity', 'reflection', 'determination', 'healing', 'gratitude']

themes = ['Hope', 'Resilience', 'Mental Health', 'Climate Action', 'Unity', 'Rebuilding', 'Recovery', 'Human Connection']

styles = ['cinematic wide shot', 'soft focus portrait', 'high contrast black and white', 'minimalist composition',
          'natural light candid', 'documentary realism', 'aerial drone perspective', 'intimate close-up']

# --- UI ---
col1, col2 = st.columns(2)

with col1:
    subject = st.selectbox("Subject", subjects)
    location = st.selectbox("Setting/Location", locations)
    action = st.selectbox("Action or Pose", actions)

with col2:
    detail = st.selectbox("Environmental/Emotional Details", details)
    lighting = st.selectbox("Lighting Description", lightings)
    emotion = st.selectbox("Emotion", emotions)
    theme = st.selectbox("Theme", themes)
    style = st.selectbox("Style/Mood/Shot Type", styles)

# --- Prompt Generator ---
def generate_prompt():
    prompt = f"A {subject} in/on/at {location}, "
    if subject not in lifeless_subjects:
        prompt += f"{action}, "
    prompt += f"surrounded by {detail}. Lighting is {lighting}, with color tones that evoke {emotion}. "
    prompt += f"Symbolizes {theme}. Style: {style}."
    return prompt

def randomize():
    subject = random.choice(subjects)
    location = random.choice(locations)
    action = random.choice(actions)
    detail = random.choice(details)
    lighting = random.choice(lightings)
    emotion = random.choice(emotions)
    theme = random.choice(themes)
    style = random.choice(styles)

# Buttons
col_gen, col_rand = st.columns([1, 1])
generate = col_gen.button("Generate Prompt")
if col_rand.button("🎲 Randomize"):
    randomize()


if generate:
    result = generate_prompt()
    st.text_area("📝 Generated Prompt", result, height=150)


# Function to be called when the button is clicked
def randomize_emotion():
    st.session_state.emotion = random.choice(emotions)

# The selectbox, with its value controlled by the session state
st.selectbox(
    "Emotion",
    emotions,
    key='emotion_selectbox', # Use a different key for the selectbox itself
    index=emotions.index(st.session_state.emotion) # Set the index based on the state value
)

# The button that triggers the randomization
st.button("Randomize", on_click=randomize_emotion)

# You can display the current value for verification
st.write("The current emotion is:", st.session_state.emotion)