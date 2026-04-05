import requests
import re
from io import BytesIO
from pypdf import PdfReader

import requests
import re
from bs4 import BeautifulSoup

def get_info_from_website(url, *filters) -> list[str]:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    codes = []
    for line in text.splitlines():
        line = line.strip()

        # Check if line matches ANY of the filters
        for pattern in filters:
            if re.fullmatch(pattern, line):
                codes.append(line)
                break  # Stop checking other filters once matched

    return sorted(set(codes))


def extract_math_courses_from_pdf_url(pdf_url: str) -> list[str]:
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()

    reader = PdfReader(BytesIO(response.content))
    
    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text() or ""
    
    # Extract MATH XXXX codes (case-insensitive)
    course_codes = re.findall(r'\b(MATH\s+\d{4})\b', all_text, re.IGNORECASE)
    return sorted(set(course_codes))  # unique, sorted

# Example
