import blenderproc as bproc
import bpy
import random
import pathlib
import addon_utils
import numpy as np
import imageio
import os
"""
Given that addon_utils is not a built-in module, this may not be able to run 
"""

def partially_clean_scene():
    """ 
    This function will remove all objects from the scene, but it will not remove the
    materials, textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

def enable_addon(addon_name):
    """ 
    This function will enable the addon with the given name if it is not already enabled
    """
    loaded_default, loaded_state = addon_utils.check(addon_name)

    if not loaded_state: 
        addon_utils.enable(addon_name)

def save_image(data, output_file):
    # Write the data into a .png file using ImageIO
    img_array = data["colors"][0]
    imageio.imwrite(output_file, img_array)

    print(f"Image saved to {output_file}")


def main(output_file):
    bproc.init()
    # May not be needed due to blenderproc
    # partially_clean_scene()

    # Set working directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = current_dir + output_file

    # May not be needee due to blenderproc
    addon_name = "io_import_images_as_planes"
    enable_addon(addon_name)
    
    # Insert the path to the image you want to import into a plane
    image_path = pathlib.Path.home() / "tmp" / "Arucos" / "aruco_3.png"
    print("image path", image_path)

    if image_path.exists():
        bpy.ops.import_image.to_plane(files=[{"name":str(image_path)}])
        print("Image imported")
        image = bpy.context.active_object
        image.location = (0, 0, 0)
        image.rotation_euler = (np.pi/2, 0, 0)
        new_table_color = bpy.data.materials.new("")
        new_table_color.diffuse_color = (random.random(),random.random(),random.random(),1)
        image.data.materials.append(new_table_color)
    else:
        print(f"Image not found at {image_path}")


    # Create a point light next to it
    light = bproc.types.Light()
    light.set_location([2, -2, 0])
    light.set_energy(300)


    # Set the camera and resolution
    bproc.camera.set_resolution(512, 512)
    cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
    bproc.camera.add_camera_pose(cam_pose)

    # Render the scene
    data = bproc.renderer.render()

    # Save the image
    save_image(data, output_file)

if __name__ == "__main__":
    output_file = r"\output_imgs\000021.png"
    main(output_file)