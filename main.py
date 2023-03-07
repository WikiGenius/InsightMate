import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen
from plyer import filechooser
from kivy.properties import ListProperty

# Define the main widget for the app

Builder.load_file('InsightMate.kv')

class MainScreen(Screen):
    pass       

        
class InsightMateApp(MDApp):
    selection = ListProperty([])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_path = None
        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        self.screen = MainScreen(name='main')

        return self.screen


    def file_selected(self, selection):
        self.file_path.text = selection[0]
        self.file_chooser.path = os.path.dirname(selection[0])

    
    def summarize_document(self):
        # TODO: Add logic to summarize the entire document
        print(self.doc_path )
        pass
    
    def summarize_pages(self):
        # TODO: Add logic to summarize each page of the document
        print(self.doc_path )
        
        pass
    
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

        
InsightMateApp().run()
