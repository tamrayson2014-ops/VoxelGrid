from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# 1. Initialize the Game Engine window
app = Ursina()

# 2. Define our custom Voxel class
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture='white_cube', # Uses Ursina's built-in block template
            color=color.green,
            origin_y=0.5
        )

# 3. Generate a flat 20x20 platform grid instantly
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

# 4. Drop in the First-Person Player Controller
# Move with W, A, S, D | Spacebar to jump | Mouse to look around freely
player = FirstPersonController()
player.y = 5  # Spawn the player slightly above the ground platform

# 5. Fire up the game window loop
app.run()
