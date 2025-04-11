from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# Constant for conversion factor
MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    # StringProperty automatically updates the label
    output_text = StringProperty()

    def __init__(self, **kwargs):
        """ Initialize the app """
        super().__init__(**kwargs)
        self.output_text = '54.717'  # Default value for output label

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Calculate the conversion from miles to km and update the label """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)  # Update the output label

    def handle_increment(self, change):
        """
        Handle increment/decrement button press
        :param change: 1 to increment, -1 to decrement
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)  # Update input field with new value
        self.handle_calculate()  # Recalculate and update the label

    def get_validated_miles(self):
        """
        Get the miles value from the text input, return 0 if invalid
        :return: float or 0 if invalid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0  # If input is invalid, return 0

MilesConverterApp().run()
