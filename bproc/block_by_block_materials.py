import blenderproc as bproc
import numpy as np
import imageio
import os
import bpy
import random

def save_image(data, output_file):
    # Write the data into a .png file using ImageIO
    img_array = data["colors"][0]
    imageio.imwrite(output_file, img_array)

    print(f"Image saved to {output_file}")

def create_texture_node(nodes, label, image_path, location):
    """
    Creates a texture node, loads the image and sets the properties

    Args:
    nodes (bpy.types.Node): The node tree to add the node to
    label (str): The label of the node
    image_path (str): The path to the image
    location (tuple): The location of the node in the node tree

    Returns:
    bpy.types.Node: The created node
    """
    node = nodes.new(type='ShaderNodeTexImage')
    node.image = bpy.data.images.load(image_path)
    node.location = location
    node.label = label
    node.name = label
    node.extension = 'REPEAT'
    node.interpolation = 'Linear'
    
    return node

def create_texture_coordinate_node(nodes,location)-> bpy.types.Node:
    """
    Creates a texture coordinate node to be used in the material nodes

    Args:
    nodes (bpy.types.Node): The node tree to add the node to
    location (tuple): The location of the node in the node tree

    Returns:
    bpy.types.Node: The created node
    """
    
    texture_coordinate = nodes.new(type='ShaderNodeTexCoord')
    texture_coordinate.location = location
    texture_coordinate.name = 'Texture Coordinate'

    return texture_coordinate

def create_material_output_node(nodes,location)-> bpy.types.Node:
    """
    Creates a material output node to be used in the material nodes

    Args:
    nodes (bpy.types.Node): The node tree to add the node to
    location (tuple): The location of the node in the node tree

    Returns:
    bpy.types.Node: The created node
    """
    
    material_output = nodes.new(type='ShaderNodeOutputMaterial')
    material_output.location = location
    material_output.name = 'Material Output'

    return material_output

def create_principled_BSDF_node(nodes,location)-> bpy.types.Node:
    """
    Creates a principled BSDF node
    """

    principled_bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    principled_bsdf_node.location = location
    principled_bsdf_node.label = 'Principled BSDF'
    principled_bsdf_node.name = 'Principled BSDF'

    return principled_bsdf_node

