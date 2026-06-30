from ursina import *
from engine import start_voxel_grid  # Import your locked engine file

# Custom Voxel definition - easy to change colors/textures here!
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture='white_cube',
            color=color.green,
            origin_y=0.5
        )

# This is the "callback" function where you cook your world logic
def generate_world():
    size = 20
    for z in range(size):
        for x in range(size):
            Voxel(position=(x, 0, z))

# Launch the game using your engine file!
if __name__ == '__main__':
    start_voxel_grid(generate_world)
