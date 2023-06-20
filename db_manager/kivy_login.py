from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]
        self.spacing = 10

        self.username_input = TextInput(multiline=False)
        self.add_widget(Label(text='Username'))
        self.add_widget(self.username_input)

        self.password_input = TextInput(multiline=False, password=True)
        self.add_widget(Label(text='Password'))
        self.add_widget(self.password_input)

        self.add_widget(Button(text='Login', on_press=self.login))

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Make a request to the Django backend for authentication
        response = requests.post('http://127.0.0.1:8000/login', data={'username': username, 'password': password})
        if response.status_code == 200:
            print('Login successful')
            # Perform necessary actions after successful login
        else:
            print('Login failed')

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
