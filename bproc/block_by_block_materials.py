import blenderproc as bproc
import numpy as np
import imageio
import os
import bpy

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

def Material_output_node(nodes)-> bpy.types.Node:
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
    new_node.inputs[2].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[3].default_value = 0.0

    return new_node

def Principled_BSDF_node(nodes)-> bpy.types.Node:
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
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = [0.5, 0.5, 0.5]
    new_node.inputs[3].default_value = 1.5
    new_node.inputs[4].default_value = 1.0
    new_node.inputs[5].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[6].default_value = 0.0
    new_node.inputs[7].default_value = 0.0
    new_node.inputs[8].default_value = [1.0, 0.20000000298023224, 0.10000000149011612]
    new_node.inputs[9].default_value = 0.05000000074505806
    new_node.inputs[10].default_value = 1.399999976158142
    new_node.inputs[11].default_value = 0.0
    new_node.inputs[12].default_value = 0.5
    new_node.inputs[13].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[14].default_value = 0.0
    new_node.inputs[15].default_value = 0.0
    new_node.inputs[16].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[17].default_value = 0.0
    new_node.inputs[18].default_value = 0.0
    new_node.inputs[19].default_value = 0.029999999329447746
    new_node.inputs[20].default_value = 1.5
    new_node.inputs[21].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[22].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[23].default_value = 0.0
    new_node.inputs[24].default_value = 0.5
    new_node.inputs[25].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[26].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[27].default_value = 0.0

    return new_node

