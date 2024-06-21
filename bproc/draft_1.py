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
    #parser.add_argument('scene', nargs='?', default="examples/resources/scene.obj", help="Path to the scene.obj file")
    parser.add_argument('output_dir', nargs='?', default="ouput_images/draft_1", help="Path to where the final files, will be saved")
    return parser.parse_args()

def load_samples(file_name: str = "samples.csv") -> pd.DataFrame:
    """ 
    This function will load the samples.csv file and return the data as a pandas DataFrame

    Returns:
    pd.DataFrame: The samples data
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    samples_file = current_dir + file_name
    samples = pd.read_csv(samples_file)

    return samples

def save_images(data:str, output_file:str = "output_imgs/output_img") -> None:
    """
    Function to save the images in the data dictionary to the output_file as .png files

    Args:
    data (dict): The data dictionary containing the images
    output_file (str): The output file to save the images to

    Returns:
    None
    """
    img_array = data["colors"]

    for i in range(len(img_array)):
        # Write the data into a .png file using ImageIO
        output_file_i = output_file + f"_{i}.png"
        imageio.imwrite(output_file_i, img_array[i])

        print(f"Image saved to {output_file}")


def main():
    args = parse_args()
    bproc.init()

    # Cargamos los objetos para tenerlos en memoria y poder manipularlos
    bproc.load_objects()

    # Cargamos las muestras
    # samples = load_samples()

    # Por cada muestra se coloca el mundo como nos indica la muestra y se renderiza
    
    
    # Render the scene
    data = bproc.renderer.render()
    save_images(data, args.output_dir)
    

if __name__ == "__main__":
    main()