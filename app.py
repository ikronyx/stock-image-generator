import streamlit as st
import random
from image_utils import get_pollinations_url
import time

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

# --- UI ---
col1, col2 = st.columns(2)

with col1:
    subject = st.selectbox(
                "subject",
                subjects,
                key='subject_selectbox', # Use a different key for the selectbox itself
                index=subjects.index(st.session_state.subject) # Set the index based on the state value
            )
    location = st.selectbox(
                "location", 
                locations,
                key='location_selectbox', 
                index=locations.index(st.session_state.location)  # Set the index based on the state value
            )
    action = st.selectbox(
                "action", 
                actions,
                key='action_selectbox', 
                index=actions.index(st.session_state.action)  # Set the index based on the state value
            )

with col2:
    detail = st.selectbox(
                "detail", 
                details,
                key='detail_selectbox', 
                index=details.index(st.session_state.detail)  # Set the index based on the state value
            )
    lighting = st.selectbox(
                "lighting", 
                lightings,
                key='lighting_selectbox', 
                index=lightings.index(st.session_state.lighting)  # Set the index based on the state value
            )
    emotion = st.selectbox(
                "emotion",
                emotions,
                key='emotion_selectbox', # Use a different key for the selectbox itself
                index=emotions.index(st.session_state.emotion) # Set the index based on the state value
            )
    theme = st.selectbox(
                "theme", 
                themes,
                key='theme_selectbox', 
                index=themes.index(st.session_state.theme)  # Set the index based on the state value
            )
    style = st.selectbox(
                "style", 
                styles,
                key='style_selectbox', 
                index=styles.index(st.session_state.style)  # Set the index based on the state value
            )

# --- Prompt Generator ---
def generate_prompt():
    prompt = f"A {subject} in/on/at {location}, "
    if subject not in lifeless_subjects:
        prompt += f"{action}, "
    prompt += f"surrounded by {detail}. Lighting is {lighting}, with color tones that evoke {st.session_state.emotion}. "
    prompt += f"Symbolizes {theme}. Style: {style}."
    return prompt

def randomize():
    st.session_state.subject = random.choice(subjects)
    st.session_state.location = random.choice(locations)
    st.session_state.action = random.choice(actions)
    st.session_state.detail = random.choice(details)
    st.session_state.lighting = random.choice(lightings)
    st.session_state.emotion = random.choice(emotions)
    st.session_state.theme = random.choice(themes)
    st.session_state.style = random.choice(styles)

def click_gen_image():
    st.session_state.bt_gen_image = True

st.button("Randomize", on_click=randomize, use_container_width=True, type='secondary')
if st.button("Generate Prompt", use_container_width=True, type='primary'):
    result = generate_prompt()
    st.text_area("Generated Prompt", result, height=150)

    with st.spinner("Generating your stock image. Please wait..."):
        time.sleep(3)
    image_url = get_pollinations_url(result)
    st.image(image_url)