def create_galvanizedsteel(imgs_path: str = None, material_name: str = "MetalGalvanizedSteelWorn001"):
    """
    Creates galvanized steel material as in the Poliigon Add-on for blender

    This function requires having the file containing the information regarding the Poliigon Material 
 
    Args:
        path (str): Indicates the path to the material with the files needed 
    
    Returns: 
        mat : GalvanizedSteel by poliigon 
    """
 
    # New background material
    mat = bpy.data.materials.new(name=material_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
 
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Try the Galvanized one 

    
    current_directory = os.getcwd()
    # Define the route to the file 
    path_to_material = os.path.join(
        "assets",
        "Raw_materials",
        "Dishes",
        material_name,
    )
    path_to_material = os.path.join(current_directory, path_to_material)

    texture_COL_path = os.path.join(
        path_to_material,
        ".png",
    )

    # Texture coordinate node (1)
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

    # Simple UV Mapping node (2)
    new_node = nodes.new(type='ShaderNodeGroup')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = '.simple_uv_mapping'
    new_node.location = (-1000.0, 300.0)
    new_node.name = '.simple_uv_mapping'
    ng = bpy.data.node_groups.get('.simple_uv_mapping')
    if not ng:
        new_node.label = "Missing Node Group : '.simple_uv_mapping'"
    else:
        new_node.node_tree = ng
        # --- Possible unnecessary ---                
        new_node.select = False
        new_node.width = 250.0
        print(len(new_node.inputs))
        new_node.inputs[0].default_value = 1.0
        new_node.inputs[1].default_value = 0.0
        new_node.inputs[2].default_value = 0.0
        new_node.inputs[3].default_value = 0.0
        new_node.inputs[4].default_value = 1.0

    

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
    new_node = Principled_BSDF_node(nodes)

    # Material output node (9)
    new_node = Material_output_node(nodes)
    
    

 
 
    # Link nodes by input name 
    # links.new(texture_node.outputs["Color"], principled_node.inputs["Base Color"])
    # links.new(normals_image_node.outputs["Color"], normals_node.inputs["Color"])
    # links.new(normals_node.outputs["Normal"], principled_node.inputs["Normal"])
    # links.new(principled_node.outputs["BSDF"], output_node.inputs["Surface"])

    # Links nodes by name and position
    links.new(nodes["Principled BSDF"].outputs[0], nodes["Material Output"].inputs[0])    
    links.new(nodes["COL"].outputs[0], nodes["Principled BSDF"].inputs[0])    
    links.new(nodes["METALNESS"].outputs[0], nodes["Principled BSDF"].inputs[1])    
    links.new(nodes["NRM16"].outputs[0], nodes["Normal Map"].inputs[1])    
    links.new(nodes["Normal Map"].outputs[0], nodes["Principled BSDF"].inputs[5])    
    links.new(nodes["COL"].outputs[1], nodes["Principled BSDF"].inputs[4])    
    links.new(nodes["ROUGHNESS"].outputs[0], nodes["Principled BSDF"].inputs[2])    
    links.new(nodes["Texture Coordinate"].outputs[2], nodes[".simple_uv_mapping"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["COL"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["METALNESS"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["NRM16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["ROUGHNESS"].inputs[0])
 
    return mat 

def create_material_script():
    new_mat = bpy.data.materials.get('MetalGalvanizedSteelWorn001_2K')
    if not new_mat:
        new_mat = bpy.data.materials.new('MetalGalvanizedSteelWorn001_2K')
        
    new_mat.use_nodes = True
    node_tree = new_mat.node_tree
    nodes = node_tree.nodes
    nodes.clear()
        
    links = node_tree.links
    links.clear()
        
    # Nodes :

    new_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.distribution = 'GGX'
    new_node.location = (-50.0, 300.0)
    new_node.name = 'Principled BSDF'
    new_node.select = False
    new_node.subsurface_method = 'RANDOM_WALK_FIXED_RADIUS'
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = [0.5,0.5,0.5]
    new_node.inputs[3].default_value = [1.5, 1.5, 1.5,1.0]
    new_node.inputs[4].default_value = 1.0
    new_node.inputs[5].default_value = 0.0
    new_node.inputs[6].default_value = 0.0
    new_node.inputs[7].default_value = 0.0
    new_node.inputs[8].default_value = [1.0, 0.20000000298023224, 0.10000000149011612]
    new_node.inputs[9].default_value = 0.05000000074505806
    new_node.inputs[10].default_value = 1.399999976158142
    new_node.inputs[11].default_value = 0.0
    new_node.inputs[12].default_value = 0.5
    new_node.inputs[13].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[14].default_value = 0.0
    new_node.inputs[15].default_value = 0.0
    new_node.inputs[16].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[17].default_value = 0.0
    new_node.inputs[18].default_value = 0.0
    new_node.inputs[19].default_value = 0.029999999329447746
    new_node.inputs[20].default_value = 1.5
    new_node.inputs[21].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[22].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[23].default_value = 0.0
    new_node.inputs[24].default_value = 0.5
    new_node.inputs[25].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[26].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.inputs[27].default_value = 0.0

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Textures'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Textures'
    new_node.select = False
    new_node.width = 304.8000183105469

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_COL_2K_METALNESS')
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
    new_node.location = (-655.1174926757812, 283.3414611816406)
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_METALNESS_2K_METALNESS')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_NRM16_2K_METALNESS')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_ROUGHNESS_2K_METALNESS')
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Texture Projection/Mapping'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Texture Projection/Mapping'
    new_node.select = False
    new_node.width = 560.4000244140625

    new_node = nodes.new(type='ShaderNodeTexCoord')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.from_instancer = False
    new_node.location = (-1250.0, 300.0)
    new_node.name = 'Texture Coordinate'
    new_node.object = None
    parent = nodes.get('Texture Projection/Mapping')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.select = False
    new_node.width = 140.0
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[5].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[6].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeGroup')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = '.simple_uv_mapping'
    new_node.location = (-1000.0, 300.0)
    new_node.name = '.simple_uv_mapping'
    ng = bpy.data.node_groups.get('.simple_uv_mapping')
    if not ng:
        new_node.label = "Missing Node Group : '.simple_uv_mapping'"
    else:
        new_node.node_tree = ng                
    parent = nodes.get('Texture Projection/Mapping')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.select = False
    new_node.width = 250.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[1].default_value = 1.0
    new_node.inputs[2].default_value = 0.0
    new_node.inputs[3].default_value = 0.0
    new_node.inputs[4].default_value = 0.0
    new_node.inputs[5].default_value = 1.0
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    # Links :

    links.new(nodes["Principled BSDF"].outputs[0], nodes["Material Output"].inputs[0])    
    links.new(nodes["COL"].outputs[0], nodes["Principled BSDF"].inputs[0])    
    links.new(nodes["METALNESS"].outputs[0], nodes["Principled BSDF"].inputs[1])    
    links.new(nodes["NRM16"].outputs[0], nodes["Normal Map"].inputs[1])    
    links.new(nodes["Normal Map"].outputs[0], nodes["Principled BSDF"].inputs[5])    
    links.new(nodes["COL"].outputs[1], nodes["Principled BSDF"].inputs[4])    
    links.new(nodes["ROUGHNESS"].outputs[0], nodes["Principled BSDF"].inputs[2])    
    links.new(nodes["Texture Coordinate"].outputs[2], nodes[".simple_uv_mapping"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["COL"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["METALNESS"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["NRM16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["ROUGHNESS"].inputs[0])    

    return new_mat

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

    material_name = "MetalGalvanizedSteelWorn001"
    background_mat_root = os.path.join(
        bpy.path.abspath("//"),
        "assets",
        "Raw_materials",
        "Dishes",
        material_name,
    )
    # Create a material for the objeect
    galvanizedsteel = create_galvanizedsteel(imgs_path = background_mat_root, material_name = material_name)
    obj.data.materials.append(galvanizedsteel)

    # Render the scene
    data = bproc.renderer.render()

    # Save the image
    save_image(data, output_file)

if __name__ == "__main__":
    object_file = r"\assets\Raw_objects\Monkey.obj"
    output_file = r"\output_imgs\000006.png"
    main(object_file, output_file)
