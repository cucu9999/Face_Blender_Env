
from Blendshape_Msgs import Blender_BS, Mediapipe_BS



def update_mp_bs(mediapipe_bs_dict):
    blender_bs_dict = {bs.name: 0 for bs in Blender_BS}
    for key, value in mediapipe_bs_dict.items():
        # 检查该键是否在 Blender_BS_Dict 的 51 个键中
        if key in blender_bs_dict and key != "Basis":
            # 更新 Blender_BS_Dict 中对应键的值
            blender_bs_dict[key] = value
    driven_bs_dict = blender_bs_dict
    return driven_bs_dict

# driven_bs_dict = update_blender_bs(mediapipe_bs_dict, blender_bs_dict)
