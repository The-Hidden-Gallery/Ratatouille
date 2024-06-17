import blenderproc as bproc
import numpy as np
import imageio
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize BlenderProc
bproc.init()

# Load the .blend file containing the sample object (Monkey.obj)
obj = bproc.loader.load_obj(current_dir + r"\Raw_objects\Monkey.obj")
obj = obj[0]

obj.set_location([0, 1, 0])
obj.set_rotation_euler([np.pi/2, 0, 0])

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

# Write the data into a .png file using ImageIO
img_array = data["colors"][0]
output_file = current_dir + r"\output_imgs\000001.png"  # Replace with a counter
imageio.imwrite(output_file, img_array)

print(f"Image saved to {output_file}")