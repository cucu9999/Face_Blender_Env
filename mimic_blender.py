import os
import sys
import bpy
import subprocess

def get_conda_env_path(env_name):
    try:
        result = subprocess.run(
            ["conda", "env", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"Error running conda command: {result.stderr}")

        for line in result.stdout.splitlines():
            if env_name in line:
                env_path = line.split()[-1]
                return f"{env_path}/lib/python3.10/site-packages"
        
        raise ValueError(f"Environment {env_name} not found")
    except Exception as e:
        return str(e)
    
env_path = "demo_renablender" # 虚拟环境名称 <---------------------------------------------
site_packages_path = get_conda_env_path(env_path)
blend_path = bpy.data.filepath
blend_dir = os.path.dirname(blend_path)

sys.path.append(site_packages_path)
sys.path.append(blend_dir+"/..")
# script_dir = os.path.dirname(__file__)
# sys.path.append(script_dir)

from utils.faceoperati import FaceMeshDetector, HeadPose
from utils.setcamera import SetCamera
from utils.animator import Animator
from utils.servo_control import Servo_Trans
import numpy as np



class AnimOperator(bpy.types.Operator):
    bl_idname = "wm.operator"
    bl_label = "Animation Operator"

    _timer = None
    _image = None
    _image_flag = False
    setcamera = SetCamera(0)
    facemeshdetector = FaceMeshDetector()
    animator = Animator()  # 数字人动画类实例
    headpose = HeadPose()
    servo_trans = Servo_Trans()
    servo_flag = False
    bs = None  # blendshapes系数
    lm = None  # landmarks坐标
    rm = None  # 旋转矩阵
    rpy_angles = [0, 0, 0]  # 欧拉角
    count = 1

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.001, window=context.window) # blender 刷新率
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):

        # 鼠标右键或者ESC键, 停止程序
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            self._image, self._image_flag = self.setcamera.start_camera()
            # print("图片：",self._image)
            # self._image = cv2.flip(self._image, 1) # flip the image
            self._image = self._image

            self.facemeshdetector.update(self._image, self._image_flag)
            self.lm, self.bs, self.rm = self.facemeshdetector.get_results()

            # result bs、pose
            if self.lm is not None and self.bs is not None and self.rm is not None:

                self.rpy_angles = self.headpose.pose_det(rm=self.rm)

                # 驱动数字人
                self.animator.face_animation(self.bs)
                self.animator.head_animation(self.rpy_angles)
                
                # -------------------------------------------------------------------------------------
                # 可能出问题的点，注释下面可解决，问题现象：blender闪退，报错信息也闪退。
                # -------------------------------------------------------------------------------------
                # self.facemeshdetector.visualize_results(self._image, self._image_flag, self.lm)

                # 如果仿真人头连接成功, 则驱动仿真人头硬件，默认false暂时不看。
                if self.servo_flag:
                    servo_msgs = self.servo_trans.trans(self.bs, self.rpy_angles)
                    self.servo_ctrl.send(servo_msgs)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager  
        wm.event_timer_remove(self._timer)  
        self.setcamera.stop_camera()
        unregister()
        print("程序结束")


classes = (
    AnimOperator,
)


def register():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
    bpy.ops.wm.operator()
