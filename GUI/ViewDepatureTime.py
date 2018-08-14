from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AbfahrtAnzeige(GridLayout):

    def __init__(self, **kwargs):
        super(AbfahrtAnzeige, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text='User Name'))
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return AbfahrtAnzeige()


if __name__ == '__main__':
    MyApp().run()