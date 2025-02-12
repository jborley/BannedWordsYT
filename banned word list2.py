#banned word list
#finished at 100 for poss and 114 for banned

import csv
import whisper

# Load Whisper model
model = whisper.load_model("base")
result = model.transcribe("Hauntedarkhouse.mp4")  # Change this to your file
text = result["text"].lower()  # Convert text to lowercase for case-insensitive matching

# Function to load words from CSV
def load_words_from_csv(filename):
    possible_demonetized = []  # Corrected variable name

    with open(filename, mode='r', newline='', encoding='utf-8') as file:  # Fixed filename reference
        reader = csv.reader(file)
        next(reader, None)  # Skip header row if it exists

        for row in reader:
            if len(row) >= 1:  # Ensure row has at least one column
                possible_demonetized.append(row[0].strip())  # Use first column

    return possible_demonetized  # Return the correctly named list

# Load words from CSV
possible_demonetized_words = load_words_from_csv("PossibleDemonitizedWords.csv")

# Find words in text
found_wordsp = [word for word in possible_demonetized_words if word in text]

# Print results
if found_wordsp:
    print(f"Possible_Demonitized_words detected: {', '.join(found_wordsp)}")
else:
    print("No Possible_Demonitized_words detected.")
