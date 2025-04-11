from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """ Clears the text input and label """
        self.root.ids.input_name.text = ""  # Clears the input field
        self.root.ids.output_label.text = ""  # Clears the label text

    def handle_greet(self):
        """ Updates the label with a greeting message """
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello, {name}!"

BoxLayoutDemo().run()
