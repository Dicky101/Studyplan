import requests
import re
from io import BytesIO
from pypdf import PdfReader

import requests
import re
from bs4 import BeautifulSoup

def get_subject_codes() -> list[str]:
    response = requests.get("https://prog-crs.hkust.edu.hk/ugcourse", timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    codes = []
    for line in text.splitlines():
        line = line.strip()
        if re.fullmatch(r'[A-Z]{4}', line):
            codes.append(line)

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
# url = "https://ugadmin.hkust.edu.hk/prog_crs/ug/202526/pdf/25-26math.pdf"
# courses = extract_math_courses_from_pdf_url(url)
# print("MATH courses:", courses)