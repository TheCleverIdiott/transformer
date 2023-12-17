import streamlit as st
import pdfplumber
from googletrans import Translator

def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def translate_text(text, target_language='hi'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    st.title("PDF Translator App")
    
    # Upload PDF file
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if pdf_file is not None:
        st.sidebar.header("Translation Options")
        target_language = st.sidebar.selectbox("Select Target Language", ["Hindi"])

        st.sidebar.text("Processing PDF...")
        pdf_text = pdf_to_text(pdf_file)
        st.sidebar.text("Translating...")
        translated_text = translate_text(pdf_text, target_language)

        st.subheader("Original Text")
        st.text(pdf_text)

        st.subheader("Translated Text")
        st.text(translated_text)

if __name__ == "__main__":
    main()
