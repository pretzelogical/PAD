import pdfquery

# Load the PDF file
pdf = pdfquery.PDFQuery("../data/electedofficials.pdf")
pdf.load()

# Highlight all text elements
pdf.tree.write("../data/output_annotated.xml", pretty_print=True)

print("Annotated PDF created successfully.")
