from kivy.app import App
from kivy.uix.button import Button


class MeningIlovam(App):

  def build(self):
    return Button(text="Salom, GitHub APK!")


if __name__ == "__main__":
  MeningIlovam().run()
