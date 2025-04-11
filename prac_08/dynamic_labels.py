from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """App that dynamically creates Labels for each name in the list."""
    status_text = StringProperty("")

    def __init__(self, **kwargs):
        """Construct the app with an initial list of names."""
        super().__init__(**kwargs)
        # List of names to generate labels
        self.names_list = ["Patience", "Ruth", "Sheila", "Tracy"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        """Create labels for each name in the names_list and add them to the layout."""
        for name in self.names_list:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        """Clear all labels from the entries_box layout."""
        self.root.ids.entries_box.clear_widgets()

DynamicLabelsApp().run()
