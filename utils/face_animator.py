import bpy
from Blendshape_Msgs import Blender_BS

# =========================== 驱动接口 ===========================
class Animator:
    def __init__(self, face_ob_name='Wolf3D_Head'):
        self.face_ob_name = face_ob_name
        self.face_ob = bpy.data.objects[face_ob_name]
        self.blender_bs_dict = {bs.name: 0 for bs in Blender_BS}

    # animation
    def face_animation(self, driven_bs_dict):
        '''
        driven_bs_dict: 驱动的面部姿态信息, type: dict, len: 52
        # driven_bs_dict的key要包含于blender_bs_dict的key
        '''

        shape_keys = self.face_ob.data.shape_keys.key_blocks
        for key, value in self.blender_bs_dict.items():
            driven_bs_dict[key] = min(driven_bs_dict[key], 1.0)
            shape_keys[key].value = driven_bs_dict[key]  # bs驱动数字人
            shape_keys[key].keyframe_insert(data_path='value')
# ==================================================================