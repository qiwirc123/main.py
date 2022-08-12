from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=1,spacing=1)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=140)
        main_layout.add_widget(self.solution)
        buttons = [
            ['Ce', 'C', '<-', '+'],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["pi", "0", '.', "="]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                button.bind(on_press=self.on_buttons_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        netbutton = Button(text="=")
        netbutton.bind(on_press=self.on_solution)
        main_layout.add_widget(netbutton)

        # return a Button() as a root widget
        return main_layout

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""
        else:
            self.solution.text += instance.text

    def on_buttons_press(self, instance):
        if instance.text == "pi":
            self.solution.text = "3.14159265"
  
  
    def on_solution(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"


if __name__ == '__main__':
    MainApp().run()