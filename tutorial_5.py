from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.app import App

class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):

    # For checkbox
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox is Unchecked")

    # For radio buttons
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    # For switch
    def switch_on(self, instance, value):
        if value is True:
            print("Switch On")
        else:
            print("Switch Off")

    # For opens popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    # For spinner
    def spinner_clicked(self, value):
        print("Spinner value " + value)

class SampleApp(App):
    def build(self):
        # set the background color for the window
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()
