import re

# Read the original HTML file
with open('/home/ubuntu/ChinaTown/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Function to remove all citations
def remove_citations(text):
    # Remove [cite_start]
    text = re.sub(r'\[cite_start\]', '', text)
    # Remove [cite: XXXX] and [cite: XXXX, YYYY, ...]
    text = re.sub(r'\[cite:\s*[\d,\s]+\]', '', text)
    return text

# Clean the content
cleaned_content = remove_citations(content)

# Save the cleaned version
with open('/home/ubuntu/ChinaTown/index_cleaned.html', 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

print("Citations removed successfully!")
