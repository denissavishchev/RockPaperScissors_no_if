from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import random
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'resizable', 0)
Window.size = (360,190)
#720-1280

saveInput = " "

class RockPaperScissorsApp(App):

    def whois(self,choice):
        global saveInput
        guess = choice.text
        choices = ['Rock', 'Paper', 'Scissors']
        computer_guess = random.choice(choices)
        guess_dict = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
        guess_idx = guess_dict.get(guess, 3)
        computer_idx = guess_dict.get(computer_guess)
        result_matrix = [[0, 2, 1],
                         [1, 0, 2],
                         [2, 1, 0],
                         [3, 3, 3]]
        result_idx = result_matrix[guess_idx][computer_idx]
        result_messages = ["Draw Game", "You win!!!", 'Computer wins...']
        result = result_messages[result_idx]
        saveInput = self.result.text = 'Computer choice is: '+ computer_guess + '\n' + result

    def build(self):
        root = BoxLayout(orientation='vertical', padding=5,spacing = 3)

        self.result = TextInput(text="",foreground_color = (1,1,1,1),readonly=True, font_size=50,
                                size_hint=[1, .5], background_color=[1, 1, 1, .5])
        root.add_widget(self.result)

        allButtons = GridLayout(cols=3, padding = 1,spacing = 4)

        allButtons.add_widget(Button(background_normal = 'rock.jpg',text = 'Rock',font_size=40,on_press=self.whois))
        allButtons.add_widget(Button(background_normal = 'paper.jpg',text = 'Paper',font_size=40,on_press=self.whois))
        allButtons.add_widget(Button(background_normal = 'scissors.jpg',text = 'Scissors',font_size=40,on_press=self.whois))

        root.add_widget(allButtons)
        return root

if __name__ == "__main__":
    RockPaperScissorsApp().run()
