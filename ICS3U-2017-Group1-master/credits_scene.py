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
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2 
        self.scale_size = 0.5
        
        # add background color
        self.background = SpriteNode('./assets/sprites/background_standard.png',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        back_button_position = Vector2()
        back_button_position.x = self.screen_center_x - 440
        back_button_position.y = self.screen_center_y + 300                     
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.9)                       
        
        coding_label_position = Vector2()
        coding_label_position.x = self.screen_center_x - 370
        coding_label_position.y = self.screen_center_y + 230
        self.coding_label = LabelNode(text = "CODING",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = coding_label_position)
                                     
        art_label_position = Vector2()
        art_label_position.x = self.screen_center_x - 400
        art_label_position.y = self.screen_center_y + 50
        self.art_label = LabelNode(text = "ART",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = art_label_position)
        
        music_label_position = Vector2()
        music_label_position.x = self.screen_center_x - 370
        music_label_position.y = self.screen_center_y - 130
        self.music_label = LabelNode(text = "MUSIC",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = music_label_position)
        
        school_label_position = Vector2()
        school_label_position.x = self.screen_center_x + 130
        school_label_position.y = self.screen_center_y + 230
        self.school_label = LabelNode(text = "SCHOOL",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = school_label_position)
        
        teacher_label_position = Vector2()
        teacher_label_position.x = self.screen_center_x + 140
        teacher_label_position.y = self.screen_center_y + 50
        self.teacher_label = LabelNode(text = "TEACHER",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = teacher_label_position)
        
        kay_label_position = Vector2()
        kay_label_position.x = self.screen_center_x - 380
        kay_label_position.y = self.screen_center_y + 190
        self.kay_label = LabelNode(text = "Kay Lin",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = kay_label_position)
        
        julie_label_position = Vector2()
        julie_label_position.x = self.screen_center_x - 350
        julie_label_position.y = self.screen_center_y + 160
        self.julie_label = LabelNode(text = "Julie Nguyen",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = julie_label_position)
                                     
        julie_art_label_position = Vector2()
        julie_art_label_position.x = self.screen_center_x - 350
        julie_art_label_position.y = self.screen_center_y + 10
        self.julie_art_label = LabelNode(text = "Julie Nguyen",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = julie_art_label_position)
        
        john_label_position = Vector2()
        john_label_position.x = self.screen_center_x - 330
        john_label_position.y = self.screen_center_y - 170
        self.john_label = LabelNode(text = "John Patraboy",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = john_label_position)
    
        school_name_label_position = Vector2()
        school_name_label_position.x = self.screen_center_x + 280
        school_name_label_position.y = self.screen_center_y + 190
        self.school_name_label = LabelNode(text = "St. Mother Teresa High School",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = school_name_label_position)
    
        coxall_label_position = Vector2()
        coxall_label_position.x = self.screen_center_x + 170
        coxall_label_position.y = self.screen_center_y + 10
        self.coxall_label = LabelNode(text = "Patrick Coxall",
                                     font = ('Menlo', 24),
                                     color = 'white',
                                     parent = self,
                                     position = coxall_label_position)
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
        
        # if back button is pressed, goto game scene
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
    
