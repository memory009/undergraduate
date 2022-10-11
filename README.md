# undergraduate
本文档主要用于本科阶段的项目记录以及未来项目的规划
<br>

## 致谢

 - [Hanwei Zhang](https://github.com/hanwei0912)
 - [Qidong Huang](https://github.com/shikiw)
 <br>

## 目前已完成工作：
## Carla
* Carla-0.9.10.1预编译版本搭建（ubuntu20.04）
* Carla-0.9.10.1（build from source）+UnrealEngine搭建（ubuntu20.04）
* Carla-0.9.13 预编译版本搭建（windows 11）
* Carla中对Carla世界的修改，e.g.对天气的修改，车辆的生成（单辆）
* Carla中获取车辆的位置信息，调用automatic_control，实现车辆（单辆）自动驾驶，并输出其实时点云消息以及2D图像
<br>
* Carla学习实时进度[点击这里](https://github.com/memory009/Carla-notebook)

## 论文研读
## Shape-invariant 3D Adversarial Point Clouds(Black-box query-based attack由于显存不够未完成代码复现，White-box attack,Black-box transfer-based attack完成)
* [code- https://github.com/shikiw/SI-Adv]( https://github.com/shikiw/SI-Adv)  
![figure1](https://github.com/memory009/undergraduate/blob/main/figure/Shape-invariant%203D%20Adversarial%20Point%20Clouds.png)
* modelnet40的点云可视化结果
![figure2](https://github.com/memory009/undergraduate/blob/main/figure/modelnet40%20airplane%E5%8F%AF%E8%A7%86%E5%8C%96.png)
<br>

## Geometry-Aware Generation ofAdversarial PointClouds(未完成代码复现)
* [code-https://github.com/Daniel-Liu-c0deb0t/Adversarial-point-perturbations-on-3D-objects ](https://github.com/Daniel-Liu-c0deb0t/Adversarial-point-perturbations-on-3D-objects)
![figure3](https://github.com/memory009/undergraduate/blob/main/figure/Geometry-Aware%20Generation%20ofAdversarial%20PointClouds.png)
<br>

## 经验
* Shape-invariant 3D Adversarial Point Clouds  
配置该论文环境的时候，可能出现```RuntimeError: CUDA error: no kernel image is available for execution on the device```的问题，出现该问题的原因是pytorch版本与rtx3060不兼容。
```
#使用以下方法卸载原有pytorch，更换为适配的版本
conda uninstall *torch* cudatoolkit
pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

* carla环境配置的时候可能会因为python版本不兼容或环境问题报错，若报错为```no moudle name carla```，则是因为carla没有安装到python的库里面，此时需要安装carla/PythonAPI/carla/dist中的```carla-0.9.10-py3.7-linux-x86_64.egg```,为减少安装时候造成的一系列错误，强烈建议使用conda新建虚拟环境进行安装
```
conda create -n carla python=3.7
conda activate carla 
pip3 install -e ~/carla/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64
```
* [windows下配置carla点击这里](https://github.com/memory009/CARLA-installation-windows-#readme)

## 未来工作计划
### 2022.10.9
* 获取其他状态下Carla输出的点云信息(e.g.加入多车辆以及行人干扰情况下Carla点云输出的获取)
* 尝试使用Carla复现detection以及classification任务
* evaluate model的确立(first: model can run; second: model can be evaluated)
* 



