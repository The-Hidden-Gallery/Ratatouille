import blenderproc as bproc
import numpy as np
import imageio
import os

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
    os.mkdir(output_file)
    output_file = output_file + '/'
    for i in range(len(img_array)):
        # Write the data into a .png file using ImageIO
        output_file_i = output_file + f"{i}.png"
        imageio.imwrite(output_file_i, img_array[i])

        print(f"Image saved to {output_file}")



def main(object_file, output_file):
    # Initialize BlenderProc
    bproc.init()

    # Set working directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = current_dir + output_file


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
    for i in range(5):
        # Sample random camera location above objects
        location = np.random.uniform([-10, -10, 8], [10, 10, 12])
        # Compute rotation based on vector going from location towards poi
        rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot=np.random.uniform(-0.7854, 0.7854))
        # Add homog cam pose based on location an rotation
        cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
        bproc.camera.add_camera_pose(cam2world_matrix)

    # Render the scene
    data = bproc.renderer.render()

    run = "8"

    save_images(data, output_file + "/" + run)
if __name__ == "__main__":
    object_file = r"\Raw_objects\Monkey.obj"
    output_file = r"\output_imgs"
    main(object_file, output_file)