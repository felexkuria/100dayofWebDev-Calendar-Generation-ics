import PyPDF2

# Open the PDF file in binary read mode
file = open("100 days of code-challenge.pdf", "rb")

# Create a PdfFileReader object
reader = PyPDF2.PdfReader(file)

# Get the number of pages in the PDF
no_of_pages = len(reader.pages)


# Extract text from the first page
page = reader.pages[0]
print(page.extract_text())

# Close the file
file.close()