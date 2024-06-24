import blenderproc as bproc
import bpy
import random
import numpy as np
import imageio
import os
# import pandas as pd
import argparse

CAMERA_RESOLUTION = (512, 512)


def parse_args() -> argparse.Namespace:
    """
    Function to parse the arguments from the command line

    Returns:
    argparse.Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('run', nargs='?', default="-1",
                         help="Run number to save the images in the same folder")
    parser.add_argument('output_dir', nargs='?', default="output_imgs/draft_1",
                         help="Path to where the final files, will be saved")
    return parser.parse_args()

# def load_samples(file_name: str = "samples.csv") -> pd.DataFrame:
#     """ 
#     This function will load the samples.csv file and return the data as a pandas DataFrame

#     Returns:
#     pd.DataFrame: The samples data
#     """
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     samples_file = current_dir + file_name
#     samples = pd.read_csv(samples_file)

#     return samples
def create_table() -> bpy.types.Object:
    """
    This function will create a table object in the scene
    """
    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD')
    table = bpy.context.active_object
    table.name = "Table"
    table_scale = (60, 60, 1)
    table.scale = table_scale

    return table


def generate_colors(n_colors: int = 20) -> np.ndarray:
    """
    This function will generate n_colors random colors and give them some reflectance properties
    
    Args:
    n_colors (int): The number of colors to generate
    
    Returns:
    np.ndarray: The generated colors
    """
    colors = []
    for i in range (0,n_colors):
        new_table_color = bpy.data.materials.new("")
        new_table_color.diffuse_color = (random.random(),random.random(),random.random(),1)
        new_table_color.use_nodes = True
        #new_table_color = bpy.ops.material.new()
        new_table_color.node_tree.nodes["Principled BSDF"].inputs["Metallic"].default_value = 0.1
        new_table_color.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.6
        new_table_color.node_tree.nodes["Principled BSDF"].inputs["Weight"].default_value = 0.3

        colors.append(new_table_color)

    return colors

def save_images(data:str, output_file:str = "output_imgs/", run:str = None) -> None:
    """
    Function to save the images in the data dictionary to the output_file as .png files

    Args:
    data (dict): The data dictionary containing the images
    output_file (str): The output file to save the images to
    run (str): A subfolder to save the images to (optional)

    Returns:
    None
    """
    
    if run != "-1": # If there is a run number other than the default selected, then we create a subfolder but 
        # we check if the folder already exists and ask the user if they want to overwrite it just in case it's a mistake 
        # We give them the chance to change the run number if they want to so as to not loose the time to run the script again correctly
        care = True
        while care: 
            try_file = output_file + f"/{run}"
            try:  
                os.mkdir(try_file)
                care = False
            except OSError as error:
                print(f"The folder {try_file} already exists and any data inside it might be overwritten.")
                confirmation = ""
                while confirmation.lower() not in ["y", "n"]:
                    confirmation = input("Type y to rewrite, n to choose a new folder (Y/N): ")
                if confirmation.lower() == "n":
                    run = input("Please enter a new RUN number: ")
                    print(run)
                else:
                    care = False
            pass
        output_file = output_file + f"/{run}"
    else: 
        try:  
            os.mkdir(output_file)
        except:
            pass
        
    img_array = data["colors"]
    output_file = output_file + '/'
    print(output_file)
    for i in range(len(img_array)):
        # Write the data into a .png file using ImageIO
        output_file_i = output_file + f"{i}.png"
        imageio.imwrite(output_file_i, img_array[i])

        print(f"Image saved to {output_file}")

def main():
    args = parse_args()
    bproc.init()

    # Cargamos los objetos para tenerlos en memoria y poder manipularlos
    # bproc.load_objects()

    # Create the 'table' and its colors
    colors = generate_colors(7)
    table = create_table()
    # Cargamos las muestras
    # samples = load_samples()

    # Por cada muestra se coloca el mundo como nos indica la muestra y se renderiza
    # Set working directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    object_file = r"\Raw_objects\Monkey.obj"

    # Load the .blend file containing the sample object (Monkey.obj)
    obj = bproc.loader.load_obj(current_dir + object_file)[0]
    obj.set_location([0, 0, 0])
    obj2 = bproc.loader.load_obj(current_dir + object_file)[0]
    obj2.set_location([0, 0, 0])
    obj.set_rotation_euler([np.pi/2, 0, 0])
    obj.set_rotation_euler([np.pi/2, 0, 0])

    # Create a point light next to it
    light = bproc.types.Light()
    light.set_type("SUN")
    light.set_location([350, -50, 0])
    light.set_energy(0.4)

    # Set the camera and resolution
    bproc.camera.set_resolution(512, 512)
    cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
    bproc.camera.add_camera_pose(cam_pose)
    
    # Find point of interest, all cam poses should look towards it
    poi = bproc.object.compute_poi([obj])
    # Sample five camera poses
    for i in range(2):
        # Sample random camera location above objects
        location = np.random.uniform([0, 0, 8], [10, 10, 12])
        # Compute rotation based on vector going from location towards poi
        rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot=np.random.uniform(-0.7854, 0.7854))
        # Add homog cam pose based on location an rotation
        cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
        bproc.camera.add_camera_pose(cam2world_matrix)
        obj.set_location([0, 0, i*0.5])

        

    table.data.materials[0] = colors[i]
    # Render the scene
    data = bproc.renderer.render()
    save_images(data, args.output_dir, args.run)


if __name__ == "__main__":
    main()