from kivy.lang import Builder
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivymd.icon_definitions import md_icons
from kivy.uix.scatter import Scatter
import cv2
import main

Config.set('graphics', 'width', '768')
Config.set('graphics', 'height', '1024')

Window.size = (480, 768)

class ContainerF(Widget):

    valuesArr = {}
    a = True


    def cameraFunc(self):
        box1 = self.box1
        box2 = self.box2
        cam = self.camera
        if self.a == True:
            self.remove_widget(box1)
            self.box2.disabled = False
            self.box2.opacity = 1
            cam.play = True
            self.a = False
        elif self.a == False:
            self.add_widget(box1)
            self.box2.disabled = True
            self.box2.opacity = 0
            cam.play = False
            self.a = True
        return 0 


    def inputValues(self):        
        
        self.valuesArr[self.quantity.text] = float(self.value.text)
        main.desired = self.desired.text
        print(self.valuesArr)
        print(main.desired)
        self.quantity.text = ""
        self.value.text = ""
        return 0
    
    def appSolver(self):
        
        print(main.desired)
        valueNames = list(self.valuesArr)
        missingNames = list(self.valuesArr)


        p = main.definingBestfunc(valueNames,main.desired,main.var)

        res = main.finalSolver(p,self.valuesArr,main.var,main.desired)
        self.answer.text = f"{main.desired}={str(res)}"
        self.valuesArr = main.valueArrClear(self.valuesArr)
        self.desired.text = ""
        print(res)
        return res
    

cont = ContainerF()

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return ContainerF()


if __name__ == "__main__":
    MyApp().run()