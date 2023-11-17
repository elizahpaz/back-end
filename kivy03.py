import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green =[0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class ExemploLayout(App):
    def build(self):
        layout = BoxLayout(padding = 20)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = f"esse é o botão #{i+1}",
            background_color = random.choice(colors))
            layout.add_widget(btn)
        return layout

if __name__=="__main__":
    app = ExemploLayout()
    app.run()