import pygame as pg

white = pg.Color(255, 255, 255)
black = pg.Color(0, 0, 0)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
brown = pg.Color(165, 42, 42)

screen_width = 400
screen_height = 400

pg.init()
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Snake')

run = True
while run:
    for event in pg.event.get():
        if event.tyoe = pg.QUIT:
            run = False
    wn.fill(black)
pg.quit()

class Food():
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 4
        self.color = red
        self.width = 10
        self.height = 10
    
    def draw_food(self, surface):
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        pf.draw.rect(surface, self.color, self.food)

    def is_eaten(self, head):
        return self.food.colliderect(head)

    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

class Player():
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 'stop'
        self.body = []
        self.head_color = green
        self.body_color = brown
    
    def draw_player(self, surface):
        self.seg = []
        self.head = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)
                self.seg.append(segment)

    def add_unit(self):
        if len(self.body) != 0:
            index = len(self.body)-1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x, y])
        else:
            self.body.append([1000, 1000])

    def is_collision(self):
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
        if self.y < 0 or self.y > screen_height - self.height or self.x < 0 or self.x > screen_width - self.width:
            return True
    
    def move(self):
        for index in range(len(self.body)-1, 0, -1):
            x = self.body[index-1][0]
            y = self.body[index-1][1]
            self.body[index] = [x, y]
        if len(self.body) > 0:
            self.body[0] = [self.x, self.y]
        if self.direction == 'up':
            self.y -= self.velocity
        if self.direction == 'down':
            self.y += self.velocity
        if self.direction == 'left':
            self.x -= self.velocity
        if self.direction == 'right':
            self.x += self.velocity  

    def change_direction(self, direction):
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        if self.direction != 'right' and direction == 'left':
            self.direction = 'left'
        if self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        if self.direction != 'left' and direction == 'right':
            self.direction = 'right'
