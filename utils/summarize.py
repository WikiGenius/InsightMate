# Author
# Muhammed Elyamani
# GitHub: https://github.com/WikiGenius

from tqdm import tqdm
import openai
from utils import extract_pages
def summarize_page(page_text, debug=False):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=("Please summarize the following page:\n" + page_text),
        max_tokens=1000,
        n=1,
        temperature=0.5,
    )
    if debug:
        return response
    else:
        summary = response.choices[0].text.strip()
        return summary
    
def get_summaries(doc_path = 'docs/2022.11.18.517004v2.full.pdf'):
    info_doc = extract_pages(doc_path)
    summaries = dict()
    number_of_pages = info_doc['number_of_pages'] 
    for page_number in tqdm(range(number_of_pages), desc = "Summarize the pages"):
        page_text = info_doc['pages'][page_number]
        summaries[page_number] = summarize_page(page_text)
    return summaries

def get_summary_doc(summaries, debug=False):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Please summarize the following summaries for pages from paper:\n {summaries}"),
        max_tokens=1000,
        n=1,
        temperature=0.5,
    )
    if debug:
        return response
    else:
        summary_doc = response.choices[0].text.strip()
        return summary_doc