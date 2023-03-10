import PyPDF2
import re

# Open the PDF file
file = open('invoice.pdf', 'rb')

# Create a PDF reader object
reader = PyPDF2.PdfReader(file)

# Get the total number of pages in the PDF file
pages = len(reader.pages)

# Define the regular expression pattern to search for
pattern = "[0-9]{14}"
#pattern = "[0-9]{11}"

# Create an empty string to store the matching text
matchingText = ""

# Loop through each page and search for the pattern
for i in range(1):
    page = reader.pages[0]
    text = page.extract_text()
    matches = re.findall(pattern, text)
    matchingText += '\n'.join(matches)

# Close the PDF file
file.close()
print(text)
print("-----")
print(matchingText)

# Now, you can use the 'matchingText' variable to do further processing or send it through your external API