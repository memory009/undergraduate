import glob
import carla
import random
import numpy as np
import os
import sys
import time

actor_list = []

try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()

    # #load a Tesla-model3
    # bp = blueprint_library.filter("model3")[0]
    spawn_point = world.get_map().get_spawn_points()
    #print(spawn_point)

    # vehicle = world.spawn_actor(bp,spawn_point)
    # #load autopolot
    # vehicle.set_autopilot(True)
    # time.sleep(100)

    for i in range(50):
        vehicle_bp = random.choice(blueprint_library.filter('vehicle'))
        npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_point))
        actor_list.append(npc)

        for v in world.get_actors().filter('*vehicle*'):
            v.set_autopilot(True)

    time.sleep(100)


finally:
    for actor in actor_list:
        actor.destory()
    print("All cleaned up")