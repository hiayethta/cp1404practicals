""""
CP1404, Week 8 Practical 8
App that converts miles to kilometres

Estimated time to complete: 40 minutes
Actual:
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    def build(self):
        self.title = "Layout Hints Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


# create and start the App running
MilesToKilometres().run()