from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="It's my first button!",
            font_size = 30,
            on_press = self.btn_press)

    def btn_press(self, isinstance):
        print('Button was pressed!')
        isinstance.text = "I'm pressed"

if __name__ == "__main__":
    MyApp().run()
