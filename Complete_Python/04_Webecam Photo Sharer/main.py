from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        #get user query from TextInput in kv file
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and taake url of the first image from the list
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        #Download that image
        req = requests.get(self.get_image_link())
        filepath = 'files/image.jpg'
        with open(filepath, 'wb') as file:
            file.write(req.content)
        return filepath

    def set_image(self):
        #Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