def init_material(material_name: str):
    """
    This function will instantiate a new material and remove all the default nodes.
    
    Args:
    name (str): The name of the material to remove.
    """
    # New material
    mat = bpy.data.materials.new(name=material_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    for node in nodes:
        nodes.remove(node)

    return mat, nodes, links

def create_imgs_path(material_name: str, imgs_path: str) -> str:
    """
    This function will create the path to the images of the material.
    
    Args:
    material_name (str): The name of the material.
    imgs_path (str): The path to the materials folder.
    
    Returns:
    str: The path to the folder containing the images of a specific material.
    """
    if imgs_path is None:
        # ------ This should be changes according to the structure of the project ------
        imgs_path = os.path.join(
            "assets",
            "Raw_materials",
            "Dishes",
            material_name,
        )
    current_directory = os.getcwd()
    complete_path = os.path.join(current_directory, imgs_path)

    return complete_path

def create_ceramic_plain_white(imgs_path: str = None, material_name: str = "CeramicPlainWhite001"):
    """
    Creates ceramic material based on the Poliigon Material
    
    This function requires having the file containing the jpgs regarding the Poliigon Material
    
    Args:
        path (str): Indicates the ABSOLUTE path to the material with the files needed 
        material_name (str): Name of the material to be created
        
        Returns:
        mat : CeramicPlainWhite by poliigon with some differences due to blenderproc (bpy.types.Material)
    
    """
    mat, nodes, links = init_material(material_name)

    # Define the route to the file
    imgs_path = create_imgs_path(material_name, imgs_path)

    # Image paths
    texture_paths = {
        "COL": os.path.join(imgs_path, material_name + "_COL_2K.jpg"),
        "REFL": os.path.join(imgs_path, material_name + "_REFL_2K.jpg"),
        "GLOSS": os.path.join(imgs_path, material_name + "_GLOSS_2K.jpg"),
        "NRM": os.path.join(imgs_path, material_name + "_NRM_2K.png"),
        "DISP16": os.path.join(imgs_path, material_name + "_DISP16_2K.tif"),
    }

    # Texture coordinate node
    texture_coordinate = create_texture_coordinate_node(nodes, (-800, 300))

    # Create texture nodes
    col_node = create_texture_node(nodes, "COL", texture_paths["COL"], (-600, 300))
    refl_node = create_texture_node(nodes, "REFL", texture_paths["REFL"], (-600, -300))
    gloss_node = create_texture_node(nodes, "GLOSS", texture_paths["GLOSS"], (-600, -600))
    nrm_node = create_texture_node(nodes, "NRM", texture_paths["NRM"], (-600, -900))
    disp16_node = create_texture_node(nodes, "DISP16", texture_paths["DISP16"], (-600, -1200))
    disp16_node.interpolation = 'Cubic'

    # Invert GLOSS node
    invert_gloss_node = nodes.new(type='ShaderNodeInvert')
    invert_gloss_node.location = (-300, -600)
    invert_gloss_node.label = 'Invert Gloss'
    invert_gloss_node.name = 'Invert Gloss'

    # Normal Map node
    normal_map_node = nodes.new(type='ShaderNodeNormalMap')
    normal_map_node.location = (-300, -900)
    normal_map_node.label = 'Normal Map'
    normal_map_node.name = 'Normal Map'
    normal_map_node.space = 'TANGENT'
    normal_map_node.inputs["Strength"].default_value = 0.0

    # Displacement node
    displacement_node = nodes.new(type='ShaderNodeDisplacement')
    displacement_node.location = (-300, -1200)
    displacement_node.label = 'Displacement'
    displacement_node.name = 'Displacement'
    displacement_node.space = 'OBJECT'
    displacement_node.inputs["Midlevel"].default_value = 0.5
    displacement_node.inputs["Scale"].default_value = 0.0

    # Principled BSDF node
    principled_bsdf_node = create_principled_BSDF_node(nodes, (0, 0))

    # Material output node
    material_output_node_node = create_material_output_node(nodes, (200, 0))

    # Create links
    links.new(texture_coordinate.outputs["UV"], col_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], refl_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], gloss_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], nrm_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], disp16_node.inputs["Vector"])

    links.new(refl_node.outputs["Color"], principled_bsdf_node.inputs["Metallic"])
    links.new(gloss_node.outputs["Color"], invert_gloss_node.inputs["Color"])
    links.new(invert_gloss_node.outputs["Color"], principled_bsdf_node.inputs["Roughness"])

    links.new(nrm_node.outputs["Color"], normal_map_node.inputs["Color"])
    links.new(normal_map_node.outputs["Normal"], principled_bsdf_node.inputs["Normal"])

    links.new(disp16_node.outputs["Color"], displacement_node.inputs["Height"])
    links.new(displacement_node.outputs["Displacement"], material_output_node_node.inputs["Displacement"])

    links.new(principled_bsdf_node.outputs["BSDF"], material_output_node_node.inputs["Surface"])

    return mat

