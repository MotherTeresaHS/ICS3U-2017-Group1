# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows level 1 scene

from scene import *
from pause_scene import *
from levels_list_scene import *
import ui


class Level1Scene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.algebra = []
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        pause_button_position = Vector2()  
        pause_button_position.x = self.screen_center_x + 440
        pause_button_position.y = self.screen_center_y + 320                          
        self.pause_button = SpriteNode('./assets/sprites/pause_button.png',
                                       parent = self,
                                       position = pause_button_position,
                                       scale = 0.8)
                                       
        health_bar_1_position = Vector2()
        health_bar_1_position.x = self.screen_center_x - 440
        health_bar_1_position.y = self.screen_center_y + 320
        self.health_1 = SpriteNode('./assets/sprites/heart_sprite.png',
                                   parent = self,
                                   position = health_bar_1_position,
                                   scale = 0.05)
                                   
        health_bar_2_position = Vector2()
        health_bar_2_position.x = self.screen_center_x - 375
        health_bar_2_position.y = self.screen_center_y + 320
        self.health_2 = SpriteNode('./assets/sprites/heart_sprite.png',
                                   parent = self,
                                   position = health_bar_2_position,
                                   scale = 0.05)
                                   
        health_bar_3_position = Vector2()
        health_bar_3_position.x = self.screen_center_x - 310
        health_bar_3_position.y = self.screen_center_y + 320
        self.health_3 = SpriteNode('./assets/sprites/heart_sprite.png',
                                   parent = self,
                                   position = health_bar_3_position,
                                   scale = 0.05)
                                   
        squareman_position = Vector2()
        squareman_position.x = self.screen_center_x - 440
        squareman_position.y = self.screen_center_y 
        self.squaremam = SpriteNode('./assets/sprites/squareman.png',
                                    parent = self,
                                    position = squareman_position,
                                    scale = 0.8)
        blob_position = Vector2()
        blob_position.x = self.screen_center_x + 380
        blob_position.y = self.screen_center_y + 40
        self.blob = SpriteNode('./assets/sprites/blob.PNG',
                                    parent = self,
                                    position = blob_position,
                                    scale = 0.15)
                                    
        shoot_button_position = Vector2()
        shoot_button_position.x = self.screen_center_x - 410
        shoot_button_position.y = self.screen_center_y - 280
        self.shoot_button = SpriteNode('./assets/sprites/shoot_button.png',
                                    parent = self,
                                    position = shoot_button_position,
                                    scale = 0.7)
                                    
        jump_button_position = Vector2()
        jump_button_position.x = self.screen_center_x + 410
        jump_button_position.y = self.screen_center_y - 280
        self.jump_button = SpriteNode('./assets/sprites/jump_button.png',
                                    parent = self,
                                    position = jump_button_position,
                                    scale = 0.7)
                                    
        special_button_position = Vector2()
        special_button_position.x = self.screen_center_x + 240
        special_button_position.y = self.screen_center_y - 280
        self.special_button = SpriteNode('./assets/sprites/special_button.png',
                                    parent = self,
                                    position = special_button_position,
                                    scale = 0.7)
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        # for algebra_line in self.algebra:
            #if algebra_line.position.y > self.size_of_screen_y + 50:
                #algebra_line.remove_from_parent()
                #self.algebra.remove(algebra_line)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(PauseScene())
            
        #if self.shoot_button.frame.contains_point(touch.location):
            #self.create_new_algebra_line()
    
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
    
    def create_new_algebra_line(self):
        pass
        # when the user hits the shoot button, a new line of algebra will be made
        #algebra_line_start_position = Vector2()
        #algebra_line_position.x = 100
        #algebra_line_position.y = self.squaremam.position.y
        
        #algebra_line_position = Vector2()
        #algebra_line_position.x = missile_start_position.x
        #algebra_line_position.y = self.size_of_screen_y + 100
        
        #self.algebra.append(SpriteNode('./assets/sprites/algebra_line.png',
                             #position = algebra_line_start_position,
                             #parent = self))
                             
        # make algebra line move forward
        #algebraLineMoveAction = Action.move_to(algebra_line_end_position.x,
                                           #algebra_line_end_position.y + 100,
                                           #5.0)
        #self.algebra[len(self.algebra)-1].run_action(algebraLineMoveAction)
        
