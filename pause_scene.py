# Created by: Kay Lin
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the pause scene.

from scene import *
import ui

from main_menu_scene import *
from help_scene import *
from levels_list_scene import *
from level_1 import *
import config

class PauseScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode(color = 'grey',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        play_button_position = Vector2()
        play_button_position.x = self.screen_center_x - 90
        play_button_position.y = self.screen_center_y + 160
        self.play_button = SpriteNode('./assets/sprites/resume_button.png',
                                       parent = self,
                                       position = play_button_position,
                                       scale = 0.6)               
                                     
        retry_button_position = Vector2()
        retry_button_position.x = self.screen_center_x + 90
        retry_button_position.y = self.screen_center_y + 160
        self.retry_button = SpriteNode('./assets/sprites/retry_button.png',
                                          parent = self,
                                          position = retry_button_position,                                                               
                                          scale = 0.6)       
        
        sound_on_button_position = Vector2()
        sound_on_button_position.x = self.screen_center_x - 90
        sound_on_button_position.y = self.screen_center_y
        self.sound_on_button = SpriteNode('./assets/sprites/sound_on_button.png',
                                           parent = self,
                                           position = sound_on_button_position,
                                           scale = 0.6)  
        
        question_mark_button_position = Vector2()
        question_mark_button_position.x = self.screen_center_x + 90
        question_mark_button_position.y = self.screen_center_y
        self.question_mark_button = SpriteNode('./assets/sprites/help_simple_button.png',
                                            parent = self,
                                            position = question_mark_button_position,
                                            scale = 0.6)
                                            
        
        home_button_position = Vector2()
        home_button_position.x = self.screen_center_x
        home_button_position.y = self.screen_center_y - 160
        self.home_button = SpriteNode('./assets/sprites/main_menu_button.PNG',
                                            parent = self,
                                            position = home_button_position,
                                            scale = 1.5)                                    
                                                                   
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
        
        # if play button is pressed, go back to the game scene
        if self.play_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        # if retry button is pressed, restart the game
        
        
        # if sound on button is pressed, goto game scene
        
        # if question mark button is pressed, goto help scene
        if self.question_mark_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
        # if home button is pressed, goto main menu game scene
        if self.home_button.frame.contains_point(touch.location):
            config.pressed_pause = True
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
    
