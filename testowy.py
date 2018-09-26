from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Etykieta(BoxLayout):
    def build(self):
        return Label()

class HelloKivyApp(App):
    def build(self):
        return Etykieta()

helloKivy = HelloKivyApp()
helloKivy.run()