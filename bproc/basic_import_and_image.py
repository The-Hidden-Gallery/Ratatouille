import blenderproc as bproc
import numpy as np
import imageio
import os

def save_image(data, output_file):
    # Write the data into a .png file using ImageIO
    img_array = data["colors"][0]
    imageio.imwrite(output_file, img_array)

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

    # Render the scene
    data = bproc.renderer.render()

    # Save the image
    save_image(data, output_file)

if __name__ == "__main__":
    object_file = r"\assets\Raw_objects\Monkey.obj"
    output_file = r"\output_imgs\000001.png"
    main(object_file, output_file)
