from agents.email_agent import process_email
from agents.json_agent import process_json
from agents.pdf_agent import process_pdf

def classify_input(content: str) -> str:
    """
    Classify input type based on content.
    Returns: 'email', 'json', or 'pdf'
    """
    if "@" in content:
        return "email"
    if content.strip().startswith("{"):
        return "json"
    return "pdf"

def classify_and_process_file(file_path: str):
    """
    Classify file based on content and process it using the right agent.
    """
    # For PDFs, read in binary mode
    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            content = f.read()
        return process_pdf(content)

    # For text files (email or json), read as text
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    content_type = classify_input(content)

    if content_type == "email":
        return process_email(content)
    elif content_type == "json":
        return process_json(content)
    else:
        return "Unsupported content type"

# For quick test
if __name__ == "__main__":
    test_files = [
        "../static/sample_invoice.pdf",
        "../static/sample_email.txt",
        "../static/sample_webhook.json"
    ]

    for file in test_files:
        print(f"Processing {file}:")
        output = classify_and_process_file(file)
        print(output)
        print("-" * 40)
