from random import randint
import pygame
import sys
import numpy

class Game:
    
    width = height = 800
    size = 79
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    first_generation = []
    first_generation = []
    
    start = True
    game_play = False
    
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.surface.fill(self.black)
        pygame.display.set_caption("Game life")

        self._fps = 10
        self._clock = pygame.time.Clock()
        
        self._matrix = numpy.zeros((80, 80), dtype=int)
        
    def draw(self):
        sz = 10
        for y in range(self.size):
            for x in range(self.size):
                if self._matrix[y][x] == 1:
                    pygame.draw.rect(self.surface, (255, 255, 255), [x  * sz, y * sz, sz, sz])
                    
                
    def cheakArround(self, x: int, y: int):
        neighbours = 0
        cors = [[y - 1, x], [y - 1, x + 1], [y, x + 1], [y + 1, x + 1], 
                [ y + 1, x], [y + 1, x - 1], [y, x - 1], [y - 1, x - 1]]
        
        for cor in cors:
            try:
                if self._matrix[cor[0]][cor[1]]:
                    neighbours += 1
            except IndexError:
                pass
                
        return neighbours
    
    def createFutureGeneration(self):
        future_generation = []

        for y in range(self.size):
            for x in range(self.size):
                if self.cheakArround(x, y) == 3 and self._matrix[y][x] == 0:
                    future_generation.append((y, x, 1))
                elif 2 <= self.cheakArround(x, y) <= 3 and self._matrix[y][x] == 1:
                    future_generation.append((y, x, 1))
                else:
                    future_generation.append((y, x, 0))
                    
        return future_generation
    
    def move(self):
        future_generation = self.createFutureGeneration()
                                            
        for cors in future_generation:
            self._matrix[cors[0]][cors[1]] = cors[2]
    
    def main(self):

        while True:
            
            while self.start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            for cor in self.first_generation:
                                self._matrix[cor[0]][cor[1]] = 1
                            self.start = False
                            self.game_play = True
                            break
                        if event.key == pygame.K_r:
                            self.first_generation = [(randint(0, 79), randint(0, 79)) for i in range(1000)]
                            for cor in self.first_generation:
                                self._matrix[cor[0]][cor[1]] = 1
                            

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]//10
                    y = pos[1]//10
                    pygame.draw.rect(self.surface, (255, 255, 255), [x  * 10, y * 10, 10, 10])
                    self.first_generation.append((y, x))
                    
                self.draw()
                pygame.display.flip()
                
            
            while self.game_play:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self._fps += 2
                    if event.key == pygame.K_DOWN:
                        if self._fps > 2:
                            self._fps -= 2
                   
                self.draw()
                self.move()
                
                pygame.display.flip()
                self._clock.tick(self._fps) 
                self.surface.fill(self.black)
                    
game = Game()
game.main()