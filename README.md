# 基于blender平台的数字人模仿系统

> ​		本数字人模仿系统的功能可以做到数字人 - 机器人 - 动作者 三者的动作协同，达到一种数字人和机器人均模仿动作者面部表情动作的效果，如下图所示。本系统首先通过相机采集一段类似图一动作者的图像帧，可以是一段离线视频，也可以是相机实时输入的图像帧。
>
> ​		获取到图像后，通过深度学习算法对图像中的人脸信息进行姿态信息获取，如面部的blendshape和头部的姿态角。这些姿态信息通过blender中的api接口可以直接驱动数字人模仿动作者的动作。同样是这些姿态信息，用来对表情机器人舵机命令的转换，而后通过串口同样来控制表情机器人的面部动作。从宏观的角度来看，它可以作为未来构建数字孪生世界的一个重要技术基础。

![image-20231117144641221](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231117144641221.png)

  数字人模仿系统示意图



## 一、环境配置

> ​		此系统所依赖的运行环境为blender，python3。具体所依赖的python环境为anaconda构建的虚拟环境，通过虚拟环境与blender配合来一起达到控制数字人的效果。以下简述环境安装顺序的依赖

1. 安装anaconda，参考此[csdn链接](https://blog.csdn.net/sinat_39620217/article/details/131675175)或者其它百度链接均可

2. 安装blender，参考此[链接](https://docs.blender.org/manual/zh-hans/3.0/getting_started/installing/index.html)或者其它百度链接均可

3. 查看blender中python版本（下步创建conda环境要一致），参考[此链接](https://baijiahao.baidu.com/s?id=1682972112422016241&wfr=spider&for=pc)，假设等于***3.10.13***

4. 建立conda环境，命令行终端创建conda环境 具体命令：

   ```shell
   conda create -n blender_rena python==3.10.13
   ```

5. 命令行终端，激活建立的conda环境具体命令：

   ```shell
   conda activate blender_rena
   ```

6. 虚拟环境中安装所需要的库，接着第5步中终端：

   ```shell
   pip install -r requirements.txt
   ```

至此，本系统锁依赖的python运行环境均已满足。



此外，本产品提供的软件安装包结构目录如下图所示：

![image-20231119164156804](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231119164156804.png)



## 二、运行仿真数字人

1. 运行blender软件  
2. 选择软件上方脚本（scripting）选项
3. 关联RenaBlender文件夹中的mimic_blender.py文件
4. 点击“三角形”运行按钮即可达到图一的效果



## 三、win10详细安装流程

接下以本人win10系统笔记本举例，从零配置此表情模仿系统。

1. 安装blender

   + 进入blender官网https://www.blender.org/download/，点击download下载安装包

   + 双击运行exe安装包，根据引导完成安装, 用户可自行修改安装目录

     点击blender图标，进入软件 --> 点击脚本（scripting）可以进行如下页面，右下角观察python版本为3.10.9
     ![image-20231117160224783](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231117160224783.png)


   2. 如下图所示，在RenaBlender\ulaa_head中，使用blender打开我们提供的数字人模型
      ![image-20231117172124469](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231117172124469.png)

   

   3. 选择软件上方脚本（scripting）选项，按下图所示，关联RenaBlender文件下此mimic_blender.py文件
      ![image-20231117172515870](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231117172515870.png)



4. 点击“三角形”运行按钮即可达到图一的效果
   ![image-20231119202304893](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231119202304893.png)



5. 运行效果如下图所示
   ![image-20231117144641221](https://littlecucu.oss-cn-shanghai.aliyuncs.com/img/image-20231117144641221.png)

