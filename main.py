from utils.layout import *  
from utils import get_summaries, get_summary_doc, generate_report_summaries, generate_report_summary_doc, get_title_paper
        
class InsightMateApp(MDApp):
    selection = ListProperty([])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_path = None
        self.summaries = None
        self.progress_percent = 0  # initialize progress percentage to 0

        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        self.screen = MainScreen(name='main')

        return self.screen

    
    def summarize_document(self):
        if self.summaries is not None:
            self.summary_doc = get_summary_doc(self.summaries)
            generate_report_summary_doc(self.title_paper, self.summary_doc)
            self.progress_percent = 100  # set progress percentage to 100 when done
        self.screen.progress.value = self.progress_percent  # update progress bar

    def summarize_pages(self):
        print(self.selection)
        if self.doc_path is not None:
            self.summaries = get_summaries(doc_path = self.doc_path )
            generate_report_summaries(self.title_paper, self.summaries)
            self.progress_percent = 100  # set progress percentage to 100 when done
        self.screen.progress.value = self.progress_percent  # update progress bar
        
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
        self.doc_path = self.selection[0]
        self.screen.file_path.text = self.doc_path
        self.title_paper = get_title_paper(doc_path = self.doc_path, debug=False)
        
InsightMateApp().run()
