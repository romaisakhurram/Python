import streamlit as st

st.title("Text Analyzer")

paragraph = st.text_area("Enter a paragraph to analyze:", height=150)

word_to_check = st.text_input("Enter a word to check if it exists in the paragraph:")
if st.button("Check Word"):
    contains_word = word_to_check in paragraph
    st.markdown(f"**Does the paragraph contain the word '{word_to_check}'?** {'Yes' if contains_word else 'No'}")

word_to_replace = st.text_input("Enter a word to replace:")
replacement_word = st.text_input("Enter the replacement word:")
if st.button("Replace Word"):
    if word_to_replace and replacement_word:
        modified_paragraph = paragraph.replace(word_to_replace, replacement_word)
        st.markdown("### Modified Paragraph:")
        st.write(modified_paragraph)
    else:
        st.warning("Please enter both the word to replace and the replacement word.")

if st.button("Analyze"):
    if paragraph:
        words = paragraph.split()
        total_words = len(words)
        
        total_characters = len(paragraph)
        
        vowels = "AEIOUaeiou"
        total_vowels = sum(1 for char in paragraph if char in vowels)
        
        uppercase_paragraph = paragraph.upper()
        
        lowercase_paragraph = paragraph.lower()
        
        average_word_length = total_characters / total_words if total_words > 0 else 0
        
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