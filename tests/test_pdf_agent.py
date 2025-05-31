import os
from agents.pdf_agent import process_pdf

# Path to your sample PDF
pdf_path = os.path.join("static", "sample_inputs", "sample_invoice.pdf")

# Read the PDF as bytes
with open(pdf_path, "rb") as f:
    file_bytes = f.read()

# Process the PDF
result = process_pdf(file_bytes)

# Print the result
print("\n--- PDF Processing Result ---")
for key, value in result.items():
    print(f"{key}: {value}")
