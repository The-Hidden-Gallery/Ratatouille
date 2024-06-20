"""
File to create a data sampler for the BProc project.
It creates samples of positions, scales and rotations for the objects in the scene.
It then attributes these samples a True or False label, depending on rules set by the user.
This csv file can be imported in the blenderproc project to generate the images and attribute the labels accordingly
"""

import random 
import numpy as np
import pandas as pd

# Constants
N_SAMPLES = 100
TABLE_COLORS = 20
PLATE_TEXTURES = 4
PLATE_TYPES = 11
LIMITS_CAMERA_POS_XY = [15,40]
LIMITS_CAMERA_POS_Z = [15,40]
LIMITS_CAMERA_ROT_X = [-1,1]
LIMITS_CAMERA_ROT_Y = [-1,1]
LIMITS_CAMERA_ROT_Z = [-1,1]
# Create a csv file with the following columns: 
# - Table_color_n, where n is the index of the table color in the color list
# - Plate_texture_n, where n is the index of the plate texture in the texture list
# - Plate_type_n, where n is the index of the plate type in the type list
# - Camera_pos, a list of 3 values representing the camera position
# - Camera_rot, a list of 3 values representing the camera rotation
# - Light_pos, a list of 3 values representing the light position
# - Light_energy, a value representing the light energy

def assign_label(worldinfo: dict):
    """
    Assigns a label to the sample based on the positions, rotations and scales of the objects in the scene

    Args: 
        worldinfo: dictionary with the information of the objects in the scene

    Returns:
        Label: True if the sample is valid, False otherwise
        Reason: The reason why the sample is invalid
    """

dataset = pd.DataFrame(columns=["Table_color", "Plate_texture", "Plate_type", "Camera_pos", "Camera_rot", "Light_pos", "Light_energy", "Label"])

for i in range(N_SAMPLES):
    # Table
    table_color = random.randint(0, TABLE_COLORS-1)
    # Plate
    plate_texture = random.randint(0, PLATE_TEXTURES-1)
    plate_type = random.randint(0, PLATE_TYPES-1)
    # Camera
    camera_pos = [random.uniform(LIMITS_CAMERA_POS_XY[0], LIMITS_CAMERA_POS_XY[1]),
                random.uniform(LIMITS_CAMERA_POS_XY[0], LIMITS_CAMERA_POS_XY[1]),
                random.uniform(LIMITS_CAMERA_POS_Z[0], LIMITS_CAMERA_POS_Z[1])]
    camera_rot = [random.uniform(LIMITS_CAMERA_ROT_X[0], LIMITS_CAMERA_ROT_X[1]),
                random.uniform(LIMITS_CAMERA_ROT_Y[0], LIMITS_CAMERA_ROT_Y[1]), 
                random.uniform(LIMITS_CAMERA_ROT_Z[0], LIMITS_CAMERA_ROT_Z[1])]
    # Light
    light_pos = [random.random()*10, random.random()*10, random.random()*10]
    light_energy = random.random()*100


    worldinfo = {}
    # Aqui se escogen las posiciones, rotaciones y escalas de los objetos en la escena y en función a eso se le asigna un label
    label, reason = assign_label(worldinfo)

    label = random.choice([True, False])

    dataset = dataset.append({"Table_color": table_color, "Plate_texture": plate_texture, "Plate_type": plate_type, "Camera_pos": camera_pos, "Camera_rot": camera_rot, "Light_pos": light_pos, "Light_energy": light_energy, "Label": label}, ignore_index=True)
