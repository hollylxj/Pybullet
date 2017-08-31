import os
import sawyer
from math import pi


##########################
## Setup Sawyer simulator
##########################
#physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
sawyer.connect()
gravity = (0, 0, -9.8)
timeStep = 0.0002
urdfFile = "/Users/holly/sawyer.git/bin/resources/sawyer/sawyer.urdf"
#print(os.getcwd())
#os.chdir("/Users/holly/sawyer.git/bin/resources/sawyer")
sawyer.setup(gravity, timeStep, urdfFile)
#sawyerId = p.loadURDF("sawyer.urdf", useFixedBase = 1)
#p.setRealTimeSimulation(1,sawyerId)



############################
## Reseting initial position
############################
sawyer.resetPos(0.5)
#time.sleep(1)

[q,dq,sum_dq] = sawyer.readQdQ()
print('q:::',q)

raw_input( "Hit Enter to proceed:")



#######################
#Preparation for torque mode control
#######################
sawyer.disableMotors()
# set 0 Torque, initial Q and dQ
#r.set(PY_JOINT_TORQUES_COMMANDED_KEY,"{} {} {} {} {} {} {}".format(0,0,0,0,0,0,0))
#r.set(PY_JOINT_ANGLES_KEY, q)
#r.set(PY_JOINT_VELOCITIES_KEY, dq)


#######################
## input desired position and orientation
#######################
pos = (0.0, 0.8, 0.0)
orn = (pi/4, pi/4, pi/4)
sawyer.setDesPosOrn(pos, orn)


###################
### TODO: ./sawyer sawyer.urdf
### Run sawyer.cpp
####################


########################
## START MOVING
########################
sawyer.moveTo()

while(1):
    None
sawyer.disconnect()

