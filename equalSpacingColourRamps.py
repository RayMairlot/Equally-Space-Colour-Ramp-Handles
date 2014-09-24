import bpy


bl_info = {
    "name": "Evenly Space ColourRamp node handles",
    "description": "Evenly space colourramp node handles.",
    "author": "Ray Mairlot",
    "version": (1, 0),
    "blender": (2, 71, 0),
    "location": "Node Editor > Q over selected colour ramp node",
    "category": "Node"}
    
    

class equaliseColourRampOperator(bpy.types.Operator):
    """ Evenly space colourramp handles for the selected colour ramp node """
    bl_idname = "node.even_colour_ramp"
    bl_label = "Evenly space colourramp node handles"


    def execute(self, context):
        main(context)
        return {'FINISHED'}


def main(context):
    if context.active_node:  
        if context.active_node.type == "VALTORGB":                          
            handles = context.active_node.color_ramp.elements
            if len(handles)>1:

                increment = 1/(len(handles)-1)
                position = 0

                for handle in handles:
                    handle.position = position
                    position+=increment


def register():
    bpy.utils.register_class(equaliseColourRampOperator)

    kc = bpy.context.window_manager.keyconfigs.addon

    km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
    km.keymap_items.new("node.even_colour_ramp", 'Q', 'PRESS')



def unregister():
    bpy.utils.unregister_class(equaliseColourRampOperator)
    
    kc = bpy.context.window_manager.keyconfigs.addon
    kc.keymaps.remove(kc.keymaps['Node Editor'])
    


if __name__ == "__main__":
    register()



