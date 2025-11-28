import re
from num2words import num2words

def clean_text(text):
    # Convert numbers to text
    def replace_numbers(match):
        return num2words(int(match.group()))

    text = re.sub(r'\d+', replace_numbers, text)

    # Lowercase
    text = text.lower()

    # Remove special characters (letters + spaces only)
    text = re.sub(r'[^a-z\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# ============================
# Read from file, clean, write
# ============================

input_file = "input.txt"
output_file = "output.txt"

# Read input text
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Clean the text
cleaned = clean_text(text)

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(cleaned)

print("Done! Cleaned text saved to", output_file)
