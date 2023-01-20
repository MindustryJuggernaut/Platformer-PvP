from pygame import Rect as pygame_rect
from random import choice as random_choice


class Player:
    def __init__(self, location):
        self.location = location
        self.size = (12, 24)
        self.collision_box = pygame_rect(location[0], location[1], self.size[0], self.size[1])
        self.speed = 2
        self.last_moved_direction = random_choice((-1, 1)) # -1 is left, 1 is right
        self.velocity = [0, 0]
        self.gravity = 0

        self.health = 100
        self.inventory = []
        self.animation_state = "idle"
        self.frame = 0

    def get_collisions(self, collidable_objects):
        return [collidable for collidable in collidable_objects if collidable.colliderect(self.collision_box)]

    def move(self, collidable_objects):
        collision_types = {"left": False, "right": False, "top": False, "bottom": False}

        self.location[0] += self.velocity[0]
        self.collision_box.x = int(self.location[0])
        collisions = self.get_collisions(collidable_objects)
        for collidable in collisions:
            if self.velocity[0] > 0:
                collision_types["right"]= True
                self.collision_box.right = collidable.left
            elif self.velocity[0] < 0:
                collision_types["left"]= True
                self.collision_box.left = collidable.right

        self.location[1] += self.velocity[1]
        self.collision_box.y = int(self.location[1])
        collisions = self.get_collisions(collidable_objects)
        for collidable in collisions:
            if self.velocity[1] > 0:
                collision_types["bottom"]= True
                self.collision_box.bottom = collidable.top
            elif self.velocity[1] < 0:
                collision_types["top"]= True
                self.collision_box.top = collidable.bottom

        return collision_types
