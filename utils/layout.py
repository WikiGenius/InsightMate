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