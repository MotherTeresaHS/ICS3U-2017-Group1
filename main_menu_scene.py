# Created by: Kay Lin
# Created on: Jan 2017
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from levels_list_scene import *
from help_scene import *
from setting_scene import *
from credits_scene import *
from bonus_scene import *
from pause_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background
        self.background = SpriteNode('./assets/sprites/main_menu_background.JPG',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        start_button_position = Vector2()
        start_button_position.x = self.screen_center_x-300
        start_button_position.y = self.screen_center_y+170                           
        self.start_button = SpriteNode('./assets/sprites/start_button.JPG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.1)
                                       
        help_button_position = Vector2() 
        help_button_position.x = self.screen_center_x - 300
        help_button_position.y = self.screen_center_y + 50                           
        self.help_button = SpriteNode('./assets/sprites/help_button.JPG',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 0.15)
                                       
        credits_button_position = Vector2()
        credits_button_position.x = self.screen_center_x-300
        credits_button_position.y = self.screen_center_y-70                          
        self.credits_button = SpriteNode('./assets/sprites/credits_button.JPG',
                                       parent = self,
                                       position = credits_button_position,
                                       scale = 0.2)
                                                                     
        settings_button_position = Vector2()
        settings_button_position.x = self.screen_center_x-400                            
        settings_button_position.y = self.screen_center_y-200     
        self.settings_button = SpriteNode('./assets/sprites/settings_button.JPG',
                                         parent = self,
                                         position = settings_button_position,
                                         scale = 0.1)
                                         
        bonus_button_position = Vector2()
        bonus_button_position.x = self.screen_center_x-200
        bonus_button_position.y = self.screen_center_y-200                           
        self.bonus_button = SpriteNode('./assets/sprites/bonus_button.JPG',
                                       parent = self,
                                       position = bonus_button_position,
                                       scale = 0.15)                                                                                       
    
        pause_button_position = Vector2()
        pause_button_position.x = self.screen_center_x-300
        pause_button_position.y = self.screen_center_y+300                          
        self.pause_button = SpriteNode('./assets/sprites/pause.JPG',
                                       parent = self,
                                       position = pause_button_position,
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
        
        # if start button is pressed, goto game scene
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(LevelsListScene())
            
        # if help button is pressed, goto game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
        # if credits button is pressed, goto game scene
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditsScene())
        
        # if setting button is pressed, goto game scene
        if self.settings_button.frame.contains_point(touch.location):
            self.present_modal_scene(SettingScene())
        
        # if bonus button is pressed, goto game scene
        if self.bonus_button.frame.contains_point(touch.location):
            self.present_modal_scene(BonusScene())
        
        # if pause button is pressed, goto pause scene
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(PauseScene())
    
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
    
