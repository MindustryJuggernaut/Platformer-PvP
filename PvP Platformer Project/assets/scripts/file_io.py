from json import dump as json_dump, load as json_load


def load_file_data(file_path):
    with open(file_path, "r") as opened_file:
        return json_load(opened_file)

# Will overwrite data
def save_file_data(file_path, data_to_save):
    with open(file_path, "w") as save_file:
        json_dump(data_to_save, save_file)

# save_file_data("animations/player/idle/config.json", {"frame_durations_list": [5, 2, 2, 2], "colorkey": (127, 127, 127)})