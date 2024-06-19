import blenderproc as bproc
import bpy
import random

#We create the table 
bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD')# The newly created object will be the active object, so we can rename it
# Select it, give it a name and dimensions
table = bpy.context.active_object
table.name = "Table"
table_scale = (60, 60, 1)
table.scale = table_scale

# We create the n random colors for the background 
n_table_colors = 20
table_colors = []
for i in range (0,n_table_colors):
    new_table_color = bpy.data.materials.new("")
    new_table_color.diffuse_color = (random.random(),random.random(),random.random(),1)
    table_colors.append(new_table_color)

# Create n tables with n colors, this won't actually be the code, because we'll just have one table that changes colors
for i in range (0,n_table_colors):
    table.data.materials.append(table_colors[i])