def create_metal_cladding_frame(imgs_path: str = None, material_name: str = "MetalCladdingFrame002"):
    """
    Creates metal cladding material based on the Poliigon Material
    
    This function requires having the file containing the jpgs regarding the Poliigon Material
    
    Args:
        path (str): Indicates the ABSOLUTE path to the material with the files needed 
        material_name (str): Name of the material to be created
        
        Returns:
        mat : MetalCladdingFrame by poliigon with some differences due to blenderproc (bpy.types.Material)
    
    """

    # New material 
    mat, nodes, links = init_material(material_name)

    # Define the route to the file
    imgs_path = create_imgs_path(material_name, imgs_path)

    # Individual image paths
    texture_paths = {
        "COL": os.path.join(imgs_path, material_name + "_COL_2K.jpg"),
        "REFL": os.path.join(imgs_path, material_name + "_REFL_2K.jpg"),
        "GLOSS": os.path.join(imgs_path, material_name + "_GLOSS_2K.jpg"),
        "NRM": os.path.join(imgs_path, material_name + "_NRM_2K.png"),
        "DISP16": os.path.join(imgs_path, material_name + "_DISP16_2K.tif"),
        "BUMP16": os.path.join(imgs_path, material_name + "_BUMP16_2K.tif"),
    }

    # Texture coordinate node
    texture_coordinate = nodes.new(type='ShaderNodeTexCoord')
    texture_coordinate.location = (-800, 300)

    # Create texture nodes
    col_node = create_texture_node(nodes, "COL", texture_paths["COL"], (-600, 300))
    refl_node = create_texture_node(nodes, "REFL", texture_paths["REFL"], (-600, -300))
    gloss_node = create_texture_node(nodes, "GLOSS", texture_paths["GLOSS"], (-600, -600))
    nrm_node = create_texture_node(nodes, "NRM", texture_paths["NRM"], (-600, -900))
    disp16_node = create_texture_node(nodes, "DISP16", texture_paths["DISP16"], (-600, -1200))
    disp16_node.interpolation = 'Cubic'
    bump16_node = create_texture_node(nodes, "BUMP16", texture_paths["BUMP16"], (-600, -1500))

    # Invert GLOSS node
    invert_gloss_node = nodes.new(type='ShaderNodeInvert')
    invert_gloss_node.location = (-300, -600)
    invert_gloss_node.label = 'Invert Gloss'
    invert_gloss_node.name = 'Invert Gloss'

    # Normal Map node
    normal_map_node = nodes.new(type='ShaderNodeNormalMap')
    normal_map_node.location = (-300, -900)
    normal_map_node.label = 'Normal Map'
    normal_map_node.name = 'Normal Map'
    normal_map_node.space = 'TANGENT'
    normal_map_node.inputs["Strength"].default_value = 0.0

    # Displacement node
    displacement_node = nodes.new(type='ShaderNodeDisplacement')
    displacement_node.location = (-300, -1200)
    displacement_node.label = 'Displacement'
    displacement_node.name = 'Displacement'
    displacement_node.space = 'OBJECT'
    displacement_node.inputs["Midlevel"].default_value = 0.5
    displacement_node.inputs["Scale"].default_value = 0.0

    # Principled BSDF node
    principled_bsdf_node = create_principled_BSDF_node(nodes, (0, 0))

    # Material output node
    material_output_node_node = create_material_output_node(nodes, (200, 0))

    # Create links
    links.new(texture_coordinate.outputs["UV"], col_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], refl_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], gloss_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], nrm_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], disp16_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], bump16_node.inputs["Vector"])

    links.new(gloss_node.outputs["Color"], invert_gloss_node.inputs["Color"])
    links.new(nrm_node.outputs["Color"], normal_map_node.inputs["Color"])
    links.new(disp16_node.outputs["Color"], displacement_node.inputs["Height"])

    links.new(col_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    links.new(col_node.outputs["Alpha"], principled_bsdf_node.inputs["Alpha"])
    links.new(refl_node.outputs["Color"], principled_bsdf_node.inputs["Metallic"])
    links.new(invert_gloss_node.outputs["Color"], principled_bsdf_node.inputs["Roughness"])
    links.new(normal_map_node.outputs["Normal"], principled_bsdf_node.inputs["Normal"])

    links.new(displacement_node.outputs["Displacement"], material_output_node_node.inputs["Displacement"])
    links.new(principled_bsdf_node.outputs["BSDF"], material_output_node_node.inputs["Surface"])

    return mat

def create_galvanizedsteel(imgs_path: str = None, material_name: str = "MetalGalvanizedSteelWorn001"):
    """
    Creates galvanized steel material based on the Poliigon Material

    This function requires having the file containing the jpgs regarding the Poliigon Material.
 
    Args:
        imgs_path (str): Indicates the ABSOLUTE path to the material with the files needed.
        material_name (str): Name of the material to be created.
    
    Returns: 
        mat : GalvanizedSteel by Poliigon with some differences due to blenderproc (bpy.types.Material)
    """
 
    # New material 
    mat, nodes, links = init_material(material_name)
    
    # Define the route to the file
    imgs_path = create_imgs_path(material_name, imgs_path)
    
    # Texture coordinate node
    tex_coord_node = create_texture_coordinate_node(nodes, (-800.0, 300.0))

    texture_paths = {
        "COL": os.path.join(imgs_path, material_name + "_COL_2K_METALNESS.jpg"),
        "METALNESS": os.path.join(imgs_path, material_name + "_METALNESS_2K_METALNESS.jpg"),
        "ROUGHNESS": os.path.join(imgs_path, material_name + "_ROUGHNESS_2K_METALNESS.jpg"),
        "NRM16": os.path.join(imgs_path, material_name + "_NRM16_2K_METALNESS.tif"),
    }

    # Create texture nodes
    col_node = create_texture_node(nodes, "COL", texture_paths["COL"], (-650.0, 300.0))
    metalness_node = create_texture_node(nodes, "METALNESS", texture_paths["METALNESS"], (-650.0, -50.0))
    roughness_node= create_texture_node(nodes, "ROUGHNESS", texture_paths["ROUGHNESS"], (-650.0, -400.0))
    nrm16_node= create_texture_node(nodes, "NRM16", texture_paths["NRM16"], (-650.0, -750.0))

    # Normal Map node
    normal_map_node = nodes.new(type='ShaderNodeNormalMap')
    normal_map_node.color = (0.608, 0.608, 0.608)
    normal_map_node.location = (-300.0, -750.0)
    normal_map_node.name = 'Normal Map'
    normal_map_node.space = 'TANGENT'

    # Principled BSDF node
    principled_bsdf = create_principled_BSDF_node(nodes, (0.0, 300.0))

    # Material output node
    material_output = create_material_output_node(nodes, (200.0, 300.0))

    # Links
    links.new(tex_coord_node.outputs["UV"], col_node.inputs["Vector"])    
    links.new(tex_coord_node.outputs["UV"], metalness_node.inputs["Vector"])    
    links.new(tex_coord_node.outputs["UV"], nrm16_node.inputs["Vector"])    
    links.new(tex_coord_node.outputs["UV"], roughness_node.inputs["Vector"])
    links.new(col_node.outputs["Color"], principled_bsdf.inputs["Base Color"])    
    links.new(col_node.outputs["Alpha"], principled_bsdf.inputs["Alpha"])    
    links.new(metalness_node.outputs["Color"], principled_bsdf.inputs["Metallic"])    
    links.new(roughness_node.outputs["Color"], principled_bsdf.inputs["Roughness"])   
    links.new(nrm16_node.outputs["Color"], normal_map_node.inputs["Color"])    
    links.new(normal_map_node.outputs["Normal"], principled_bsdf.inputs["Normal"])    
    links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])    
    
    return mat

