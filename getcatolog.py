import re
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
from pypdf import PdfReader

def extract_text_from_pdf(pdf_url: str) -> str:
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()

    with BytesIO(response.content) as pdf_file:
        text = extract_text(pdf_file)

    return text
  # Clean readable text


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


if __name__ == "__main__":
    pdf_url = "https://ugadmin.hkust.edu.hk/prog_crs/ug/202526/pdf/25-26math.pdf"
    math_courses = extract_text_from_pdf(pdf_url)
    print("MATH courses found:", math_courses[2000:2500])  # Print the first 500 characters of the extracted text