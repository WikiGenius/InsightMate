# Author
# Muhammed Elyamani
# GitHub: https://github.com/WikiGenius

import PyPDF2
def extract_pages(doc_path = 'docs/2022.11.18.517004v2.full.pdf'):
    info_doc = dict()
    pdf_file = open(doc_path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    info_doc['number_of_pages'] = number_of_pages
    info_doc['pages'] = []
    for page_number in range(number_of_pages):  
        page = read_pdf.getPage(page_number)
        page_text = page.extractText()
        info_doc['pages'].append(page_text)
    pdf_file.close()
    return info_doc