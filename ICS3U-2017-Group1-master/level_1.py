# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows level 1 scene

from scene import *
from levels_list_scene import *
from game_over_scene import *
from level_completed_scene import *

import ui
import config
import sound
import time
from numpy import random

class Level1Scene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.algebra = []
        self.small_blobs = []
        self.small_blob_create_rate = 1
        self.jump_button_down = False
        self.squareman_move_speed = 10.0
        self.small_blob_speed = 12.0
        self.attack_counter = 0
        self.shoot_button_pressed = time.time()
        self.shoot_button_enabled = True
        self.jump_button_time = time.time()
        self.squareman_jump = False
        
        
        #self.game_over = False
        
        # music is played or not
        # you can turn on/off the music in setting scene
        #if config.music_on == True:
           #config.main_game_music.number_of_loops = -1
           #config.main_game_music.play()
        #elif config.music_on == False:
           #config.main_game_music.pause()
        
        # add background color
        self.background = SpriteNode('./assets/sprites/background_standard.png',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        home_button_position = Vector2()
        home_button_position.x = self.screen_center_x + 440
        home_button_position.y = self.screen_center_y + 310
        self.home_button = SpriteNode('./assets/sprites/main_menu_simple_button.png',
                                            parent = self,
                                            position = home_button_position,
                                            scale = 0.4)    
                                       
        health_bar_1_position = Vector2()
        health_bar_1_position.x = self.screen_center_x - 440
        health_bar_1_position.y = self.screen_center_y + 320
        self.health_bar_1 = SpriteNode('./assets/sprites/heart_sprite.png',
                                       parent = self,
                                       position = health_bar_1_position,
                                       scale = 2.0)
        self.add_child(self.health_bar_1)
        
        health_bar_2_position = Vector2()
        health_bar_2_position.x = self.screen_center_x - 375
        health_bar_2_position.y = self.screen_center_y + 320
        self.health_bar_2 = SpriteNode('./assets/sprites/heart_sprite.png',
                                       parent = self,
                                       position = health_bar_2_position,
                                       scale = 2.0)
        self.add_child(self.health_bar_2)
        
        health_bar_3_position = Vector2()
        health_bar_3_position.x = self.screen_center_x - 310
        health_bar_3_position.y = self.screen_center_y + 320
        self.health_bar_3 = SpriteNode('./assets/sprites/heart_sprite.png',
                                       parent = self,
                                       position = health_bar_3_position,
                                       scale = 2.0)
        self.add_child(self.health_bar_3)
        
        # squareman
        self.squareman_choice = self.skin_file(config.skin_settings)
        squareman_position = Vector2()
        squareman_position.x = self.screen_center_x - 440
        squareman_position.y = self.screen_center_y - 25
        self.squareman = SpriteNode('./assets/sprites/' + self.squareman_choice + '.png',
                                    parent = self,
                                    position = squareman_position,
                                    scale = 0.8)
     
        # main blob
        blob_position = Vector2()
        blob_position.x = self.screen_center_x + 380
        blob_position.y = self.screen_center_y + 40
        self.blob = SpriteNode('./assets/sprites/blob.png',
                                    parent = self,
                                    position = blob_position,
                                    scale = 1.0)
                                    
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
                                    
        score_label_position = Vector2()
        score_label_position.x = self.screen_center_x + 280
        score_label_position.y = self.screen_center_y + 320
        self.score_label = LabelNode(text = "SCORE: 0",
                                     font = ('Menlo-Bold', 36),
                                     color = 'white',
                                     parent = self,
                                     position = score_label_position)                            
                                    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if config.retry == True:
            self.setup()
            config.retry = False
        
        # check if game is over to play game over sound
        #if config.game_over == True:
        	 #config.main_menu_music.pause()
        
        # check if game is over
        if config.pressed_home == True or config.game_over == True:
            self.dismiss_modal_scene()
        
        # check every update if a algebra line is off the screen
        for algebra_line in self.algebra:
            if algebra_line.position.x > self.size_of_screen_x - 5:
                algebra_line.remove_from_parent()
                self.algebra.remove(algebra_line)
        
        # check every update if a new small blob should be created
        small_blob_create_chance = random.randint(1, 50)
        if small_blob_create_chance <= self.small_blob_create_rate:
            self.create_small_blob()
        
        # check if any small blob is off the screen and delete
        for small_blob in self.small_blobs:
            if small_blob.position.x < 1:
                small_blob.remove_from_parent()
                self.small_blobs.remove(small_blob)
                
        # squareman jumps if jump button is down
        if self.jump_button_down == True:
            # move up squareman
            self.squareman.run_action(Action.move_by(0.0, self.squareman_move_speed, 0.1))
        
        
        
        
        if self.jump_button_down == False:
            # move down squareman
            #self.squareman.run_action(Action.move_by(0.0, -1self.squareman_move_speed, 0.1))
            
            #squareman_start_position = Vector2()
            #squareman_start_position.x = self.squareman.position.x
            #squareman_start_position.y = self.squareman.position.y
        
            squareman_end_position = Vector2()
            squareman_end_position.x = self.screen_center_x - 440
            squareman_end_position.y = self.screen_center_y - 25
            squaremanMoveAction = Action.move_to(squareman_end_position.x, squareman_end_position.y)
            self.squareman.run_action(squaremanMoveAction)
        
        # check if algebra line hits an blob and remove it
        if len(self.algebra) > 0:
           for algebra_line in self.algebra:
               if algebra_line.frame.intersects(self.blob.frame):
                   algebra_line.remove_from_parent()
                   self.algebra.remove(algebra_line)
                   config.score = config.score + 1
                   config.blob_hit = config.blob_hit + 1
        
        # check every update to see if a algebra has touched a small blob
        if len(self.small_blobs) > 0 and len(self.algebra) > 0:
            for small_blob in self.small_blobs:
                for algebra_line in self.algebra:
                    if small_blob.frame.contains_rect(algebra_line.frame):
                        algebra_line.remove_from_parent()
                        self.algebra.remove(algebra_line)
                        small_blob.remove_from_parent()
                        self.small_blobs.remove(small_blob)
                  
        # check if small blob hits squareman and remove it
        if len(self.small_blobs) > 0:
           for small_blob in self.small_blobs:
               if small_blob.frame.intersects(self.squareman.frame):
                   small_blob.remove_from_parent()
                   self.small_blobs.remove(small_blob)
                   config.squareman_hit = config.squareman_hit + 1
               
        # check if blob was hit ten times
        if config.blob_hit == 10:
            self.blob.remove_from_parent()
            self.present_modal_scene(LevelCompletedScene())
                             
        # update score
        self.score_label.text = "SCORE: " + str(config.score)
        
        # remove heart if squareman is hit
        # check if squareman is hit three times, if so move to game over scene
        if config.squareman_hit == 1:
            self.health_bar_3.remove_from_parent()
        if config.squareman_hit == 2:
            self.health_bar_2.remove_from_parent()
        if config.squareman_hit == 3:
            self.health_bar_1.remove_from_parent()
            self.squareman.remove_from_parent()
            self.present_modal_scene(GameOverScene())
        
        if time.time() - self.shoot_button_pressed > 0.5:
            self.shoot_button_enabled = True
            self.squareman_back()
        
        
        
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if jump button is down
        if self.jump_button.frame.contains_point(touch.location):
            self.jump_button_down = True
            self.jump_button_time = time.time()
        
        # check if shoot button is down
        if self.shoot_button.frame.contains_point(touch.location) and self.shoot_button_enabled == True:
            self.create_new_algebra_line()
            
            
            
            self.shoot_button_enabled = False
            self.shoot_button_pressed = time.time()
            
            
            self.squareman.remove_from_parent()
            
            self.squareman_attack()
            #self.squareman_removed = True
            #self.squareman.remove_from_parent()
            
            #self.squareman_back()
            
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.home_button.frame.contains_point(touch.location):
            config.pressed_home = True
            
        
            
        if self.jump_button.frame.contains_point(touch.location):
            self.jump_button_down = False
        
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
    
    def squareman_attack(self):
        # when the shoot button is pressed, squareman changes its gesture
        
        self.squareman_choice = self.skin_file(config.skin_settings)
        squareman_attack_image_position = Vector2()
        squareman_attack_image_position.x = self.squareman.position.x
        squareman_attack_image_position.y = self.squareman.position.y
        
        self.squareman = SpriteNode('./assets/sprites/' + self.squareman_choice + '_attack.png',
                                                 parent = self,
                                                 position = squareman_attack_image_position,
                                                 scale = 0.8)
        #self.squareman_attack_image.remove_from_parent()
    
    def squareman_back(self):
        # when the user releases fingers from shoot button, original squareman occurs
        
        self.squareman_choice = self.skin_file(config.skin_settings)
        squareman_position = Vector2()
        squareman_position.x = self.screen_center_x - 440
        squareman_position.y = self.screen_center_y - 25
        self.squareman.remove_from_parent()
        
        self.squareman = SpriteNode('./assets/sprites/' + self.squareman_choice + '.png',
                                    parent = self,
                                    position = squareman_position,
                                    scale = 0.8)
        
    def create_new_algebra_line(self):
        # when the user hits the shoot button, a new line of algebra will be made
        
        algebra_line_start_position = Vector2()
        algebra_line_start_position.x = self.squareman.position.x + 100
        algebra_line_start_position.y = self.squareman.position.y + 20
        
        algebra_line_end_position = Vector2()
        algebra_line_end_position.x = self.size_of_screen_x + 100
        algebra_line_end_position.y = algebra_line_start_position.y
        
        self.algebra.append(SpriteNode('./assets/sprites/algebra.png',
                             position = algebra_line_start_position,
                             parent = self,
                             scale = 0.5))
                             
        # make algebra line move forward
        algebraLineMoveAction = Action.move_to(algebra_line_end_position.x,
                                           algebra_line_end_position.y,
                                           7.0)
        self.algebra[len(self.algebra)-1].run_action(algebraLineMoveAction)
        
    def create_small_blob(self):
        # creates small blobs to move across screen
        # from right side to left side
        
        small_blob_start_position = Vector2()
        small_blob_start_position.x = self.blob.position.x - 50
        small_blob_start_position.y = random.randint(self.screen_center_y, self.screen_center_y + 320)
        
        small_blob_end_position = Vector2()
        small_blob_end_position.x = 0
        small_blob_end_position.y = small_blob_start_position.y
        
        # 
        self.small_blobs.append(SpriteNode('./assets/sprites/blob.png',
                               position = small_blob_start_position,
                               parent = self,
                               scale = 0.2))
        
        # make small blobs move to squareman
        small_blobMoveAction = Action.move_to(small_blob_end_position.x, 
                                         small_blob_end_position.y, 
                                         self.small_blob_speed,
                                         TIMING_SINODIAL)
        self.small_blobs[len(self.small_blobs)-1].run_action(small_blobMoveAction)
        
    def skin_file(self, squareman_choice):
        # chooses which squareman to display
        
        the_skin_file = ' '
        if squareman_choice == 'original':
            the_skin_file = 'skins/original'
        elif squareman_choice == 'flashback':
            the_skin_file = 'skins/flashback'
        elif squareman_choice == 'poker':
            the_skin_file = 'skins/poker'
        elif squareman_choice == 'panda':
            the_skin_file = 'skins/panda'
            
        return the_skin_file
