# generic libraries
import argparse
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from tqdm import tqdm
import cv2
import os
import shutil
from typing import List

# # projectaria libraries
from projectaria_tools.core import data_provider, calibration
from projectaria_tools.core.image import InterpolationMethod
from projectaria_tools.core.sensor_data import TimeDomain, TimeQueryOptions
from projectaria_tools.core.stream_id import RecordableTypeId, StreamId

def check_vrs_file(value: str) -> str:
    """ Function that checks if the input file is of the type .vrs.
        Args:
            value (str): The input file.
        Returns:
            str: The input file if it is of the type .vrs.
        Raises:
            argparse.ArgumentTypeError: If the file is not of the type .vrs."""
    
    if not value.endswith('.vrs'):
        raise argparse.ArgumentTypeError("The file must be of the type .vrs")
    return value

def parsedinputs() -> str:
    """ Function that parses the input arguments and returns the path of the .vrs file.
        Returns:
            str: The path of the .vrs file."""
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Program that converts a .vrs file to .mp4 files of its different streams. \
                    The file must be inside a 'data' folder in the same directory as the script.\
                    The output files will be saved in the same folder as the original.")

    # Add the mandatory argument
    parser.add_argument('vrs_file', type=check_vrs_file, help='Video file in the format .vrs')

    return parser.parse_args().vrs_file

def compress_folder(folder_path: str) -> None:
    """ Function that compresses a folder into a ZIP file.
        Args:
            folder_path (str): The path of the folder to compress.
            output_filename (str): The name of the output ZIP file.
        Returns:
            None."""
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found")
    
    zip_path = os.path.join(os.getcwd(), folder_path + ".zip")

    shutil.make_archive(base_name=zip_path.replace('.zip', ''), format='zip', root_dir=folder_path)

    print(f"Folder '{folder_path}' compressed into '{zip_path}'")

def save_video(images:List[Image.Image], filename: str, foldername: str="output", fps: int=30) -> None:
    """ Function that saves a list of images as a video file.
        Args:
            images (List[Image.Image]): The list of images to save.
            filename (str): The name of the output video file.
            foldername (str): The name of the folder where the video will be saved.
            fps (int): The frames per second of the output video.
        Returns:
            None."""

    output_dir = os.path.join(os.getcwd(), foldername)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    full_path = os.path.join(output_dir, filename + ".mp4")

    height, width = np.array(images[0]).shape[:2]
    video = cv2.VideoWriter(full_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for img in images:
        video.write(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    video.release()

    print(f"Video '{filename}.mp4' saved in '{output_dir}'")

def process_vrs_file(vrsfile: str) -> None:
    """ Function that processes a .vrs file and saves its streams as .mp4 files.
        Args:
            vrs_file (str): The path of the .vrs file.
        Returns:
            None."""

    provider = data_provider.create_vrs_data_provider(vrsfile)

    if not provider:
        print("Please select an existing video")
        return
    else:
        print("File chosen: "+ vrsfile)

    # Hay que mejorar esto para tener todos los canales, no solo los de video
    stream_mappings = {
    "camera_slam_left": StreamId("1201-1"),
    "camera_slam_right":StreamId("1201-2"),
    "camera_rgb":StreamId("214-1"),
    "camera_eyetracking":StreamId("211-1"),
    }

    for [stream_name, stream_id] in list(stream_mappings.items()):
        num_data = provider.get_num_data(stream_id)
        if num_data:
            final_video = []
            for index in range(0, num_data):
                image_data = provider.get_image_data_by_index(stream_id, index)
                image_array = image_data[0].to_numpy_array()
                image = Image.fromarray(image_array)
                final_video.append(image)

            # Los fps deberían ser los mismos que los del video original en ese canal, pero no se como sacarlos todavía
            save_video(final_video, filename=stream_name, foldername=vrsfile, fps= 30)

def main():
    vrs_file = parsedinputs()
    process_vrs_file(vrs_file)
    

if __name__ == "__main__":
    main()
