
import bpy
import os
import sys
import itertools

# 52bs的txt文件的绝对路径
bs_file_path = "/media/2T/yongtong/Rena/face_blender/bs_files/bs52_hongji.txt"
# utils文件夹的绝对路径
sys.path.append("/media/2T/yongtong/Rena/face_blender/utils")            

from face_animator import Animator
from Blendshape_Msgs import Blender_BS, Mediapipe_BS
from Reset_drivenBS import update_mp_bs


blender_bs_dict_zero = {bs.name: 0 for bs in Blender_BS}
mp_bs_dict_temp = {bs.name: 0 for bs in Mediapipe_BS}

def read_bs52_to_dict(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        values = line.strip().split() # 去除首尾空格并分割为数值列表
        assert len(values) == 52, f"读取文件每行有{len(float_values)}个数值, 而非52个!!!"
        float_values = [float(val) for val in values]

        # 创建新的字典，键为mediapipe_bs的键，值为对应的数值
        mp_bs_dict = {}
        for index, (key, value) in enumerate(mp_bs_dict_temp.items()):
            mp_bs_dict[key] = float_values[index]

        result.append(mp_bs_dict)

    # return result # [dict1, dict2, dict3, ...]
    return itertools.cycle(result)

# dict_list = read_bs52_to_dict(file_path)
# if dict_list:
#     print(dict_list[0])


# =========================== 虚拟人控制接口 ===========================
class AnimOperator(bpy.types.Operator):
    bl_idname = "wm.operator" 
    bl_label = "Animation Operator" 
    animator = Animator(face_ob_name='Wolf3D_Head')  # 数字人实例化
    result_cycle = read_bs52_to_dict(bs_file_path)
    _timer = None

    def execute(self, context):
        wm = context.window_manager
        # fps 设置
        self._timer = wm.event_timer_add(0.033, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        # 事件类型是单击鼠标右键或者ESC键, 停止插件运行
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            self.animator.face_animation(blender_bs_dict_zero)
            return {'CANCELLED'}

        # 事件类型是TIMER, 执行自定义操作
        if event.type == 'TIMER':
            mp_bs_dict = next(self.result_cycle)
            # print(len(mp_bs_dict), mp_bs_dict,"\n")
            self.driven_bs_dict = update_mp_bs(mp_bs_dict)
            # print(len(self.driven_bs_dict), self.driven_bs_dict,"\n")
            self.animator.face_animation(self.driven_bs_dict)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

def register():
    bpy.utils.register_class(AnimOperator)

def unregister():
    bpy.utils.unregister_class(AnimOperator)


# ---------------------------- 程序入口 --------------------------
if __name__ == "__main__":
    register()
    bpy.ops.wm.operator()
    # result_cycle = read_bs52_to_dict(file_path)
    # for i in range(1):
    #     print(next(result_cycle))