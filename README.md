# Undergraduate
This document is mainly used for project records at the undergraduate level and planning for future projects
<br>

## Thanks

 - [Hanwei Zhang](https://github.com/hanwei0912)
 - [Qidong Huang](https://github.com/shikiw)
 <br>

## Completed work：
## Carla（2022.10.9）
* Environment configuration for Carla-0.9.10.1 precompiled version（ubuntu20.04）
* Environment configuration for Carla-0.9.10.1（build from source）+ UnrealEngine（ubuntu20.04）
* Environment configuration Carla-0.9.13 precompiled version（windows 11）
* Modify Carla's world;e.g.change the weather ，spawn vehicle（single）
* Get the location information of the vehicle in CARLA's world，use autopilot module,realize vehicle (single) autonomous driving，and output its real-time 3D point clouds message as well as RGB image(2D)
## Carla（2022.10.13）
* Carla's workload(https://github.com/memory009/undergraduate/tree/main/CARLA/carla-notebook)
* Spawn 50 npc in CARLA's world，use camera_sensor and opencv to get real-time data


# Paper list 
<details>
<summary>Shape-invariant 3D Adversarial Point Clouds(Uncompleted 'Black-box query-based attack' reproduction due to insufficient video memory;Finsh 'White-box attack','Black-box transfer-based attack')</summary>
* [code- https://github.com/shikiw/SI-Adv]( https://github.com/shikiw/SI-Adv)  
![figure1](https://github.com/memory009/undergraduate/blob/main/figure/Shape-invariant%203D%20Adversarial%20Point%20Clouds.png)
* Point cloud visualization results of modelnet40
![figure2](https://github.com/memory009/undergraduate/blob/main/figure/modelnet40%20airplane%E5%8F%AF%E8%A7%86%E5%8C%96.png)
<br>

<summary>Geometry-Aware Generation ofAdversarial PointClouds(Unfinished code reproduction)</summary>
* [code-https://github.com/Daniel-Liu-c0deb0t/Adversarial-point-perturbations-on-3D-objects ](https://github.com/Daniel-Liu-c0deb0t/Adversarial-point-perturbations-on-3D-objects)
![figure3](https://github.com/memory009/undergraduate/blob/main/figure/Geometry-Aware%20Generation%20ofAdversarial%20PointClouds.png)
<br>
</details>
 
## experience
* Shape-invariant 3D Adversarial Point Clouds  
When configuring environment，maybe emerge```RuntimeError: CUDA error: no kernel image is available for execution on the device```，The reason for this problem is pytorch version not compatible with GPU (nvidia RTX3060--mine)
```
#Use the following method to uninstall the original pytorch and replace it with the adapted version
conda uninstall *torch* cudatoolkit,
pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

* When the carla environment is configured, an error may be reported due to incompatible python versions or environmental problems，if error is```no moudle name carla```，this is because translater can't find carla's library in pythons enviroment'，so we should go to 'carla/PythonAPI/carla/dist'and find```carla-0.9.10-py3.7-linux-x86_64.egg```,in order to reduce a series of errors during installation, it is strongly recommended to use conda to create a new virtual environment for installation
```
conda create -n carla python=3.7
conda activate carla 
pip3 install -e ~/carla/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64
```
* [To configure carla under windows click here](https://github.com/memory009/CARLA-installation-windows-#readme)

## Next Move
### 2022.10.9
* Obtain 3D point clouds information output by Carla in other states (e.g. the acquisition of Carla point cloud output in the case of multi-vehicle and pedestrian interference)    --finished
* Try to use Carla to reproduce other people's detection and classification models
* Establishment evaluate model(first: model can run; second: model can be evaluated)
### 2022.10.17
* Solve the problem that the point cloud is too sparse to detect
* Run the 3D point clouds data obtained by carla and run an evaluate result on the detection
* Deploy the attack code to the previous problem

<details>
  <summary>什么是iuap design</summary>
  iuap design 是用友网络FED团队开发的企业级应用前端集成解决方案。
</details>


