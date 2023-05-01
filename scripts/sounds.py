import kivy
from kivy.core.audio import SoundLoader
import random

class SoundsMaster():
    background_music = None
    
    @staticmethod
    def playMusic():
        if not SoundsMaster.background_music or SoundsMaster.background_music.state == 'stop':
            SoundsMaster.playBackgroundMusic()

    @staticmethod
    def playBackgroundMusic():
        songs = ['./assets/sounds/adventures_of_flying_jack.mp3', './assets/sounds/battle_ready.mp3', './assets/sounds/epic_blockbuster 2.mp3', './assets/sounds/epic_boss_battle.mp3']
        song = random.choice(songs)

        SoundsMaster.background_music = SoundLoader.load(song)
        SoundsMaster.background_music.play()