from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text='Hello welcome in my First Mobile app using',halign='center')

if __name__=='__main__':
    Main_App().run()

