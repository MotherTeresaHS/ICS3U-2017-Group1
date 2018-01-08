# Created by: Kay Lin
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the setting scene.

from scene import *
import ui
from numpy import random

from main_menu_scene import *

class SettingScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/star_background.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        #sound_on_button_position = Vector2()
        #sound_on_button_position.x = self.screen_center_x 
        #sound_on_button_position.y = self.screen_center_y + 250
        #self.sound_on_button = SpriteNode('./assets/sprites/sound_on_button.png',
                                       #parent = self,
                                      # position = sound_on_button_position
                                      # alpha = 0.5
                                      # scale = self.scale_size)       
        
        #sound_off_button_position = Vector2()
        #sound_off_button_position.x = self.screen_center_x
        #sound_off_button_position.y = self.screen_center_y + 450
        #self.sound_off_button = SpriteNode('./assets/sprites/sound_off_button.png',
                                       #parent = self,
                                      # position = sound_off_button_position
                                      # alpha = 0.5
                                      # scale = self.scale_size) 
        
        
        #back_button_position = Vector2()
        #back_button_position.x = 100
        #back_button_position.y = back_button_position.y - 100
        #self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       #parent = self,
                                      # position = back_button_position)     

        #reset_game_button_position = Vector2()
        #reset_game_button_position.x = 100
        #reset_game_button_position.y = reset_game_button_position.y - 100
        #self.reset_game_button = SpriteNode('./assets/sprites/reset_game_button.png',
                                       #parent = self,
                                      # position = reset_game_button_position)
                                      
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
