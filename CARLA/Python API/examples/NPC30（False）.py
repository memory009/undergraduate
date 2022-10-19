import carla
import random
import math
import time

#使用carla客户端对象设置客户端
#默认是与本机上的carla进行通信，如果在单独的机器上运行客户端，则可以使用网络机器的IP地址。第二个参数是端口号，默认情况下服务器在端口2000运行，可以在启动CARLA时在设置中更改此选项
client = carla.Client('localhost', 2000)


#客户端对象可用于许多功能，包括加载新地图、记录模拟和初始化交通管理器：
# client.load_world('Town07')
# client.start_recorder('recording.log')

#使用客户端对象检索世界对象
world = client.get_world()
bp_lib = world.get_blueprint_library()

#生成点
spawn_points = world.get_map().get_spawn_points()
#从蓝图中搞一辆车出来，这里搞的是一辆林肯的车
vehicle_bp = bp_lib.find('vehicle.mercedes-benz.coupe')
# vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020')
#try在这里是因为怕生成汽车的点已经被占用，例如在另一辆车上或者在树上
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
#vehicle.set_autopilot(True)

#加入一个旁观者,以便可以通过wsad和鼠标来移动视角
spectator = world.get_spectator()
#指定生成汽车的位置
#transform = random.choice(world.get_map().get_spawn_points())
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=2.5)),vehicle.get_transform().rotation)
#把旁观者放在车子正后方
spectator.set_transform(transform)

#添加模拟车辆
for i in range(3):
    vehicle_bp = random.choice(bp_lib.filter('vehicle'))
    npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
    #npc.set_autopilot(True)

#使用交通管制设置所有汽车的motion
for v in world.get_actors().filter('*vehicle*'):
    v.set_autopilot(True)



# #世界对象可用于访问模拟中的对象，例如天气、车辆、交通信号灯、建筑物和使用其多种方法的地图
# level = world.get_map()
# weather = world.get_weather()
# blueprint_library = world.get_blueprint_library()

