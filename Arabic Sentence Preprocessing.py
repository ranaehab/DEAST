import re
from pyarabic.number import number2text

def normalize_arabic(text):
    # Normalize Alif forms
    text = re.sub(r"[أإآٱ]", "ا", text)

    # Normalize Alif Maqsura to Yaa
    text = text.replace("ى", "ي")

    # Normalize Ta Marbuta to Ha
    text = text.replace("ة", "ه")

    return text


def replace_numbers(text):
    # Replace Arabic/English digits with words
    def num_to_words(match):
        num = int(match.group())
        return number2text(num)  # Arabic number-to-text

    return re.sub(r"\d+", num_to_words, text)


def clean_arabic_text(text):
    # 1. Normalize letters
    text = normalize_arabic(text)

    # 2. Convert digits to words
    text = replace_numbers(text)

    # 3. Remove special characters (keep Arabic, English letters & spaces)
    text = re.sub(r"[^ء-يA-Za-z\s]", " ", text)

    # 4. Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==============================
# Example usage
# ==============================

input_file = "input_ar.txt"
output_file = "output_ar.txt"

# Read input file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Process text
cleaned = clean_arabic_text(text)

# Save to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(cleaned)

print("Done! Cleaned text saved to", output_file)
