from pygame import Rect as pygame_rect
from math import cos, sin


class Projectile:
    def __init__(self, location, angle_radians, damage, speed_pixels, weight):
        self.location = location
        self.direction = angle_radians
        self.velocity = [cos(angle_radians) * speed_pixels, sin(angle_radians) * speed_pixels]

        self.damage = damage
        self.speed = speed_pixels
        self.weight = weight
        self.alive = True

class Arrow(Projectile):
    def __init__(self, location, angle_radians):
        super().__init__(location, angle_radians, 15, 10, 1)

        self.collision_point = None #I dont want to repeat self.collision_point = [cos(angle_radians) * 10 + location[0], sin(angle_radians) * 10 + location[1]]

    def update(self, collidable_objects, despawn_limits):
        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]
        self.velocity[1] += self.weight
        self.collision_point = [cos(angle_radians) * 10 + location[0], sin(angle_radians) * 10 + location[1]]

        if (self.collision_point[0] < despawn_limits[0][0] or self.collision_point[0] > despawn_limits[0][1]
            or self.collision_point[1] < despawn_limits[1][0] or self.collision_point[1] > despawn_limits[1][1]):
            self.alive = False

        for collidable in collidable_objects:
            if collidable.collidepoint(self.collision_point):
                self.alive = False
                break


class Bullet(Projectile):
    def __init__(self, location, angle_radians):
        super().__init__(location, angle_radians, 34, 20, 0)

        self.size = (6, 3)
        self.collision_box = pygame_rect(location[0], location[1], self.size[0], self.size[1])

    def update(self, collidable_objects, despawn_limits):
        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]
        self.collision_box.x = int(self.location[0])
        self.collision_box.y = int(self.location[1])

        if (self.collision_box.right < despawn_limits[0][0] or self.collision_box.left > despawn_limits[0][1]
        or self.collision_box.bottom < despawn_limits[1][0] or self.collision_box.top > despawn_limits[1][1]):

            self.alive = False

        for collidable in collidable_objects:
            if collidable.colliderect(self.collision_box) or collidable.colliderect.contains(self.collision_box):
                self.alive = False
                break

