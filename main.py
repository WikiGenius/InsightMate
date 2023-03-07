import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen
from plyer import filechooser

# Define the main widget for the app

Builder.load_file('InsightMate.kv')

class MainScreen(Screen):
    pass       

class FileUploader(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dirselect = False
        self.filters = ['*.docx', '*.doc', '*.pdf']
        
class InsightMateApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        # Create a new file chooser
        self.file_chooser = filechooser.FileChooser()
        self.file_chooser.filters = ['*.docx', '*.doc', '*.pdf']

        self.file_path = ObjectProperty(None)

        self.screen = MainScreen(name='main')

        return self.screen


def file_selected(self, selection):
    self.file_path.text = selection[0]
    self.file_chooser.path = os.path.dirname(selection[0])

    
    def summarize_document(self):
        # TODO: Add logic to summarize the entire document
        pass
    
    def summarize_pages(self):
        # TODO: Add logic to summarize each page of the document
        pass
    
InsightMateApp().run()
