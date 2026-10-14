from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text="Welcome Prof Hafid - APK Ready", font_size=30)

if __name__ == "__main__":
    MainApp().run()
