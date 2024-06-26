""" Codigo de Nacho, para importat materiales de blender a blenderproc
    Hay que escribir las rutas a las diferentes carpetas de texturas y normales que tengan nuestos materiales"""


import bpy
import os

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