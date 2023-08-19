import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

# Убирает возможность изменять размер программы
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '1284');
Config.set('graphics', 'height', '2778');


class MyApp(App):
    def build(self):
        return Button(text="Push", font_size=40, on_press=self.btn_click, background_color=[.181, .154, .214, 1],
                      background_normal='')

    def btn_click(self, instance):
        print('button click')
        instance.text = "Active button"


if __name__ == "__main__":
    MyApp().run()
