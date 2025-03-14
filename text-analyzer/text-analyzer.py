import streamlit as st

st.title("Text Analyzer")

# Input text
paragraph = st.text_area("Enter a paragraph to analyze:", height=150)

# Check if the paragraph contains a specific word
word_to_check = st.text_input("Enter a word to check if it exists in the paragraph:")
if st.button("Check Word"):
    contains_word = word_to_check in paragraph
    st.markdown(f"**Does the paragraph contain the word '{word_to_check}'?** {'Yes' if contains_word else 'No'}")

# Replace a word in the paragraph
word_to_replace = st.text_input("Enter a word to replace:")
replacement_word = st.text_input("Enter the replacement word:")
if st.button("Replace Word"):
    if word_to_replace and replacement_word:
        modified_paragraph = paragraph.replace(word_to_replace, replacement_word)
        st.markdown("### Modified Paragraph:")
        st.write(modified_paragraph)
    else:
        st.warning("Please enter both the word to replace and the replacement word.")

# Analyze the paragraph
if st.button("Analyze"):
    if paragraph:
        # Total words
        words = paragraph.split()
        total_words = len(words)
        
        # Total characters
        total_characters = len(paragraph)
        
        # Number of vowels
        vowels = "AEIOUaeiou"
        total_vowels = sum(1 for char in paragraph if char in vowels)
        
        # Paragraph in uppercase
        uppercase_paragraph = paragraph.upper()
        
        # Paragraph in lowercase
        lowercase_paragraph = paragraph.lower()
        
        # Average word length
        average_word_length = total_characters / total_words if total_words > 0 else 0
        
        # Display results
        st.markdown("### Original Paragraph:")
        st.write(paragraph)
        
        st.markdown(f"**Total Words:** {total_words}")
        st.markdown(f"**Total Characters:** {total_characters}")
        st.markdown(f"**Number of Vowels:** {total_vowels}")
        
        st.markdown("### Paragraph in Uppercase:")
        st.write(uppercase_paragraph)
        
        st.markdown("### Paragraph in Lowercase:")
        st.write(lowercase_paragraph)
        
        st.markdown(f"**Average Word Length:** {average_word_length:.2f}")