# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the scene that is shown after the user successfuly completes a level.

from scene import *
import ui
from level_1 import *

class LevelCompletedScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/completed_scene_background.JPG',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        home_button_position = Vector2()
        home_button_position.x = self.screen_center_x + 100
        home_button_position.y = self.screen_center_y - 100
        self.home_button = SpriteNode('./assets/sprites/home_button.JPG',
                                            parent = self,
                                            position = home_button_position,
                                            scale = 0.2)               
                                     
        retry_button_position = Vector2()
        retry_button_position.x = self.screen_center_x + 100
        retry_button_position.y = self.screen_center_y + 100
        self.retry_button = SpriteNode('./assets/sprites/retry_button.JPG',
                                          parent = self,
                                          position = retry_button_position,                                                               
                                          scale = 0.1)   
        
        next_button_position = Vector2()
        next_button_position.x = self.screen_center_x + 100
        next_button_position.y = self.screen_center_y + 250
        self.next_button = SpriteNode('./assets/sprites/next_button.JPG',
                                           parent = self,
                                           position = next_button_position,
                                           scale = 0.1)  
    
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
        
        # if retry button is pressed, restart the game
            
        # if home button is pressed, goto MainMenuScene scene
        #if self.home_button.frame.contains_point(touch.location):
            #self.present_modal_scene(MainMenuScene())
        
        # if next button is pressed, goto next level
        # if self.next_button.frame.contains_point(touch.location):
             #self.present_modal_scene(Level_2_scene)
             
    
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
    
