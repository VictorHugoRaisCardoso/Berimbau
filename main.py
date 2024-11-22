from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(20)



class Tela(BoxLayout):
    sons = {}
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sons['1.wav'] = pygame.mixer.Sound('1.wav')
        self.sons['2.wav'] = pygame.mixer.Sound('2.wav')
        self.sons['3.wav'] = pygame.mixer.Sound('3.wav')
    
    def tocar_audio(self, tipo):
        som = self.sons.get(tipo)
        if som:
            som.play()

class Main(App):
    def build(self):
        return Tela()

Main().run()
