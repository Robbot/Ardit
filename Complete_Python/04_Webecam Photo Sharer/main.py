from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        #get user query from TextInput in kv file
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and taake url of the first image from the list
        page = wikipedia.page(query)
        image_link = page.images[0]
        #Download that image
        req = requests.get(image_link)
        filepath = 'files/image.jpg'
        with open(filepath, 'wb') as file:
            file.write(req.content)
        #Set the image in the Image widget
        self.manager.current_screen.ids.img.source = filepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
