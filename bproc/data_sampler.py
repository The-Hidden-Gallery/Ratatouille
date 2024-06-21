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
N_SAMPLES = 10
TABLE_COLORS = 20
PLATE_TEXTURES = 4
PLATE_TYPES = 11
LIMITS_CAMERA_POS_XY = [15,40]
LIMITS_CAMERA_POS_Z = [15,40]
LIMITS_CAMERA_ROT_X = [-1,1]
LIMITS_CAMERA_ROT_Y = [-1,1]
LIMITS_CAMERA_ROT_Z = [-1,1]

# Every ingredient must have a list of constraints in order to be valid in the scene
# The constraints are the following:
# - The ingredient must be in the scene
# - The ingredient must be in the correct position ( bounding box given by max and min values)
# - The ingredient must be in the correct rotation ( bounding box given by max and min values)
# - The ingredient must be in the correct scale ( bounding box given by max and min values)
# - The ingredient must be in the correct material ( pending )
INGREDIENTS = {
    "A": {"position": [[0, 0, 0], [20, 20, 20]], "rotation": [[0, 0, 0], [75, 75, 75]], "scale": [[1, 1, 1], [10, 10, 10]]},
    "B": {"position": [[3, 3, 3], [50, 50, 50]], "rotation": [[0, 0, 0], [75, 75, 75]], "scale": [[1, 1, 1], [10, 10, 10]]},
    "C": {"position": [[3, 3, 3], [80, 80, 80]], "rotation": [[0, 0, 0], [75, 75, 75]], "scale": [[1, 1, 1], [10, 10, 10]]},
    "D": {"position": [[4, 1, 2], [10, 10, 10]], "rotation": [[0, 0, 0], [75, 75, 75]], "scale": [[1, 1, 1], [10, 10, 10]]},
}
INGREDIENT_POSIBILITIES ={
    "position": [[0, 0, 0], [10, 10, 10]],
    "rotation": [[0, 0, 0], [90, 90, 90]],
    "scale": [[1, 1, 1], [6, 6, 6]]
}

# There also exists a reason to number dictionary that will be used to explain why a sample is invalid, this should be consistent 
# with the constraints given in the INGREDIENTS dictionary 

REASON_TO_NUMBER = {
    1: "Ingredient not in scene",
    2: "Ingredient not in correct position",
    3: "Ingredient not in correct rotation",
    4: "Ingredient not in correct scale",
}

# Create a csv file with the following columns: 
# - Table_color_n, where n is the index of the table color in the color list
# - Plate_texture_n, where n is the index of the plate texture in the texture list
# - Plate_type_n, where n is the index of the plate type in the type list
# - Camera_pos, a list of 3 values representing the camera position
# - Camera_rot, a list of 3 values representing the camera rotation
# - Light_pos, a list of 3 values representing the light position
# - Light_energy, a value representing the light energy

def assign_label(worldinfo: dict) -> tuple[bool, list[int]]:
    """
    Assigns a label to the sample based on the positions, rotations and scales of the objects in the scene

    Args: 
        worldinfo: dictionary with the information of the objects in the scene

    Returns:
        label: True if the sample is valid, False otherwise
        reason: The reason why the sample is invalid
    """
    reason = []
    label = True
    for ingredient in INGREDIENTS.keys():
        ingredient_reason = []
        # Check if the ingredient is in the scene
        if ingredient not in worldinfo.keys():
            label = False
            ingredient_reason.append(1)
        else:
            # Check if the ingredient is in the correct position
            if not INGREDIENTS[ingredient]["position"][0] <= worldinfo[ingredient]["position"] <= INGREDIENTS[ingredient]["position"][1]:
                label = False
                ingredient_reason.append(2)
            # Check if the ingredient is in the correct rotation
            if not INGREDIENTS[ingredient]["rotation"][0] <= worldinfo[ingredient]["rotation"] <= INGREDIENTS[ingredient]["rotation"][1]:
                label = False
                ingredient_reason.append(3)
            # Check if the ingredient is in the correct scale
            if not INGREDIENTS[ingredient]["scale"][0] <= worldinfo[ingredient]["scale"] <= INGREDIENTS[ingredient]["scale"][1]:
                label = False
                ingredient_reason.append(4)
        reason.append(ingredient_reason)
    return label, reason



dataset = pd.DataFrame(columns=["Sample_number", "Table_color", "Plate_texture", "Plate_type", "Camera_pos", "Camera_rot", "Light_pos", "Light_energy", "World_info", "Label", "Reason"])

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
    for ingredient in INGREDIENTS.keys():
        ingredient_pos = [random.uniform(INGREDIENT_POSIBILITIES["position"][0][0], INGREDIENT_POSIBILITIES["position"][1][0]),
                        random.uniform(INGREDIENT_POSIBILITIES["position"][0][1], INGREDIENT_POSIBILITIES["position"][1][1]),
                        random.uniform(INGREDIENT_POSIBILITIES["position"][0][2], INGREDIENT_POSIBILITIES["position"][1][2])]
        ingredient_rot = [random.uniform(INGREDIENT_POSIBILITIES["rotation"][0][0], INGREDIENT_POSIBILITIES["rotation"][1][0]),
                        random.uniform(INGREDIENT_POSIBILITIES["rotation"][0][1], INGREDIENT_POSIBILITIES["rotation"][1][1]),
                        random.uniform(INGREDIENT_POSIBILITIES["rotation"][0][2], INGREDIENT_POSIBILITIES["rotation"][1][2])]
        ingredient_scale = [random.uniform(INGREDIENT_POSIBILITIES["scale"][0][0], INGREDIENT_POSIBILITIES["scale"][1][0]),
                        random.uniform(INGREDIENT_POSIBILITIES["scale"][0][1], INGREDIENT_POSIBILITIES["scale"][1][1]),
                        random.uniform(INGREDIENT_POSIBILITIES["scale"][0][2], INGREDIENT_POSIBILITIES["scale"][1][2])]
        worldinfo[ingredient] = {"position": ingredient_pos, "rotation": ingredient_rot, "scale": ingredient_scale}
    # Aqui se escogen las posiciones, rotaciones y escalas de los objetos en la escena y en función a eso se le asigna un label
    label, reason = assign_label(worldinfo)

    sample_data = {
    "Sample_number": i,
    "Table_color": table_color,
    "Plate_texture": plate_texture,
    "Plate_type": plate_type,
    "Camera_pos": camera_pos,
    "Camera_rot": camera_rot,
    "Light_pos": light_pos,
    "Light_energy": light_energy,
    "World_info": worldinfo,
    "Label": label,
    "Reason": reason
    }

    # Convert the dictionary to a DataFrame
    sample_df = pd.DataFrame([sample_data])

    # Concatenate the new DataFrame with the existing one
    dataset = pd.concat([dataset, sample_df], ignore_index=True)
dataset.to_csv("samples.csv", index=False)
print("Dataset created")
