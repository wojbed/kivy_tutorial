from kivy.uix.button import Label
from kivy.app import App

class HelloKivyApp(App):
    def build(self):
        return Label()

helloKivy = HelloKivyApp()
helloKivy.run()