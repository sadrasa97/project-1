from kivy.app import App
from kivy.uix.label import Label

# Define the main application class
class MainApp(App):
    def build(self):
        # Create a Label widget with the text "Hello"
        return Label(text='Hello')

# Run the app
if __name__ == '__main__':
    MainApp().run()
