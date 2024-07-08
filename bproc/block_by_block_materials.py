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

def create_background(back_data: dict, mods_dict: dict):
    """
    Creates a background plane in the Blender scene and applies a texture and normal map
    to it.
 
    This function creates a plane named "Background" in the Blender scene if it doesn't
    exist already. It then creates a new material named "Background_Material" and sets
    up nodes to use the specified texture and normal map files to create a textured sur-
    face on the plane.
 
    Args:
        data (dict): A dictionary containing info about the position or scale of the
        plane background.
        mods_dict (dict): The dictionary with the info about what to modify according to
        the blueprint
    """
 
    # Create plane
    if not bpy.data.objects.get("Plane"):
        bpy.ops.mesh.primitive_plane_add()
    plane = bpy.data.objects["Plane"]
    plane.scale = (back_data["scale_x"], back_data["scale_y"], 1)
    plane.location = (back_data["pos_x"], back_data["pos_y"], back_data["pos_z"])
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
 
    # New background material
    mat = bpy.data.materials.new(name="Background_Material")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
 
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
 
    # Create necessary nodes and adjust values
    principled_node = nodes.new(type="ShaderNodeBsdfPrincipled")
    principled_node.inputs["Specular"].default_value = 0.25
    principled_node.inputs["Roughness"].default_value = 0.25
    principled_node.inputs["Metallic"].default_value = 0.8
    texture_node = nodes.new(type="ShaderNodeTexImage")
    normals_node = nodes.new(type="ShaderNodeNormalMap")
    normals_node.inputs["Strength"].default_value = 0.5
    normals_image_node = nodes.new(type="ShaderNodeTexImage")
    output_node = nodes.new(type="ShaderNodeOutputMaterial")
 
    # Set node locations to prevent overlapping
    principled_node.location = (200, 300)
    texture_node.location = (-300, 300)
    normals_node.location = (0, -50)
    normals_image_node.location = (-300, -50)
    output_node.location = (500, 300)
 
    background_mat = mods_dict["background_material"]
    background_mat_root = os.path.join(
        bpy.path.abspath("//"),
        "assets",
        "textures",
        "backgrounds",
        background_mat,
    )
    texture_path = os.path.join(
        background_mat_root,
        "texture.png",
    )
    normals_path = os.path.join(
        background_mat_root,
        "normals.png",
    )
    texture_node.image = bpy.data.images.load(texture_path)
    normals_image_node.image = bpy.data.images.load(normals_path)
 
    # Link nodes
    links.new(texture_node.outputs["Color"], principled_node.inputs["Base Color"])
    links.new(normals_image_node.outputs["Color"], normals_node.inputs["Color"])
    links.new(normals_node.outputs["Normal"], principled_node.inputs["Normal"])
    links.new(principled_node.outputs["BSDF"], output_node.inputs["Surface"])
 
    # Asign material
    if plane.data.materials:
        plane.data.materials[0] = mat
    else:
        plane.data.materials.append(mat)

def texture_coordinate_node(nodes)-> bpy.types.Node:
    """
    Creates a texture coordinate node
    """
    new_node = nodes.new(type='ShaderNodeTexCoord')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.from_instancer = False
    new_node.location = (-1250.0, 300.0)
    new_node.name = 'Texture Coordinate'
    # --- Possible unnecessary ---
    # new_node.object = None
    # new_node.select = False
    # new_node.width = 140.0
    # new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[5].default_value = [0.0, 0.0, 0.0]
    # new_node.outputs[6].default_value = [0.0, 0.0, 0.0]

    return new_node

def material_output_node(nodes)-> bpy.types.Node:
    """
    Creates a material output node
    """
    new_node = nodes.new(type='ShaderNodeOutputMaterial')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.is_active_output = True
    new_node.location = (300.0, 300.0)
    new_node.name = 'Material Output'
    new_node.select = False
    new_node.target = 'ALL'
    new_node.width = 140.0

    return new_node

