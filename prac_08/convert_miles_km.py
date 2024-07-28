""""
CP1404, Week 8 Practical 8
App that converts miles to kilometres

Estimated time to complete: 40 minutes
Actual:
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    """ MilesToKilometres is a Kivy app for converting miles to kilometres """

    def build(self):
        """ Build Kivy app from kv file"""
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.user_input.text


# create and start the App running
MilesToKilometres().run()
