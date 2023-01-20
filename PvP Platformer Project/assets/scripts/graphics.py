import pygame

from assets.scripts.file_io import load_file_data


def load_image(image_path, colorkey):
    loaded_image = pygame.image.load(image_path).convert()
    loaded_image.set_colorkey(colorkey)
    return loaded_image.copy()

def load_animation(folder_path):
    frames = []

    config_data = load_file_data(folder_path + "config.json")

    animation_name = folder_path.split("/")[-2]
    for frame_number, duration in enumerate(config_data["frame_durations_list"]):
        frame_image_path = folder_path + animation_name + "_" + str(frame_number) + ".png"
        frame_image = load_image(frame_image_path, config_data["colorkey"])
        for i in range(duration):
            frames.append(frame_image)
    return frames

# def load_animation_group(group_folder_path)

class Animation:
    def __init__(self, loaded_frames, all_in_sync):
        self.frames = loaded_frames

        self.all_synced = all_in_sync # All animations beinged played of the same class will be synced or unsynced
        self.active_animations = []

    def update_active_animations(self):
        for index, animation in sorted(enumerate(self.active_animations), reverse=True):
            animation[0] += 1
            if animation[0] > len(self.frames) - 1:
                animation[0] = 0

    def draw_active_animations(self, surface, offset):
        for animation in self.active_animations:
            surface.blit(self.frames[animation[0]], (animation[1][0] + offset[0], animation[1][1] + offset[1]))

# Cuts out a rectangular portion of a larger image
def extracted_image(image, x_topleft, y_topleft, cut_width, cut_height):
    image_copy = image.copy()
    image_copy.set_clip(pygame.Rect(x_topleft, y_topleft, cut_width, cut_height))
    extracted_image = image.subsurface(image_copy.get_clip())
    return extracted_image.copy()

def rgba_to_rgb(rgba_color):
    return (rgba_color[0], rgba_color[1], rgba_color[2])

def load_spritesheet(spritesheet_path, colorkey):
    extracted_images = []
    rows = []
    spritesheet_image = load_image(spritesheet_path, None)
    for y in range(spritesheet_image.get_height()):
        pixel_color = rgba_to_rgb(spritesheet_image.get_at((0, y)))
        if pixel_color == (255, 0, 255):
            rows.append(y)

    for row in rows:
        row_extracted_images = []
        for x in range(spritesheet_image.get_width()):
            pixel_color = rgba_to_rgb(spritesheet_image.get_at((x, row)))
            if pixel_color == (255, 0, 255):

                extracted_image_width = 0
                while True:
                    extracted_image_width += 1
                    pixel_color = rgba_to_rgb(spritesheet_image.get_at((x + extracted_image_width, row)))
                    if pixel_color == (0, 255, 255):
                        break

                extracted_image_height = 0
                while True:
                    extracted_image_height += 1
                    pixel_color = rgba_to_rgb(spritesheet_image.get_at((x, row + extracted_image_height)))
                    if pixel_color == (0, 255, 255):
                        break

                extracted_image = extracted_image(spritesheet_image, x + 1, row + 1, extracted_image_width - 1, extracted_image_height - 1)
                extracted_image.set_colorkey(colorkey)
                row_extracted_images.append(extracted_image)
        extracted_images.append(row_extracted_images)
    return extracted_images