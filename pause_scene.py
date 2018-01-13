# Created by: Kay Lin
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the pause scene.

from scene import *
import ui

from main_menu_scene import *
from help_scene import *

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
        play_button_position.x = self.screen_center_x - 100
        play_button_position.y = self.screen_center_y + 100                          
        self.play_button = SpriteNode('./assets/sprites/play_button.JPG',
                                       parent = self,
                                       position = play_button_position,
                                       scale = 0.2)               
                                     
        retry_button_position = Vector2()
        retry_button_position.x = self.screen_center_x + 100
        retry_button_position.y = self.screen_center_y + 100
        self.retry_button = SpriteNode('./assets/sprites/retry_button.JPG',
                                          parent = self,
                                          position = retry_button_position,                                                               
                                          scale = 0.1)       
        
        sound_on_button_position = Vector2()
        sound_on_button_position.x = self.screen_center_x - 100
        sound_on_button_position.y = self.screen_center_y
        self.sound_on_button = SpriteNode('./assets/sprites/sound_on_button.JPG',
                                           parent = self,
                                           position = sound_on_button_position,
                                           scale = 0.05)  
        
        question_mark_button_position = Vector2()
        question_mark_button_position.x = self.screen_center_x + 100
        question_mark_button_position.y = self.screen_center_y
        self.question_mark_button = SpriteNode('./assets/sprites/question_mark.JPG',
                                            parent = self,
                                            position = question_mark_button_position,
                                            scale = 0.2)
                                            
        level_list_button_position = Vector2()
        level_list_button_position.x = self.screen_center_x - 100
        level_list_button_position.y = self.screen_center_y - 100
        self.level_list_button = SpriteNode('./assets/sprites/level_list_button.JPG',
                                            parent = self,
                                            position = level_list_button_position,
                                            scale = 0.2)
                                            
        home_button_position = Vector2()
        home_button_position.x = self.screen_center_x + 100
        home_button_position.y = self.screen_center_y - 100
        self.home_button = SpriteNode('./assets/sprites/home_button.JPG',
                                            parent = self,
                                            position = home_button_position,
                                            scale = 0.2)                                    
                                                                   
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
            self.present_modal_scene(level_1_scene())
        
        # if retry button is pressed, restart the game
        
        
        # if sound on button is pressed, goto game scene
        
        # if question mark button is pressed, goto help scene
        if self.question_mark_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
        # if menu button is pressed, goto game scene
        #if self.menu_button.frame.contains_point(touch.location):
            #self.present_modal_scene(LevelsListScene())
            
        # if home button is pressed, goto MainMenuScene scene
        if self.home_button.frame.contains_point(touch.location):
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
    
