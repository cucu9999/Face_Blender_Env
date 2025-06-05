
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

def update_pico_bs(pico_bs_dict):
    """
    将 pico_bs_dict（键是 Pico_BS.name，值是权重）
    映射到 Blender_BS 枚举上。返回一个 Blender_BS.name -> value 的字典。
    """

    # 1) 初始化：所有 Blender_BS 名称都置为 0
    blender_bs_dict = {bs.name: 0 for bs in Blender_BS}

    # 2) Pico->Blender 的映射表（只映射前 52 项）
    pico2blend= {
        'EyeLookDown_L':   'eyeLookDownLeft',
        'NoseSneer_L':     'noseSneerLeft',
        'EyeLookIn_L':     'eyeLookInLeft',
        'BrowInnerUp':     'browInnerUp',
        'BrowDown_R':      'browDownRight',
        'MouthClose':      'mouthClose',
        'MouthLowerDown_R':'mouthLowerDownRight',
        'JawOpen':         'jawOpen',
        'MouthUpperUp_R':  'mouthUpperUpRight',
        'MouthShrugUpper':'mouthShrugUpper',
        'MouthFunnel':     'mouthFunnel',
        'EyeLookIn_R':     'eyeLookInRight',
        'EyeLookDown_R':   'eyeLookDownRight',
        'NoseSneer_R':     'noseSneerRight',
        'MouthRollUpper':  'mouthRollUpper',
        'JawRight':        'jawRight',
        'BrowDown_L':      'browDownLeft',
        'MouthShrugLower': 'mouthShrugLower',
        'MouthRollLower':  'mouthRollLower',
        'MouthSmile_L':    'mouthSmileLeft',
        'MouthPress_L':    'mouthPressLeft',
        'MouthSmile_R':    'mouthSmileRight',
        'MouthPress_R':    'mouthPressRight',
        'MouthDimple_R':   'mouthDimpleRight',
        'MouthLeft':       'mouthLeft',
        'JawForward':      'jawForward',
        'EyeSquint_L':     'eyeSquintLeft',
        'MouthFrown_L':    'mouthFrownLeft',
        'EyeBlink_L':      'eyeBlinkLeft',
        'CheekSquint_L':   'cheekSquintLeft',
        'BrowOuterUp_L':   'browOuterUpLeft',
        'EyeLookUp_L':     'eyeLookUpLeft',
        'JawLeft':         'jawLeft',
        'MouthStretch_L':  'mouthStretchLeft',
        'MouthPucker':     'mouthPucker',
        'EyeLookUp_R':     'eyeLookUpRight',
        'BrowOuterUp_R':   'browOuterUpRight',
        'CheekSquint_R':   'cheekSquintRight',
        'EyeBlink_R':      'eyeBlinkRight',
        'MouthUpperUp_L':  'mouthUpperUpLeft',
        'MouthFrown_R':    'mouthFrownRight',
        'EyeSquint_R':     'eyeSquintRight',
        'MouthStretch_R':  'mouthStretchRight',
        'CheekPuff':       'cheekPuff',
        'EyeLookOut_L':    'eyeLookOutLeft',
        'EyeLookOut_R':    'eyeLookOutRight',
        'EyeWide_R':       'eyeWideRight',
        'EyeWide_L':       'eyeWideLeft',
        'MouthRight':      'mouthRight',
        'MouthDimple_L':   'mouthDimpleLeft',
        'MouthLowerDown_L':'mouthLowerDownLeft',
        'TongueOut':       'tongueOut',
    }

    # 3) 把 pico 的值写入 blender_bs_dict
    for pico_name, pico_val in pico_bs_dict.items():
        blender_name = pico2blend.get(pico_name)
        if blender_name:
            blender_bs_dict[blender_name] = pico_val
    return blender_bs_dict

def update_arkit_bs(arkit_bs_dict):
    blender_bs_dict = {bs.name: 0 for bs in Blender_BS}
    arkit2blend = {
        "EyeBlinkLeft":    "eyeBlinkLeft",
        "EyeLookDownLeft": "eyeLookDownLeft",
        "EyeLookInLeft":   "eyeLookInLeft",
        "EyeLookOutLeft":  "eyeLookOutLeft",
        "EyeLookUpLeft":   "eyeLookUpLeft",
        "EyeSquintLeft":   "eyeSquintLeft",
        "EyeWideLeft":     "eyeWideLeft",
        "EyeBlinkRight":   "eyeBlinkRight",
        "EyeLookDownRight":"eyeLookDownRight",
        "EyeLookInRight":  "eyeLookInRight",
        "EyeLookOutRight": "eyeLookOutRight",
        "EyeLookUpRight":  "eyeLookUpRight",
        "EyeSquintRight":  "eyeSquintRight",
        "EyeWideRight":    "eyeWideRight",
        "JawForward":      "jawForward",
        "JawLeft":         "jawLeft",
        "JawRight":        "jawRight",
        "JawOpen":         "jawOpen",
        "MouthClose":      "mouthClose",
        "MouthFunnel":     "mouthFunnel",
        "MouthPucker":     "mouthPucker",
        "MouthLeft":       "mouthLeft",
        "MouthRight":      "mouthRight",
        "MouthSmileLeft":  "mouthSmileLeft",
        "MouthSmileRight": "mouthSmileRight",
        "MouthFrownLeft":  "mouthFrownLeft",
        "MouthFrownRight": "mouthFrownRight",
        "MouthDimpleLeft": "mouthDimpleLeft",
        "MouthDimpleRight":"mouthDimpleRight",
        "MouthStretchLeft":"mouthStretchLeft",
        "MouthStretchRight":"mouthStretchRight",
        "MouthRollLower":  "mouthRollLower",
        "MouthRollUpper":  "mouthRollUpper",
        "MouthShrugLower": "mouthShrugLower",
        "MouthShrugUpper": "mouthShrugUpper",
        "MouthPressLeft":  "mouthPressLeft",
        "MouthPressRight": "mouthPressRight",
        "MouthLowerDownLeft":  "mouthLowerDownLeft",
        "MouthLowerDownRight": "mouthLowerDownRight",
        "MouthUpperUpLeft":    "mouthUpperUpLeft",
        "MouthUpperUpRight":   "mouthUpperUpRight",
        "BrowDownLeft":    "browDownLeft",
        "BrowDownRight":   "browDownRight",
        "BrowInnerUp":     "browInnerUp",
        "BrowOuterUpLeft": "browOuterUpLeft",
        "BrowOuterUpRight":"browOuterUpRight",
        "CheekPuff":       "cheekPuff",
        "CheekSquintLeft": "cheekSquintLeft",
        "CheekSquintRight":"cheekSquintRight",
        "NoseSneerLeft":   "noseSneerLeft",
        "NoseSneerRight":  "noseSneerRight",
        "TongueOut":       "tongueOut",
}

    # 3) 把 arkit 的值写入 blender_bs_dict
    for arkit_name, arkit_val in arkit_bs_dict.items():
        blender_name = arkit2blend.get(arkit_name)
        if blender_name:
            blender_bs_dict[blender_name] = arkit_val
    return blender_bs_dict
