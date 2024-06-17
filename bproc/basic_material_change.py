import blenderproc as bproc
import bpy
import random
import numpy as np
import imageio
import os


def load_material(material_name):
    # Load the material
    material = bpy.data.materials.get(material_name)
    if material is None:
        raise ValueError("Material not found")

    return material

def write_output_image(current_dir, data):
    # Write the data into a .png file using ImageIO
    img_array = data["colors"][0]
    output_file = current_dir + r"\output_imgs\000001.png"  # Replace with a counter
    imageio.imwrite(output_file, img_array)

    print(f"Image saved to {output_file}")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize BlenderProc
bproc.init()

# Load the .blend file containing the sample object (Monkey.obj)
obj = bproc.loader.load_obj(current_dir + r"\Raw_objects\Monkey.obj")
obj = obj[0]

obj.set_location([0, 1, 0])
obj.set_rotation_euler([np.pi/2, 0, 0])

# Load the material
loaded_material = load_material("CeramicPlainWhite001")
# apply the material to the mesh object
if obj is not None and obj.type == 'MESH':
    if obj.data.materials:
        obj.data.materials[0] = loaded_material
    else:
        obj.data.materials.append(loaded_material)

# Set the output resolution
bproc.camera.set_resolution(512, 512)

# Create a point light next to it
light = bproc.types.Light()
light.set_location([2, -2, 0])
light.set_energy(300)

# Set the camera
cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
bproc.camera.add_camera_pose(cam_pose)

# Render the scene
data = bproc.renderer.render()

# Guardamos la imagen png de los datos renderizados
write_output_image(current_dir, data)


def partially_clean_the_scene():
    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()

    # make sure we remove data that was connected to the objects we just deleted
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

