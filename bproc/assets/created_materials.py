def CeramicPlainWhite001_2K():
    import bpy
    new_mat = bpy.data.materials.get('CeramicPlainWhite001_2K')
    if not new_mat:
        new_mat = bpy.data.materials.new('CeramicPlainWhite001_2K')
        
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
    new_node.subsurface_method = 'RANDOM_WALK_SKIN'
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = 0.5
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Textures'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Textures'
    new_node.select = False
    new_node.width = 300.0000305175781

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('CeramicPlainWhite001_COL_2K')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('CeramicPlainWhite001_DISP16_2K')
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
    new_node.location = (-650.0, -1100.0)
    new_node.name = 'DISP16'
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
    new_node.image = bpy.data.images.get('CeramicPlainWhite001_GLOSS_2K')
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
    new_node.location = (-650.0, -400.0)
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('CeramicPlainWhite001_NRM_2K')
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
    new_node.location = (-650.0, -750.0)
    new_node.name = 'NRM'
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
    new_node.image = bpy.data.images.get('CeramicPlainWhite001_REFL_2K')
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
    new_node.location = (-650.0, -50.0)
    new_node.name = 'REFL'
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

    new_node = nodes.new(type='ShaderNodeDisplacement')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1100.0)
    new_node.name = 'Displacement'
    new_node.select = False
    new_node.space = 'OBJECT'
    new_node.width = 140.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = 0.5
    new_node.inputs[2].default_value = 0.0
    new_node.inputs[3].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeNormalMap')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -750.0)
    new_node.name = 'Normal Map'
    new_node.select = False
    new_node.space = 'TANGENT'
    new_node.width = 150.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = [0.5, 0.5, 1.0, 1.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeInvert')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Invert Gloss'
    new_node.location = (-300.0, -400.0)
    new_node.name = 'Invert Gloss'
    new_node.select = False
    new_node.width = 140.0
    new_node.inputs[0].default_value = 1.0
    new_node.inputs[1].default_value = [0.0, 0.0, 0.0, 1.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]

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

    new_node = nodes.new(type='ShaderNodeRGBCurve')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-340.0, 20.0)
    map = new_node.mapping
    map.clip_max_x = 1.0
    map.clip_max_y = 1.0
    map.clip_min_x = 0.0
    map.clip_min_y = 0.0
    map.tone = 'STANDARD'
    map.use_clip = True                
    map_c = map.curves[0]
    map_c.points.new(0.0, 0.0)
    map_c.points.new(1.0, 1.0)
    removed_start = removed_end = False
    for i in range(len(map_c.points) - 1, -1, -1):
        p = map_c.points[i]
        if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
            map_c.points.remove(p)
            removed_start = True
        if not removed_end and p.location[0] == 1 and p.location[1] == 1:
            map_c.points.remove(p)
            removed_end = True                    
    map_c = map.curves[1]
    map_c.points.new(0.0, 0.0)
    map_c.points.new(1.0, 1.0)
    removed_start = removed_end = False
    for i in range(len(map_c.points) - 1, -1, -1):
        p = map_c.points[i]
        if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
            map_c.points.remove(p)
            removed_start = True
        if not removed_end and p.location[0] == 1 and p.location[1] == 1:
            map_c.points.remove(p)
            removed_end = True                    
    map_c = map.curves[2]
    map_c.points.new(0.0, 0.0)
    map_c.points.new(1.0, 1.0)
    removed_start = removed_end = False
    for i in range(len(map_c.points) - 1, -1, -1):
        p = map_c.points[i]
        if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
            map_c.points.remove(p)
            removed_start = True
        if not removed_end and p.location[0] == 1 and p.location[1] == 1:
            map_c.points.remove(p)
            removed_end = True                    
    map_c = map.curves[3]
    map_c.points.new(0.0, 0.0)
    map_c.points.new(1.0, 1.0)
    removed_start = removed_end = False
    for i in range(len(map_c.points) - 1, -1, -1):
        p = map_c.points[i]
        if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
            map_c.points.remove(p)
            removed_start = True
        if not removed_end and p.location[0] == 1 and p.location[1] == 1:
            map_c.points.remove(p)
            removed_end = True                    
    map.update()
    new_node.name = 'RGB Curves'
    new_node.select = False
    new_node.width = 240.0
    new_node.inputs[0].default_value = 1.0
    new_node.inputs[1].default_value = [1.0, 1.0, 1.0, 1.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]

    # Links :

    links.new(nodes["Principled BSDF"].outputs[0], nodes["Material Output"].inputs[0])    
    links.new(nodes["COL"].outputs[0], nodes["Principled BSDF"].inputs[0])    
    links.new(nodes["DISP16"].outputs[0], nodes["Displacement"].inputs[0])    
    links.new(nodes["Displacement"].outputs[0], nodes["Material Output"].inputs[2])    
    links.new(nodes["REFL"].outputs[0], nodes["Principled BSDF"].inputs[1])    
    links.new(nodes["NRM"].outputs[0], nodes["Normal Map"].inputs[1])    
    links.new(nodes["Normal Map"].outputs[0], nodes["Principled BSDF"].inputs[5])    
    links.new(nodes["COL"].outputs[1], nodes["Principled BSDF"].inputs[4])    
    links.new(nodes["GLOSS"].outputs[0], nodes["Invert Gloss"].inputs[1])    
    links.new(nodes["Invert Gloss"].outputs[0], nodes["Principled BSDF"].inputs[2])    
    links.new(nodes["Texture Coordinate"].outputs[2], nodes[".simple_uv_mapping"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["COL"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["DISP16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["GLOSS"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["NRM"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["REFL"].inputs[0])    
    links.new(nodes["RGB Curves"].outputs[0], nodes["Principled BSDF"].inputs[13])    

def MetalCladdingFrame002_2K(): 
    import bpy
    new_mat = bpy.data.materials.get('MetalCladdingFrame002_2K')
    if not new_mat:
        new_mat = bpy.data.materials.new('MetalCladdingFrame002_2K')
        
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
    new_node.subsurface_method = 'RANDOM_WALK_SKIN'
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = 0.5
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Textures'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Textures'
    new_node.select = False
    new_node.width = 300.0000305175781

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_BUMP16_2K')
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
    new_node.location = (-650.0, -1450.0)
    new_node.name = 'BUMP16'
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
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_COL_2K')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_DISP16_2K')
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
    new_node.location = (-650.0, -1100.0)
    new_node.name = 'DISP16'
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
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_GLOSS_2K')
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
    new_node.location = (-650.0, -400.0)
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_NRM_2K')
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
    new_node.location = (-650.0, -750.0)
    new_node.name = 'NRM'
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
    new_node.image = bpy.data.images.get('MetalCladdingFrame002_REFL_2K')
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
    new_node.location = (-650.0, -50.0)
    new_node.name = 'REFL'
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

    new_node = nodes.new(type='ShaderNodeDisplacement')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1100.0)
    new_node.name = 'Displacement'
    new_node.select = False
    new_node.space = 'OBJECT'
    new_node.width = 140.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = 0.5
    new_node.inputs[2].default_value = 0.0
    new_node.inputs[3].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeNormalMap')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -750.0)
    new_node.name = 'Normal Map'
    new_node.select = False
    new_node.space = 'TANGENT'
    new_node.width = 150.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = [0.5, 0.5, 1.0, 1.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeInvert')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Invert Gloss'
    new_node.location = (-300.0, -400.0)
    new_node.name = 'Invert Gloss'
    new_node.select = False
    new_node.width = 140.0
    new_node.inputs[0].default_value = 1.0
    new_node.inputs[1].default_value = [0.0, 0.0, 0.0, 1.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]

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
    links.new(nodes["DISP16"].outputs[0], nodes["Displacement"].inputs[0])    
    links.new(nodes["Displacement"].outputs[0], nodes["Material Output"].inputs[2])    
    links.new(nodes["REFL"].outputs[0], nodes["Principled BSDF"].inputs[1])    
    links.new(nodes["NRM"].outputs[0], nodes["Normal Map"].inputs[1])    
    links.new(nodes["Normal Map"].outputs[0], nodes["Principled BSDF"].inputs[5])    
    links.new(nodes["COL"].outputs[1], nodes["Principled BSDF"].inputs[4])    
    links.new(nodes["GLOSS"].outputs[0], nodes["Invert Gloss"].inputs[1])    
    links.new(nodes["Invert Gloss"].outputs[0], nodes["Principled BSDF"].inputs[2])    
    links.new(nodes["Texture Coordinate"].outputs[2], nodes[".simple_uv_mapping"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["BUMP16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["COL"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["DISP16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["GLOSS"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["NRM"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["REFL"].inputs[0])    

def MetalGalvanizedSteelWorn001_1K():
    import bpy
    new_mat = bpy.data.materials.get('MetalGalvanizedSteelWorn001_1K')
    if not new_mat:
        new_mat = bpy.data.materials.new('MetalGalvanizedSteelWorn001_1K')
        
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
    new_node.subsurface_method = 'RANDOM_WALK_SKIN'
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = 0.5
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Textures'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Textures'
    new_node.select = False
    new_node.width = 300.0000305175781

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_COL_1K_METALNESS')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_METALNESS_1K_METALNESS')
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
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_NRM16_1K_METALNESS')
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
    new_node.image = bpy.data.images.get('MetalGalvanizedSteelWorn001_ROUGHNESS_1K_METALNESS')
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
    new_node.width = 151.07217407226562
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Texture Projection/Mapping'
    new_node.label_size = 20
    new_node.location = (-334.32275390625, 61.22723388671875)
    new_node.name = 'Texture Projection/Mapping.001'
    new_node.width = 211.0721435546875

    new_node = nodes.new(type='ShaderNodeTexCoord')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.from_instancer = False
    new_node.location = (-1250.0, 300.0)
    new_node.name = 'Texture Coordinate.001'
    new_node.object = None
    parent = nodes.get('Texture Projection/Mapping.001')
    if parent:
        new_node.parent = parent
        while True:
            new_node.location += parent.location
            if parent.parent:
                parent = parent.parent
            else:
                break                    
    new_node.select = False
    new_node.width = 151.07217407226562
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[5].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[6].default_value = [0.0, 0.0, 0.0]

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

def WoodFlooringAshSuperWhite001_2K():
    import bpy
    new_mat = bpy.data.materials.get('WoodFlooringAshSuperWhite001_2K')
    if not new_mat:
        new_mat = bpy.data.materials.new('WoodFlooringAshSuperWhite001_2K')
        
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
    new_node.subsurface_method = 'RANDOM_WALK_SKIN'
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.inputs[1].default_value = 0.0
    new_node.inputs[2].default_value = 0.5
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

    new_node = nodes.new(type='NodeFrame')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Textures'
    new_node.label_size = 20
    new_node.location = (0.0, 0.0)
    new_node.name = 'Textures'
    new_node.select = False
    new_node.width = 300.0000305175781

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_AO_2K')
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
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_BUMP16_2K')
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
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_COL_2K')
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
    new_node.width = 240.0
    new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[1].default_value = 0.0

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_DISP16_2K')
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
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_GLOSS_2K')
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

    new_node = nodes.new(type='ShaderNodeTexImage')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.extension = 'REPEAT'
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_NRM_2K')
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
    new_node.image = bpy.data.images.get('WoodFlooringAshSuperWhite001_REFL_2K')
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
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = [0.5, 0.5, 0.5]
    new_node.inputs[2].default_value = 0.0
    new_node.inputs[3].default_value = 0.0
    new_node.inputs[4].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[5].default_value = [0.0, 0.0, 0.0]
    new_node.inputs[6].default_value = [0.5, 0.5, 0.5, 1.0]
    new_node.inputs[7].default_value = [0.5, 0.5, 0.5, 1.0]
    """
    new_node.inputs[8].default_value = <Euler (x=0.0000, y=0.0000, z=0.0000), order='XYZ'>
    new_node.inputs[9].default_value = <Euler (x=0.0000, y=0.0000, z=0.0000), order='XYZ'>
    new_node.outputs[0].default_value = 0.0
    new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[2].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
    new_node.outputs[3].default_value = <Euler (x=0.0000, y=0.0000, z=0.0000), order='XYZ'>"""

    new_node = nodes.new(type='ShaderNodeDisplacement')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1450.0)
    new_node.name = 'Displacement'
    new_node.select = False
    new_node.space = 'OBJECT'
    new_node.width = 140.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = 0.5
    new_node.inputs[2].default_value = 0.0
    new_node.inputs[3].default_value = [0.0, 0.0, 0.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeNormalMap')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.location = (-300.0, -1100.0)
    new_node.name = 'Normal Map'
    new_node.select = False
    new_node.space = 'TANGENT'
    new_node.width = 150.0
    new_node.inputs[0].default_value = 0.0
    new_node.inputs[1].default_value = [0.5, 0.5, 1.0, 1.0]
    new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

    new_node = nodes.new(type='ShaderNodeInvert')
    new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    new_node.label = 'Invert Gloss'
    new_node.location = (-300.0, -750.0)
    new_node.name = 'Invert Gloss'
    new_node.select = False
    new_node.width = 140.0
    new_node.inputs[0].default_value = 1.0
    new_node.inputs[1].default_value = [0.0, 0.0, 0.0, 1.0]
    new_node.outputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]

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
    links.new(nodes["COL"].outputs[0], nodes["COLOR * AO"].inputs[6])    
    links.new(nodes["AO"].outputs[0], nodes["COLOR * AO"].inputs[7])    
    links.new(nodes["COLOR * AO"].outputs[2], nodes["Principled BSDF"].inputs[0])    
    links.new(nodes["DISP16"].outputs[0], nodes["Displacement"].inputs[0])    
    links.new(nodes["Displacement"].outputs[0], nodes["Material Output"].inputs[2])    
    links.new(nodes["REFL"].outputs[0], nodes["Principled BSDF"].inputs[1])    
    links.new(nodes["NRM"].outputs[0], nodes["Normal Map"].inputs[1])    
    links.new(nodes["Normal Map"].outputs[0], nodes["Principled BSDF"].inputs[5])    
    links.new(nodes["COL"].outputs[1], nodes["Principled BSDF"].inputs[4])    
    links.new(nodes["GLOSS"].outputs[0], nodes["Invert Gloss"].inputs[1])    
    links.new(nodes["Invert Gloss"].outputs[0], nodes["Principled BSDF"].inputs[2])    
    links.new(nodes["Texture Coordinate"].outputs[2], nodes[".simple_uv_mapping"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["AO"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["BUMP16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["COL"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["DISP16"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["GLOSS"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["NRM"].inputs[0])    
    links.new(nodes[".simple_uv_mapping"].outputs[0], nodes["REFL"].inputs[0])    

