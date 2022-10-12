# Carla-notebook
Thanks for [Mr. Sihao Wu](https://github.com/WilliamWu96) and [Ms. Hanwei Zhang](https://github.com/hanwei0912)'s contribution to this project !


## Launching CARLA and connecting the client(2022.10.10)

launch CARLA from the command line
```bash
cd /carla-0.9.10.1
./CarlaUE4.sh                      # or use 'sh CarlaUE4.sh' to launch it
``` 

To manipulate CARLA through the Python API, we need to connect the Python client to the server through an open port. The client controls the simulator through the client and world objects Open a Python notebook or create a new script, then add the following code to the start of the script or the main function:
```bash
import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
```

The port can be chosen as any available port and is set to 2000 by default, you can also choose a host different from localhost by using a computer's IP address. This way, the CARLA server can be run on a networked machine, while the python client can be run from a personal computer. 

## Loading a map
In the CARLA API, the world object provides access to all elements of the simulation, including the map, objects within the map, such as buildings, traffic lights, vehicles and pedestrians. The CARLA server normally loads a default map (normally Town10). If you want to launch CARLA with an alternate map, use the config.py script:
```bash
./config.py --map Town05 
```

we also can use the world object to load a map from the client:
```bash
world.load_world('Town05')
```
find more information about CARLA map [here](https://carla.readthedocs.io/en/latest/core_map/) 


<s> The spectator and its properties can be accessed and manipulated through the Python API: 
#通过 Python API 访问和操作观众及其属性
```bash
# Retrieve the spectator object
spectator = world.get_spectator()

# Get the location and rotation of the spectator through its transform
transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation

# Set the spectator with an empty transform
spectator.set_transform(carla.Transform())
# This will set the spectator at the origin of the map, with 0 degrees
# pitch, yaw and roll - a good way to orient yourself in the map
```
</s>

## Get the blueprint library and the spawn points for the map（2022.10.11-10.12 under construction）
* If you want to spawn(生成) Actors ，firstly you must defind its Blueprint
```
# load blueprint for all objects
blueprint_library = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points() 
```

## Get the blueprint for the vehicle you want(e.g. mercedes-benz)
```
vehicle_bp = blueprint_library.find('vehicle.mercedes-benz.coupe')
# Try spawning the vehicle at a randomly chosen spawn point
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
```

##  Move the spectator behind the vehicle 
```
spectator = world.get_spectator() 
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=2.5)),vehicle.get_transform().rotation) 
spectator.set_transform(transform) 
```

## Change the weather
```bash
weather = carla.WeatherParameters(cloudiness=10.0,precipitation=10.0,fog_density=10.0)
world.set_weather(weather)
```

## Add traffic to the simulation
```
for i in range(30): 
    vehicle_bp = random.choice(bp_lib.filter('vehicle')) 
    npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points)) 
```

## Set the all vehicles in motion using the Traffic Manager
```
for v in world.get_actors().filter('*vehicle*'): 
    v.set_autopilot(True) 
```

## Destroy Actor
Remember to destroy the car after running the script, otherwise it will always exist in the simulation world, which may affect the operation of other scripts
```
# destory single Actor
vehicle.destroy()
# if you have many actors,you should put them into a list,and destroy them together
client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
```

## bulid sensor 
we can put various of sensor in the car,so there are many carla's sensor.  
you can learn more information about sensor in [here](https://carla.readthedocs.io/en/latest/python_api/)  
here are some introduce about sensor
![figure1](https://github.com/memory009/undergraduate/blob/main/figure/sensor.png)
* Spawn an RGB cammera with an offset from the vehicle center
```
camera_bp = bp_lib.find('sensor.camera.rgb') 
camera_init_trans = carla.Transform(carla.Location(z=2))
camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=vehicle)
```

* Start the camera saving data to disk
```
camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))
```

* Stop the camera when we've recorded enough data
```
camera.stop()
```

## cautious
```bash
The following presumes that CARLA is running in the default asynchronous mode. If you have engaged synchronous mode, some of the code in the following sections might not work as expected.
# 以下假设 CARLA 在默认异步模式下运行。如果您使用了同步模式，以下部分中的某些代码可能无法按预期工作。
```
