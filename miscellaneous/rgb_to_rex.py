def check_boundries(rgb):
    for val in rgb:
        if val == int:
            continue
        if val in range(0,256):
            continue
        else:
            raise ValueError


    return rgb

def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    rgb = check_boundries(rgb)
    (r,g,b) = (rgb[0], rgb[1], rgb[2])
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b).upper()