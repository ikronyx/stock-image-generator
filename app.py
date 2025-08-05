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
    emotion = st.selectbox(
                "Emotion",
                emotions,
                key='emotion_selectbox', # Use a different key for the selectbox itself
                index=emotions.index(st.session_state.emotion) # Set the index based on the state value
            )
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

if 'emotion' not in st.session_state:
    st.session_state.emotion = emotions[0] # Set a default value
if 'subject' not in st.session_state:
    st.session_state.subject = subjects[0]  # Set a default value
if 'location' not in st.session_state:
    st.session_state.location = locations[0]  # Set a default value
if 'action' not in st.session_state:
    st.session_state.action = actions[0]  # Set a default value
if 'detail' not in st.session_state:
    st.session_state.detail = details[0]  # Set a default value
if 'lighting' not in st.session_state:
    st.session_state.lighting = lightings[0]  # Set a default value
if 'theme' not in st.session_state:
    st.session_state.theme = themes[0]  # Set a default value
if 'style' not in st.session_state:
    st.session_state.style = styles[0]  # Set a default value

def randomize():
    st.session_state.subject = random.choice(subjects)
    st.session_state.location = random.choice(locations)
    st.session_state.action = random.choice(actions)
    st.session_state.detail = random.choice(details)
    st.session_state.lighting = random.choice(lightings)
    st.session_state.emotion = random.choice(emotions)
    st.session_state.theme = random.choice(themes)
    st.session_state.style = random.choice(styles)

def generate():
    result = generate_prompt()
    st.text_area("Generated Prompt", height=150)
# # Buttons
# col_gen, col_rand = st.columns([1, 1])
# generate = col_gen.button("Generate Prompt")
# random_ = col_rand.button("🎲 Randomize",)

# if generate:
#     result = generate_prompt()
#     st.text_area("📝 Generated Prompt", result, height=150)


# The selectbox, with its value controlled by the session state


# The button that triggers the randomization
st.button("Randomize", on_click=randomize)
st.button("Generate Prompt", on_click=generate)