import pygame
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


pygame.init()


class Tela(BoxLayout):

    def tocar_audio(self, arquivo):
        toque = pygame.mixer.Sound(arquivo)
        toque.play()

class Main(App):
    def build(self):
        return Tela()

Main().run()
