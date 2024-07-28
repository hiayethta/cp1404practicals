""""
CP1404, Week 8 Practical 8
App that converts miles to kilometres

Estimated time to complete: 40 minutes
Actual:
"""

MILES_TO_KM = 1.60934

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    """ MilesToKilometres is a Kivy app for converting miles to kilometres """
    def build(self):
        """ Build Kivy app from kv file"""
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation from miles to kilometres, output result to label"""
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


# create and start the App running
MilesToKilometres().run()
