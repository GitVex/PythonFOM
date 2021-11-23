def hex_to_rgb(col_list):
    width = [i for i in range(0, 7, 2)]
    return [tuple([int(col_list[sub][width[a]:width[a + 1]], 16) for a in range(len(width) - 1)]) for sub in
            range(len(col_list))]

def hex_to_rgb1(col_list):
    width = [i for i in range(0, 7, 2)]
    return [tuple([round((int(col_list[sub][width[a]:width[a + 1]], 16)/255), 2) for a in range(len(width) - 1)]) for sub in
            range(len(col_list))]

def rgb_to_hex(col_list):
    return ["".join([hex(rgb_num)[2:].upper() for rgb_num in sub]) for sub in col_list]


def __init__(self, name):
    self.name = name
