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
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """
        get text input from widget and convert to float
        :return: 0 if error, float of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


# create and start the App running
MilesToKilometres().run()
