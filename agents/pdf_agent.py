import re
import fitz  # PyMuPDF

def extract_invoice_fields(text: str):
    invoice_patterns = [
        r"Invoice\s+No[:\s]*([A-Z0-9\-]+)",
        r"Invoice\s*#[:\s]*([A-Z0-9\-]+)",
        r"Inv\s*No[:\s]*([A-Z0-9\-]+)"
    ]
    total_patterns = [
        r"Total\s+Amount[:\s]*([\d,.]+ ?€?)",
        r"Amount\s+Due[:\s]*([\d,.]+ ?€?)",
        r"Amount\s*[:\s]*([\d,.]+ ?€?)"
    ]
    date_patterns = [
        r"Date[:\s]*(\d{4}[-./]\d{2}[-./]\d{2})",
        r"Date[:\s]*(\d{2}[-./]\d{2}[-./]\d{4})",
    ]
    recipient_patterns = [
        r"Bill\s*To[:\s]*(.+)",  # capture anything after Bill To:
        r"Recipient[:\s]*(.+)",
        r"(Musterkunde AG|(?:Mr\.|Ms\.|Mrs\.)\s+\w+\s+\w+)"
    ]

    def search_patterns(patterns, text):
        for pat in patterns:
            m = re.search(pat, text, re.IGNORECASE)
            if m:
                return m.group(1).strip()
        return None

    invoice_no = search_patterns(invoice_patterns, text)
    total = search_patterns(total_patterns, text)
    date = search_patterns(date_patterns, text)
    recipient = search_patterns(recipient_patterns, text)

    return {
        "invoice_number": invoice_no,
        "total_amount": total,
        "date": date,
        "recipient": recipient
    }

def process_pdf(file_bytes: bytes):
    try:
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            text = ""
            page_count = len(doc)
            for page in doc:
                text += page.get_text()

        print("----- Extracted PDF Text Start -----")
        print(text[:1000])  # print first 1000 chars for debug
        print("----- Extracted PDF Text End -------")

        fields = extract_invoice_fields(text)

        return {
            "message": "PDF processed",
            "page_count": page_count,
            "text_snippet": text[:500],
            "follow_up": "invoice" in text.lower(),
            "extracted_fields": fields
        }

    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}
