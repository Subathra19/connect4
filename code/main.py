import pygame

from player import Player
from board import Board

class Game_Screen:
    def __init__(self, player):
        self.chip_size = 80
        self.offset = 60
        self.chip_offset = 20
        self.board_height = 600
        self.chip_radius=int(self.chip_size/2)

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Connect 4")


        self.screen_width=800
        self.screen_height=700
        self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))
        self.board_image=pygame.image.load("images/board.png")
        self.board_image_numbers=pygame.image.load("images/board_numbers.png")
        self.font=pygame.font.SysFont("Calibri",26)

        self.initialize_screen(player)
        
    def initialize_screen(self,player):
        self.screen.fill((255,255,255))

        pygame.display.update()

        self.draw_board()
        self.draw_player(player)  
    
    def draw_board(self, player=None, row=-1, column=-1):
        if player is not None:
            pygame.draw.circle(self.screen, player.get_color(),
             (self.offset + self.chip_radius + self.chip_offset * column + self.chip_size * column, 
             self.board_height - self.chip_size * row - self.chip_offset * row), self.chip_radius)

        self.screen.blit(self.board_image, (self.offset-10, self.offset-10))
        self.screen.blit(self.board_image_numbers, (self.offset+self.chip_radius-10, self.offset+self.board_height-5))

        pygame.display.update()

    def draw_player(self,player):
        pygame.draw.rect(self.screen, (255,255,255), [0, 0, 800, 50], 0)

        text = "Current Player: " + player.get_name()
        text = self.font.render(text, True, (0,0,0))
        self.screen.blit(text, (50, 10))

        pygame.display.update()
    
    def draw_player_won(self,player):
        pygame.draw.rect(self.screen, (255,255,255), [0, 0, 800, 50], 0)
        text = player.get_name() + " won! Restart (y | n)?"  
        text = self.font.render(text, True, (0,0,0))
        self.screen.blit(text, (50, 10))

        pygame.display.update()


class Game:
    def __init__(self):
        self.current_player=0
        self.players=[Player(0), Player(1)]
        self.board=Board()
        self.game_GUI=Game_Screen(self.players[0])
    
    def game_loop(self):
        keys=[1,2,3,4,5,6,7]

        update_screen=False
        player_won=False
        game_close=False

        row=-1
        column=-1

        while not game_close:
            update_screen=False

            # Check for the player's input
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_close=True
                elif event.type==pygame.KEYUP:
                    if player_won:
                        # To restart (i.e) press Y
                        if event.key==pygame.K_y:
                            player_won=False
                            game_close=False
                            self.restart()
                        elif event.key==pygame.K_n:
                            game_close=True
                    else:
                        # Insert a chip to a column
                        column=event.key-49
                        if column+1 in keys:
                            row=self.add_chip(column)

                            if row>-1:
                                player_won=self.check_winning(self.players[self.current_player])
                                update_screen=True
                
                # Update the GUI screen
                if update_screen:
                    self.game_GUI.draw_board(self.players[self.current_player],row,column)

                    if player_won:
                        self.game_GUI.draw_player_won(self.players[self.current_player])
                    else:
                        self.switch_player()
                        self.game_GUI.draw_player(self.players[self.current_player])

    def switch_player(self):
        self.current_player=self.current_player+1
        self.current_player=self.current_player%2
            
    def restart(self):
        self.board.clear()
        self.game_GUI.initialize_screen(self.players[self.current_player])
                
    def add_chip(self,column):
        player = self.players[self.current_player]
        return self.board.add_chip(player, column)
            
    def check_winning(self,player):
        return self.board.check_winning(player)
            
               

game = Game()
game.game_loop()
