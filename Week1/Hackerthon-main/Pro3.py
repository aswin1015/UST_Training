import re
from collections import Counter

def count_words_in_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = re.findall(r"\w+", ' '.join(lines).lower())
    count = Counter(words)
    total_words = sum(count.values())
    rare_words = {word : freq for word, freq in count.items() if freq/total_words < 0.01}

    for line in lines:
        if any(word in line.lower() for word in rare_words):
            print(f"Flagged Line: {line.strip()}")