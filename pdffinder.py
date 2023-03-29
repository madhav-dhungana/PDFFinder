import os
import csv
import PyPDF2
import textract

# Define the keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']

# Define the folder where the PDF files are stored
folder_path = '/path/to/pdf/folder'

# Create an empty list to store the results
results = []

# Loop over all the PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Open the PDF file using PyPDF2
        pdf_file = open(os.path.join(folder_path, filename), 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Extract the text from the PDF using textract
        pdf_text = textract.process(pdf_file).decode('utf-8')
        
        # Search the text for the keywords
        for keyword in keywords:
            if pdf_text.find(keyword) != -1:
                # If the keyword is found, add the PDF file name and keyword to the results list
                results.append([filename, keyword])
        
        # Close the PDF file
        pdf_file.close()

# Write the results to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['File Name', 'Keyword'])
    csvwriter.writerows(results)
