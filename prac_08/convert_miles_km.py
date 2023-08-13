"""
CP1404 Prac_08
Margareth Tajonera

Kivy GUI program to convert miles to kilometres
"""


class DistanceConverterApp(App):
    """ DistanceConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('converting.kv')
        return self.root



    def handle_calculate(self, value):
        """ handle calculation, output result to label widget """
