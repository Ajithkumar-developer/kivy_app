import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.camera import Camera
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout

class DemoApp(App):
    def build(self):
        return Label(text="hello world")
    
# widgets
class WidgetApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical', spacing = 10)
        label = Label(text = "This is text")
        button = Button(text = "button")
        text_input = TextInput(hint_text = "input text")
        image = Image(source = "sp3.jpg")

        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(text_input)
        layout.add_widget(image)

        return layout

    
# layouts
class LayoutApp(App):
    def build(self):

        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # box layout
        box_layout = BoxLayout(orientation='horizontal', spacing=10)
        box_layout.add_widget(Label(text="Box layout"))
        box_layout.add_widget(Button(text="Button 1"))
        box_layout.add_widget(Button(text="Button 2"))

        main_layout.add_widget(box_layout)

        # Grid layout
        grid_layout = GridLayout(rows=2, cols=2, spacing=10)
        grid_layout.add_widget(Label(text="grid layout"))
        grid_layout.add_widget(Button(text="Button 3"))
        grid_layout.add_widget(Button(text="Button 4"))
        grid_layout.add_widget(Label(text="Layout"))

        main_layout.add_widget(grid_layout)

        # Float layout
        # float_layout = FloatLayout()
        # float_layout.add_widget(Label(text="float layout", pos=(100,100)))
        # float_layout.add_widget(Button(text="button 6", pos=(150, 50)))
        # float_layout.add_widget(Button(text="button 7", pos=(250, 150)))

        # main_layout.add_widget(float_layout)

        return main_layout


# User interactions and event handling
class CounterApp(App):
    def build(self):

        box_layout = BoxLayout(orientation='vertical', spacing=10)
        self.count = 0
        self.label = Label(text=str(self.count), font_size=70)
        box_layout.add_widget(self.label)
        

        grid_layout = GridLayout(rows=1, cols=3, spacing=10)
        self.add = Button(text='+')
        self.dec = Button(text='-')
        self.res = Button(text='Reset')
        
        self.dec.bind(on_press=self.value)
        self.res.bind(on_press=self.value)
        self.add.bind(on_press=self.value)
        
        grid_layout.add_widget(self.dec)
        grid_layout.add_widget(self.res)
        grid_layout.add_widget(self.add)

        box_layout.add_widget(grid_layout)

        return box_layout
    
    def value(self, instance):
        if instance.text == '+':
            self.count += 1
            self.label.text = str(self.count)

        elif instance.text == '-':
            self.count -= 1
            self.label.text = str(self.count)

        elif instance.text == 'Reset' :
            self.count = 0
            self.label.text = str(self.count)

        else: 
            print("Button not clicked")

    
# access camera
class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)

        return layout
    

# Rock paper scissor
class RPSApp(App):
    def build(self):
        layout = BoxLayout(orientation=("vertical"), spacing=10)
        self.label = Label(text="Choose Your Choice --> Rock / Paper / Scissor", font_size = 30, markup=True)
        layout.add_widget(self.label)

        self.your_choice = ''
        self.computer_choice = ''

        # Button creation
        grid_layout = GridLayout(rows=1, cols=4, spacing=10)
        self.rock = Button(text='Rock')
        self.paper = Button(text='Paper')
        self.scissor = Button(text='Scissor')
        

        # Binding choise
        self.rock.bind(on_press=self.choice)
        self.paper.bind(on_press=self.choice)
        self.scissor.bind(on_press=self.choice)
        

        # Add to widget
        grid_layout.add_widget(self.rock)
        grid_layout.add_widget(self.paper)
        grid_layout.add_widget(self.scissor)
        

        # add grid to layout
        layout.add_widget(grid_layout)

        return layout

    # choosing choice
    def choice(self, instance):
        if instance.text == 'Rock':
            self.your_choise = 'Rock'
        elif instance.text == 'Paper':
            self.your_choise = 'Paper'
        elif instance.text == 'Scissor':
            self.your_choise = 'Scissor'
        else:
            print("Nothing")
        self.computer()


    def computer(self):
        choices = ['Rock', 'Paper', 'Scissor']
        self.computer_choice = random.choice(choices)
        self.check()
    
    def check(self):
        if self.your_choise == self.computer_choice:
            self.result = 'Match is Tie!'
        elif (self.your_choise == 'Rock' and self.computer_choice == 'Scissor') or \
                (self.your_choise == 'Paper' and self.computer_choice == 'Rock') or \
                (self.your_choise == 'Scissor' and self.computer_choice == 'Paper'):
            self.result = 'You Win!'
        else:
            self.result = 'You Lost!'
        self.label.text = f'Your choice [i]{self.your_choise}[/i]. Computer choice [i]{self.computer_choice}[/i]. [b]{self.result}[/b] '
        



if __name__ == '__main__':
    # app = DemoApp()
    # app = WidgetApp()
    # app = LayoutApp()
    # app = CounterApp()
    # app = CameraApp()
    app = RPSApp()
    app.run()