def principled_BSDF_node(nodes)-> bpy.types.Node:
    """
    Creates a principled BSDF node
    """
    new_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.distribution = 'GGX'
    new_node.location = (-50.0, 300.0)
    new_node.name = 'Principled BSDF'
    new_node.select = False
    new_node.subsurface_method = 'RANDOM_WALK'
    new_node.width = 240.0
    new_node.inputs["IOR"].default_value = 1.5
    new_node.inputs["Weight"].default_value = 0.0
    new_node.inputs["Anisotropic"].default_value = 0.0


    return new_node

def create_galvanizedsteel(imgs_path: str = None, material_name: str = "MetalGalvanizedSteelWorn001"):
    """
    Creates galvanized steel material based on the Poliigon Material

    This function requires having the file containing the jpgs regarding the Poliigon Material 
 
    Args:
        path (str): Indicates the ABSOLUTE path to the material with the files needed 
        material_name (str): Name of the material to be created
    
    Returns: 
        mat : GalvanizedSteel by poliigon with some differences due to blenderproc (bpy.types.Material)
    """
 
    # New background material
    mat = bpy.data.materials.new(name=material_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
 
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Define the route to the file
    current_directory = os.getcwd()
    if imgs_path is None:
        # The path from the current file to the material
        path_to_material = os.path.join(
            "assets",
            "Raw_materials",
            "Dishes",
            material_name,
        )
        path_to_material = os.path.join(current_directory, path_to_material)
    else:
        path_to_material = imgs_path
    
    # Texture coordinate node (1)
    new_node = texture_coordinate_node(nodes)  
    

    # Simple UV Mapping node (2)
    # --- Possible unnecessary ---
    # new_node = nodes.new(type='ShaderNodeGroup')
    # new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    # new_node.label = '.simple_uv_mapping'
    # new_node.location = (-1000.0, 300.0)
    # new_node.name = '.simple_uv_mapping'
    # ng = bpy.data.node_groups.get('.simple_uv_mapping')
    # if not ng:
    #     new_node.label = "Missing Node Group : '.simple_uv_mapping'"
    # else:
    #     new_node.node_tree = ng               
    #     new_node.select = False
    #     new_node.width = 250.0
    #     print(len(new_node.inputs))
    #     new_node.inputs[0].default_value = 1.0
    #     new_node.inputs[1].default_value = 0.0
    #     new_node.inputs[2].default_value = 0.0
    #     new_node.inputs[3].default_value = 0.0
    #     new_node.inputs[4].default_value = 1.0

    

    # Texture COL node (3)
    # Image path
    texture_COL_path = os.path.join(
        path_to_material,
        material_name + "_COL_2K_METALNESS.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_COL_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'COL'
    new_node.location = (-650.0, 300.0)
    new_node.name = 'COL'
    parent = nodes.get('Textures')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0


    # Texture METALNESS node (4)
    # Image path
    texture_METALNESS_path = os.path.join(
        path_to_material,
        material_name + "_METALNESS_2K_METALNESS.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_METALNESS_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'METALNESS'
    new_node.location = (-650.0, -50.0)
    new_node.name = 'METALNESS'
    parent = nodes.get('Textures')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0

    # Texture ROUGHNESS node (5)
    # Image path
    texture_ROUGHNESS_path = os.path.join(
        path_to_material,
        material_name + "_ROUGHNESS_2K_METALNESS.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_ROUGHNESS_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'ROUGHNESS'
    new_node.location = (-650.0, -400.0)
    new_node.name = 'ROUGHNESS'
    parent = nodes.get('Textures')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0

    # Texture NRM16 node (6)
    # Image path
    texture_NRM16_path = os.path.join(
        path_to_material,
        material_name + "_NRM16_2K_METALNESS.tif",
    )
    # texture_NRM16_path = os.path.join(
    #     path_to_material,
    #     material_name + "_NRM_2K_METALNESS.jpg",
    # )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_NRM16_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'NRM16'
    new_node.location = (-650.0, -750.0)
    new_node.name = 'NRM16'
    parent = nodes.get('Textures')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0

    # Normal Map node (7)
    new_node = nodes.new(type='ShaderNodeNormalMap')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -750.0)
    new_node.name = 'Normal Map'
    new_node.select = False
    new_node.space = 'TANGENT'
    new_node.width = 150.0
    new_node.inputs[0].default_value = 1.0
    new_node.inputs[1].default_value = [0.5, 0.5, 1.0, 1.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
    
    # Principled BSDF node (8)
    new_node = principled_BSDF_node(nodes)

    # Material output node (9)
    new_node = material_output_node(nodes)

    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["COL"].inputs["Vector"])    
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["METALNESS"].inputs["Vector"])    
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["NRM16"].inputs["Vector"])    
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["ROUGHNESS"].inputs["Vector"])
    links.new(nodes["COL"].outputs["Color"], nodes["Principled BSDF"].inputs["Base Color"])    
    links.new(nodes["COL"].outputs["Alpha"], nodes["Principled BSDF"].inputs["Alpha"])    
    links.new(nodes["METALNESS"].outputs["Color"], nodes["Principled BSDF"].inputs["Metallic"])    
    links.new(nodes["ROUGHNESS"].outputs["Color"], nodes["Principled BSDF"].inputs["Roughness"])   
    links.new(nodes["NRM16"].outputs["Color"], nodes["Normal Map"].inputs["Color"])    
    links.new(nodes["Normal Map"].outputs["Normal"], nodes["Principled BSDF"].inputs["Normal"])    
    links.new(nodes["Principled BSDF"].outputs["BSDF"], nodes["Material Output"].inputs["Surface"])    
    
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

    # New background material
    mat = bpy.data.materials.new(name=material_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    for node in nodes:
        nodes.remove(node)

    # Define the route to the file
    current_directory = os.getcwd()
    if imgs_path is None:
        # The path from the current file to the material
        path_to_material = os.path.join(
            "assets",
            "Raw_materials",
            "Dishes",
            material_name,
        )
        path_to_material = os.path.join(current_directory, path_to_material)
    else:
        path_to_material = imgs_path

    # Texture coordinate node (1)
    new_node = texture_coordinate_node(nodes)

    # Texture COL node (2)
    # Image path
    texture_COL_path = os.path.join(
        path_to_material,
        material_name + "_COL_2K.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    # attributes = dir(new_node)
    # for attribute in attributes:
    #     print(attribute)
    # input()
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_COL_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0
    new_node.interpolation = 'Linear'
    new_node.label = 'COL'
    new_node.location = (-650.0, 300.0)
    new_node.name = 'COL'
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # Texture AO node (3)
    # Image path
    texture_AO_path = os.path.join(
        path_to_material,
        material_name + "_AO_2K.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_AO_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0
    new_node.interpolation = 'Linear'
    new_node.label = 'AO'
    new_node.location = (-650.0, -50.0)
    new_node.name = 'AO'
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # Texture REFL node (4)
    # Image path
    texture_REFL_path = os.path.join(
        path_to_material,
        material_name + "_REFL_2K.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_REFL_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0
    new_node.interpolation = 'Linear'
    new_node.label = 'REFL'
    new_node.location = (-650.0, -400.0)
    new_node.name = 'REFL'
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # Texture GLOSS node (5)
    # Image path
    texture_GLOSS_path = os.path.join(
        path_to_material,
        material_name + "_GLOSS_2K.jpg",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_GLOSS_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0
    new_node.interpolation = 'Linear'
    new_node.label = 'GLOSS'
    new_node.location = (-650.0, -750.0)
    new_node.name = 'GLOSS'
    parent = nodes.get('Textures')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0

    # Texture NRM node (6)
    # Image path
    texture_NRM_path = os.path.join(
        path_to_material,
        material_name + "_NRM_2K.png",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_NRM_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'NRM'
    new_node.location = (-650.0, -1100.0)
    new_node.name = 'NRM'                 
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # Texture DISP node (7)
    # Image path
    texture_DISP_path = os.path.join(
        path_to_material,
        material_name + "_DISP16_2K.tif",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_DISP_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Cubic'
    new_node.label = 'DISP16'
    new_node.location = (-650.0, -1450.0)
    new_node.name = 'DISP16'                   
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # Texture BUMP node (8)
    # Image path
    texture_BUMP_path = os.path.join(
        path_to_material,
        material_name + "_BUMP16_2K.tif",
    )
    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.load(texture_BUMP_path)
    img_text = new_node.image_user
    img_text.frame_current = 0
    img_text.frame_duration = 100
    img_text.frame_offset = 0
    img_text.frame_start = 1
    img_text.use_auto_refresh = False
    img_text.use_cyclic = False
    img_text.tile = 0                
    new_node.interpolation = 'Linear'
    new_node.label = 'BUMP16'
    new_node.location = (-650.0, -1800.0)
    new_node.name = 'BUMP16'                   
    new_node.projection = 'FLAT'
    new_node.projection_blend = 0.0
    new_node.select = False
    new_node.width = 240.0

    # COLOR * AO node (9)
    new_node = nodes.new(type='ShaderNodeMix')
    new_node.blend_type = 'MULTIPLY'
    new_node.clamp_factor = True
    new_node.clamp_result = False
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.data_type = 'RGBA'
    new_node.factor_mode = 'UNIFORM'
    new_node.label = 'COLOR * AO'
    new_node.location = (-300.0, 300.0)
    new_node.name = 'COLOR * AO'
    new_node.select = False
    new_node.width = 140.0

    # Invert GLOSS node (10)
    new_node = nodes.new(type='ShaderNodeInvert')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Invert Gloss'
    new_node.location = (-300.0, -750.0)
    new_node.name = 'Invert Gloss'
    new_node.select = False
    new_node.width = 140.0
    new_node.inputs[0].default_value = 1.0

    # Normal Map node (11)
    new_node = nodes.new(type='ShaderNodeNormalMap')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1100.0)
    new_node.name = 'Normal Map'
    new_node.select = False
    new_node.space = 'TANGENT'
    new_node.width = 150.0
    new_node.inputs[0].default_value = 0.0

    # Displacement node (12)
    new_node = nodes.new(type='ShaderNodeDisplacement')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1450.0)
    new_node.name = 'Displacement'
    new_node.select = False
    new_node.space = 'OBJECT'
    new_node.width = 140.0
    new_node.inputs[1].default_value = 0.5
    new_node.inputs[2].default_value = 0.0
    
    # Principled BSDF node (13)
    new_node = principled_BSDF_node(nodes)

    # Material output node (14)
    new_node = material_output_node(nodes)

    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["COL"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["AO"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["REFL"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["GLOSS"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["NRM"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["DISP16"].inputs["Vector"])
    links.new(nodes["Texture Coordinate"].outputs["UV"], nodes["BUMP16"].inputs["Vector"])
    links.new(nodes["COL"].outputs["Color"], nodes["COLOR * AO"].inputs["A"])
    links.new(nodes["COL"].outputs["Alpha"], nodes["Principled BSDF"].inputs["Alpha"])
    links.new(nodes["AO"].outputs["Color"], nodes["COLOR * AO"].inputs["B"])
    links.new(nodes["REFL"].outputs["Color"], nodes["Principled BSDF"].inputs["Metallic"])
    links.new(nodes["GLOSS"].outputs["Color"], nodes["Invert Gloss"].inputs["Color"])
    links.new(nodes["NRM"].outputs["Color"], nodes["Normal Map"].inputs["Color"])
    links.new(nodes["DISP16"].outputs["Color"], nodes["Displacement"].inputs["Height"])
    #links.new(nodes["COLOR * AO"].outputs["Result"], nodes["Material Output"].inputs["Surface"])
    links.new(nodes["COLOR * AO"].outputs["Result"], nodes["Principled BSDF"].inputs["Base Color"])
    links.new(nodes["Invert Gloss"].outputs["Color"], nodes["Principled BSDF"].inputs["Roughness"])
    links.new(nodes["Normal Map"].outputs["Normal"], nodes["Principled BSDF"].inputs["Normal"])
    links.new(nodes["Displacement"].outputs["Displacement"], nodes["Material Output"].inputs["Displacement"])
    links.new(nodes["Principled BSDF"].outputs["BSDF"], nodes["Material Output"].inputs["Surface"])



    # New background material
    mat = bpy.data.materials.new(name=material_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    nodes.clear()

    # Texture coordinate node
    texture_coordinate = nodes.new(type='ShaderNodeTexCoord')
    texture_coordinate.location = (-800, 300)

    def create_texture_node(label, image_path, location):
        node = nodes.new(type='ShaderNodeTexImage')
        node.image = bpy.data.images.load(image_path)
        node.location = location
        node.label = label
        node.name = label
        node.extension = 'REPEAT'
        return node


    current_directory = os.getcwd()
    if imgs_path is None:
        # The path from the current file to the material
        path_to_material = os.path.join(
            "assets",
            "Raw_materials",
            "Dishes",
            material_name,
        )
        path = os.path.join(current_directory, path_to_material)
    else:
        path = imgs_path

    # Image paths
    texture_paths = {
        "COL": os.path.join(path, material_name + "_COL_2K.jpg"),
        "AO": os.path.join(path, material_name + "_AO_2K.jpg"),
        "REFL": os.path.join(path, material_name + "_REFL_2K.jpg"),
        "GLOSS": os.path.join(path, material_name + "_GLOSS_2K.jpg"),
        "NRM": os.path.join(path, material_name + "_NRM_2K.png"),
        "DISP16": os.path.join(path, material_name + "_DISP16_2K.tif"),
        "BUMP16": os.path.join(path, material_name + "_BUMP16_2K.tif"),
    }

    # Create texture nodes
    col_node = create_texture_node("COL", texture_paths["COL"], (-600, 300))
    ao_node = create_texture_node("AO", texture_paths["AO"], (-600, 0))
    refl_node = create_texture_node("REFL", texture_paths["REFL"], (-600, -300))
    gloss_node = create_texture_node("GLOSS", texture_paths["GLOSS"], (-600, -600))
    nrm_node = create_texture_node("NRM", texture_paths["NRM"], (-600, -900))
    disp16_node = create_texture_node("DISP16", texture_paths["DISP16"], (-600, -1200))
    bump16_node = create_texture_node("BUMP16", texture_paths["BUMP16"], (-600, -1500))

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
    principled_bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    principled_bsdf_node.location = (0, 0)
    principled_bsdf_node.label = 'Principled BSDF'
    principled_bsdf_node.name = 'Principled BSDF'

    # Material output node
    material_output_node_node = nodes.new(type='ShaderNodeOutputMaterial')
    material_output_node_node.location = (200, 0)

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
    light.set_location([2, -2, 0])
    light.set_energy(300)

    # Set the camera and resolution
    bproc.camera.set_resolution(512, 512)
    cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
    bproc.camera.add_camera_pose(cam_pose)

    colors = generate_colors(7)
    # Create a material for the objeect
    galvanized_steel = create_galvanizedsteel()
    wood_flooring_ash_super_white = create_wood_flooring_ash_super_white()
    obj.blender_obj.data.materials.clear()
    # obj.blender_obj.data.materials.append(galvanized_steel)
    obj.blender_obj.data.materials.append(wood_flooring_ash_super_white)
    # Render the scene
    data = bproc.renderer.render()

    # Save the image
    save_image(data, output_file)

if __name__ == "__main__":
    object_file = r"\assets\Raw_objects\Monkey.obj"
    output_file = r"\output_imgs\000003.png"
    main(object_file, output_file)
