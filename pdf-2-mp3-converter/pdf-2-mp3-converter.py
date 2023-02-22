import pypdf
import pyttsx3
import os

def open_pdf_file(pdf_file_name):
    print('Opening pdf file: ' + pdf_file_name)
    pdf_file = open(pdf_file_name, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    return pdf_reader

def extract_text_from_pdf(pdf_reader):
    print('Extracting text from pdf file')
    full_text = ''
    for page in pdf_reader.pages:
        text = page.extract_text()
        full_text = full_text + text
    return full_text

def save_text_as_mp3(text, mp3_file_name):
    print('Saving text as mp3 file: ' + mp3_file_name)
    engine = pyttsx3.init()
    engine.save_to_file(text, mp3_file_name)
    engine.runAndWait()

def search_for_pdf_files_in_directory_recursively(directory):
    print('Searching for pdf files in directory: ' + directory)
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(root + '\\' + file)
                print('Found pdf file: ' + file)
    return pdf_files

def main():
    pdf_files = search_for_pdf_files_in_directory_recursively(os.getcwd())
    for pdf_file in pdf_files:
        pdf_reader = open_pdf_file(pdf_file)
        text = extract_text_from_pdf(pdf_reader)
        mp3_file_name = pdf_file.replace('.pdf', '.mp3')
        save_text_as_mp3(text, mp3_file_name)
        print('Done converting pdf file: ' + pdf_file)
    print('Done converting all pdf files')

main()