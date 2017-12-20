# Created by: Kay Lin
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the credits scene.

from scene import *
import ui

from main_menu_scene import *


class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        #self.coding = LabelNode(text = 'CODING: Kay Lin, Julie Nguyen',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)
                                
        #self.art = LabelNode(text = 'ART: Julie Nguyen',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)
                                
        #self.music = LabelNode(text = 'MUSIC: John Lupe Patraboy',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)
                                
        #self.school = LabelNode(text = 'SCHOOL: St. Mother Teresa High School',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)
                                
        #self.teacher = LabelNode(text = 'TEACHER: Patrick Coxall',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)                                                                                                                                                                    
                                      
        #self.thanks = LabelNode(text = 'SPECIAL THANKS TO John Nguyen, for creating and inspiring us with the orginal Squareman',
                                #font=('Helvetica', 20),
                                #parent = self,
                                #position = self.size / 2,
                                #scale = 0.75)                             
                                      
        #back_button_position = self.size
        #back_button_position.x = 100
        #back_button_position.y = back_button_position.y - 100
        #self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       #parent = self,
                                       #position = back_button_position)
        
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
    
