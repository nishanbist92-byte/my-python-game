__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TapGame(App):
    def build(self):
        self.score = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.label = Label(
            text="Score: 0",
            font_size=32
        )

        button = Button(
            text="TAP ME!",
            font_size=28
        )
        button.bind(on_press=self.tap)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def tap(self, button):
        self.score += 1
        self.label.text = f"Score: {self.score}"


if __name__ == "__main__":
    TapGame().run()