def create_wood_flooring_ash_super_white(imgs_path: str = None, material_name: str = "WoodFlooringAshSuperWhite001"):
    """
    Creates wood flooring material based on the Poliigon Material
    
    This function requires having the file containing the jpgs regarding the Poliigon Material
    
    Args:
        path (str): Indicates the ABSOLUTE path to the material with the files needed 
        material_name (str): Name of the material to be created
        
        Returns:
        mat : WoodFlooringAshSuperWhite by poliigon with some differences due to blenderproc (bpy.types.Material)
    """

    # New material 
    mat, nodes, links = init_material(material_name)

    # Texture coordinate node
    texture_coordinate = create_texture_coordinate_node(nodes, (-800, 300))

    # Define the route to the file
    imgs_path = create_imgs_path(material_name, imgs_path)

    # Image paths
    texture_paths = {
        "COL": os.path.join(imgs_path, material_name + "_COL_2K.jpg"),
        "AO": os.path.join(imgs_path, material_name + "_AO_2K.jpg"),
        "REFL": os.path.join(imgs_path, material_name + "_REFL_2K.jpg"),
        "GLOSS": os.path.join(imgs_path, material_name + "_GLOSS_2K.jpg"),
        "NRM": os.path.join(imgs_path, material_name + "_NRM_2K.png"),
        "DISP16": os.path.join(imgs_path, material_name + "_DISP16_2K.tif"),
        "BUMP16": os.path.join(imgs_path, material_name + "_BUMP16_2K.tif"),
    }

    # Create texture nodes
    col_node = create_texture_node(nodes, "COL", texture_paths["COL"], (-600, 300))
    ao_node = create_texture_node(nodes, "AO", texture_paths["AO"], (-600, 0))
    refl_node = create_texture_node(nodes, "REFL", texture_paths["REFL"], (-600, -300))
    gloss_node = create_texture_node(nodes, "GLOSS", texture_paths["GLOSS"], (-600, -600))
    nrm_node = create_texture_node(nodes, "NRM", texture_paths["NRM"], (-600, -900))
    disp16_node = create_texture_node(nodes, "DISP16", texture_paths["DISP16"], (-600, -1200))
    bump16_node = create_texture_node(nodes, "BUMP16", texture_paths["BUMP16"], (-600, -1500))

    # COLOR * AO node
    color_ao_node = nodes.new(type='ShaderNodeMixRGB')
    color_ao_node.blend_type = 'MULTIPLY'
    color_ao_node.location = (-300, 300)
    color_ao_node.label = 'COLOR * AO'
    color_ao_node.name = 'COLOR * AO'

    # Invert GLOSS node
    invert_gloss_node = nodes.new(type='ShaderNodeInvert')
    invert_gloss_node.location = (-300, -600)
    invert_gloss_node.label = 'Invert Gloss'
    invert_gloss_node.name = 'Invert Gloss'

    # Normal Map node
    normal_map_node = nodes.new(type='ShaderNodeNormalMap')
    normal_map_node.location = (-300, -900)
    normal_map_node.label = 'Normal Map'
    normal_map_node.name = 'Normal Map'

    # Displacement node
    displacement_node = nodes.new(type='ShaderNodeDisplacement')
    displacement_node.location = (-300, -1200)
    displacement_node.label = 'Displacement'
    displacement_node.name = 'Displacement'

    # Principled BSDF node
    principled_bsdf_node = create_principled_BSDF_node(nodes, (0, 0))

    # Material output node
    material_output_node_node = create_material_output_node(nodes, (200, 0))

    # Create links
    links.new(texture_coordinate.outputs["UV"], col_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], ao_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], refl_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], gloss_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], nrm_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], disp16_node.inputs["Vector"])
    links.new(texture_coordinate.outputs["UV"], bump16_node.inputs["Vector"])
    links.new(col_node.outputs["Color"], color_ao_node.inputs[1])
    links.new(ao_node.outputs["Color"], color_ao_node.inputs[2])
    links.new(color_ao_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    links.new(refl_node.outputs["Color"], principled_bsdf_node.inputs["Metallic"])
    links.new(gloss_node.outputs["Color"], invert_gloss_node.inputs["Color"])
    links.new(invert_gloss_node.outputs["Color"], principled_bsdf_node.inputs["Roughness"])
    links.new(nrm_node.outputs["Color"], normal_map_node.inputs["Color"])
    links.new(normal_map_node.outputs["Normal"], principled_bsdf_node.inputs["Normal"])
    links.new(disp16_node.outputs["Color"], displacement_node.inputs["Height"])
    links.new(displacement_node.outputs["Displacement"], material_output_node_node.inputs["Displacement"])
    links.new(principled_bsdf_node.outputs["BSDF"], material_output_node_node.inputs["Surface"])

    return mat

def generate_colors(n_colors: int = 20) -> list:
    """
    This function will generate n_colors random colors and give them some reflectance properties.
    
    Args:
    n_colors (int): The number of colors to generate.
    
    Returns:
    list: The generated colors.
    """
    colors = []
    for i in range(n_colors):
        # Create a new material
        new_table_color = bpy.data.materials.new(name=f"Color_{i}")
        new_table_color.use_nodes = True
        nodes = new_table_color.node_tree.nodes

        # Clear all existing nodes
        for node in nodes:
            nodes.remove(node)

        # Add Principled BSDF node
        principled_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled_bsdf.location = (0, 0)

        # Add Material Output node
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        material_output.location = (200, 0)

        # Connect Principled BSDF to Material Output
        new_table_color.node_tree.links.new(principled_bsdf.outputs['BSDF'], material_output.inputs['Surface'])

        # Generate random color values
        values = [round(random.random(), 2), round(random.random(), 2), round(random.random(), 2), 1]

        # Set the base color of the Principled BSDF
        principled_bsdf.inputs['Base Color'].default_value = values

        # Set additional properties
        principled_bsdf.inputs['Metallic'].default_value = 0.1
        principled_bsdf.inputs['Roughness'].default_value = 0.6
        # principled_bsdf.inputs['Specular'].default_value = 0.5  # If needed

        colors.append(new_table_color)

    return colors


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
    light.set_location([0, -2, 5])
    light.set_energy(300)

    light = bproc.types.Light()
    light.set_location([0, -2, -5])
    light.set_energy(300)

    # Set the camera and resolution
    bproc.camera.set_resolution(512, 512)
    cam_pose = bproc.math.build_transformation_mat([0, -12, 0], [np.pi / 2, 0, 0])
    bproc.camera.add_camera_pose(cam_pose)

    colors = generate_colors(7)
    # Create a material for the objeect
    galvanized_steel = create_galvanizedsteel()
    wood_flooring_ash_super_white = create_wood_flooring_ash_super_white()
    ceranic_plain_white = create_ceramic_plain_white()
    metal_cladding_frame = create_metal_cladding_frame()
    obj1, obj2, obj3, obj4 = bproc.loader.load_obj(current_dir + object_file)[0], bproc.loader.load_obj(current_dir + object_file)[0], bproc.loader.load_obj(current_dir + object_file)[0], bproc.loader.load_obj(current_dir + object_file)[0]

    # Separate the objs 
    obj.set_location([0, 0, 0])
    obj1.set_location([-2, 0, 2])
    obj2.set_location([2, 0, 2])
    obj3.set_location([-2, 0, -2])
    obj4.set_location([2, 0, -2])

    for monkeyhead in [obj1, obj2, obj3, obj4]:
        monkeyhead.blender_obj.data.materials.clear()
    obj1.blender_obj.data.materials.append(galvanized_steel)
    obj2.blender_obj.data.materials.append(ceranic_plain_white)
    obj3.blender_obj.data.materials.append(wood_flooring_ash_super_white)
    obj4.blender_obj.data.materials.append(metal_cladding_frame)
    # Render the scene
    data = bproc.renderer.render()

    # Save the image
    save_image(data, output_file)

if __name__ == "__main__":
    object_file = r"\assets\Raw_objects\Monkey.obj"
    output_file = r"\output_imgs\material_gal.png"
    main(object_file, output_file)
