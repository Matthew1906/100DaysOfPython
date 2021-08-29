# Import modules
from numpy import array, prod 
from matplotlib.colors import to_hex
from PIL import Image
from collections import Counter

# Create functions
def get_image(file_path:str):
    '''Return numpy array of the image'''
    return array(Image.open(file_path))

def find_top_colors(image:array):
    '''Extract top 10 colors from the image'''
    if len(image.shape)<=2:
        return False
    colors = map(tuple, image.reshape(prod(image.shape[:-1]),image.shape[-1]))
    return Counter(colors).most_common(10)

def rgb_to_hex(rgb:tuple):
    '''Converting rgb into hexcode format'''
    rgb = list(map(lambda x:x/255, rgb))
    return to_hex(rgb, keep_alpha=True).upper()

def reshape_colors(colors:list):
    '''Reshape the (rgb_tuple, count) into {hex_color:count}'''
    return {rgb_to_hex(color):count for color, count in colors}