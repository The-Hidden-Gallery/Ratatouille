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
    parser.add_argument('output_dir', nargs='?', default="output_imgs/draft_1",
                         help="Path to where the final files, will be saved")
    parser.add_argument('run', nargs='?', default="0",
                         help="Run number to save the images in the same folder")
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
    if run:
        output_file = output_file + f"/{run}"
        try:  
            os.mkdir(output_file)
        except OSError as error:
            print("The folder already exists and any data inside it might be overwritten.")
            confirmation = ""
            while confirmation.lower() not in ["y", "n"]:
                confirmation = input("Do you want to continue? (Y/N): ")
            if confirmation.lower() == "n":
                return
            pass
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

    # Cargamos las muestras
    # samples = load_samples()

    # Por cada muestra se coloca el mundo como nos indica la muestra y se renderiza
    # Set working directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    object_file = r"\Raw_objects\Monkey.obj"

    # Load the .blend file containing the sample object (Monkey.obj)
    obj = bproc.loader.load_obj(current_dir + object_file)[0]
    obj.set_location([0, 0, 0])
    obj.set_rotation_euler([np.pi/2, 0, 0])

    # Create a point light next to it
    light = bproc.types.Light()
    light.set_location([2, -2, 0])
    light.set_energy(300)

    # Set the camera and resolution
    bproc.camera.set_resolution(512, 512)
    cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
    bproc.camera.add_camera_pose(cam_pose)
    
    # Find point of interest, all cam poses should look towards it
    poi = bproc.object.compute_poi([obj])
    # Sample five camera poses
    for i in range(2):
        # Sample random camera location above objects
        location = np.random.uniform([-10, -10, 8], [10, 10, 12])
        # Compute rotation based on vector going from location towards poi
        rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot=np.random.uniform(-0.7854, 0.7854))
        # Add homog cam pose based on location an rotation
        cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
        bproc.camera.add_camera_pose(cam2world_matrix)

    # Render the scene
    data = bproc.renderer.render()
    save_images(data, args.output_dir, args.run)


if __name__ == "__main__":
    main()