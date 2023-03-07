# Author
# Muhammed Elyamani
# GitHub: https://github.com/WikiGenius

import os 
from jinja2 import Environment, FileSystemLoader
import webbrowser

def generate_report_summaries(title_paper, summaries, report_template = "/report_template_summaries.html"):
    env = Environment(loader=FileSystemLoader('./templates/'))
    template = env.get_template(report_template)

        
    html = template.render(summaries=summaries, page_title = title_paper)
    report_summaries_path = "./generations/report_summaries.html"
    with open(report_summaries_path, "w") as f:
        f.write(html)
    
    # open the generated HTML file in the default web browser
    webbrowser.open("file://" + os.path.realpath(report_summaries_path))


def generate_report_summary_doc(title_paper, summary_doc, report_template = "/report_template_summary_doc.html"):
    env = Environment(loader=FileSystemLoader('./templates/'))
    template = env.get_template(report_template)

        
    html = template.render(summary=summary_doc, page_title = title_paper)
    report_summaries_path = "./generations/report_summary.html"
    with open(report_summaries_path, "w") as f:
        f.write(html)
    
    # open the generated HTML file in the default web browser
    webbrowser.open("file://" + os.path.realpath(report_summaries_path))