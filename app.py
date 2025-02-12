import csv
import whisper
import streamlit as st

model = whisper.load_model("base")  # Load Whisper model

def load_words_from_csv(filename):
    possible_demonetized = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for row in reader:
            if len(row) >= 1:
                possible_demonetized.append(row[0].strip())
    return possible_demonetized

st.title("Banned Word Checker")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "wav", "mp3", "mov"])

if uploaded_file is not None:
    with open("temp.mp4", "wb") as f:
        f.write(uploaded_file.read())

    # Transcribe the video
    result = model.transcribe("temp.mp4")
    text = result["text"].lower()

    # Check for banned words
    possible_demonetized_words = load_words_from_csv("PossibleDemonitizedWords.csv")
    found_words = [word for word in possible_demonetized_words if word in text]

    if found_words:
        st.error(f"⚠️ Banned words detected: {', '.join(found_words)}")
    else:
        st.success("✅ No banned words detected!")

