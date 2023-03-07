from utils.layout import *  
from utils import get_summaries, get_summary_doc, generate_report_summaries, generate_report_summary_doc, get_title_paper
import time       

# TODO
# 1. Fix update the progress bar
# 2. Fix calc sumary doc once 
 
class InsightMateApp(MDApp):
    selection = ListProperty([])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_path = None
        self.summaries = None
        self.progress_percent = 0  # initialize progress percentage to 0
        self.selected_file = False
        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        self.screen = MainScreen(name='main')

        return self.screen

    
    def summarize_pages(self):
        if self.selected_file:
            self.screen.progress.value = 0  # update progress bar
            
            self.summaries = dict()
            generator = get_summaries(doc_path = self.doc_path)
            # Loop through the generator object and print the values
            while True:
                try:
                    page_number, summary, number_of_pages = next(generator)
                    print(f"Page number: {page_number}")
                    print(f"Number of pages: {number_of_pages}")
                    self.summaries[page_number] = summary
                    self.screen.progress.value = int(round((page_number + 1) / (number_of_pages) * 100))  # update progress bar
                    print(f"self.screen.progress.value : {self.screen.progress.value }")

                except StopIteration:
                    # Stop the loop when the generator is exhausted
                    break
            self.selected_file = False
            generate_report_summaries(self.title_paper, self.summaries)
            
    def summarize_document(self):
        if self.summaries is not None:
            self.screen.progress.value = 0  # update progress bar
            self.summary_doc = get_summary_doc(self.summaries)
            generate_report_summary_doc(self.title_paper, self.summary_doc)
            self.selected_file = False
            self.screen.progress.value = 100  # update progress bar

            
        
    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filters = [ '*.pdf', '*.docx', '*.doc']  # add more video file extensions here
        path = './docs/*'
        filechooser.open_file(filters=filters, on_selection=self.handle_selection, path=path)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        if selection is not None:
            self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        self.selected_file = True
        self.doc_path = self.selection[0]
        self.screen.file_path.text = self.doc_path
        self.title_paper = get_title_paper(doc_path = self.doc_path, debug=False)
        
InsightMateApp().run()
