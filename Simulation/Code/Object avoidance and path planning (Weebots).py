"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
 # from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import InertialUnit
import math
import time
import asyncio
from threading import Event,Timer
# create the Robot instance.
MAX_SPEED = 6.20
# get the time step of the current world.
TIMESTEP = 32
flag = [0,0]

def path_planning(gps_values):
    if round(gps_values[0],3)>x_target-0.01 and round(gps_values[0],3)<x_target+0.01 and round(gps_values[1],3)>y_target-0.01 and round(gps_values[1],3)<y_target+0.01:
            print("reached")
            return 1
        


def run_robot(robot):
    k = 90
    r = 0
    begin = 0
    p = 0
    opt = 0
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:

        
    
    
    
    
    
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
     # ds = robot.getDevice('dsname')
     # ds.enable(timestep)
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    # Main loop:
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    distant_sensor = []
    # ir0 = robot.getDevice('ps0')
    # ir0.enable(TIMESTEP)
    gps = robot.getDevice('gps')
    gps.enable(TIMESTEP)
    

    Inertial = robot.getDevice("inertial unit")
    Inertial.enable(TIMESTEP)
    # gyro = robot.getDevice('gyro')
    # gyro.enable(TIMESTEP)
    # acc = robot.getDevice('accelerometer')
    # acc.enable(TIMESTEP)
    
    for ind in ([0,1,2,5,6,7]):
        sensor_name = 'ps'+str(ind)
        distant_sensor.append(robot.getDevice(sensor_name))
        distant_sensor[-1].enable(TIMESTEP)
    # - perform simulation steps until Webots is stopping the controller
    l = Inertial.getRollPitchYaw()
    theta = math.degrees(round(l[2],3))
    
    def x_error():
        while robot.step(TIMESTEP) != -1:
            theta_0 = 0
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
            l = Inertial.getRollPitchYaw()
            theta = math.degrees(round(l[2],3))
            print(theta_0-theta,"in")
            if abs(theta_0-theta)<5:
                print(theta)
                break
            if (theta_0-theta) > 0:
                left_speed = -MAX_SPEED
            if (theta_0-theta) < 0:
                right_speed = -MAX_SPEED
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
        while robot.step(TIMESTEP) != -1:
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
            gps_values = gps.getValues()
            print(gps_values)
            if gps_values[0]<x_target+0.02 and gps_values[0]>x_target-0.02:
                left_motor.setVelocity(0)
                right_motor.setVelocity(0)
                exit()
    def y_error():
        while robot.step(TIMESTEP) != -1:
            theta_0 = 90
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
            l = Inertial.getRollPitchYaw()
            theta = math.degrees(round(l[2],3))
            print(theta_0-theta,"in")
            if abs(theta_0-theta)<5:
                print(theta)
                break
            if (theta_0-theta) > 0:
                left_speed = -MAX_SPEED
            if (theta_0-theta) < 0:
                right_speed = -MAX_SPEED
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
        while robot.step(TIMESTEP) != -1:
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
            gps_values = gps.getValues()
            print(gps_values)
            if gps_values[1]<y_target+0.02 and gps_values[1]>y_target-0.02:
                left_motor.setVelocity(0)
                right_motor.setVelocity(0)
                exit()


    def reached(gps):
        if gps[0]<x_target+0.02 and gps[0]>x_target-0.02:
            print("x_reached",gps)
            y_error()
            return 1
        if gps[1]<y_target+0.02 and gps[1]>y_target-0.02:
            print("y_reached",gps)
            x_error()
            return 1
        else: return 0
        
        
    while robot.step(TIMESTEP) != -1:
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
            l = Inertial.getRollPitchYaw()
            theta = math.degrees(round(l[2],3))
            print(theta_goal-theta,"in")
            if abs(theta_goal-theta)<5:
                print(theta)
                break
            if (theta_goal-theta) > 0:
                left_speed = -MAX_SPEED
            if (theta_goal-theta) < 0:
                right_speed = -MAX_SPEED
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
         
                
            #print(theta,"in")

    while robot.step(TIMESTEP) != -1:
        # Read the sensors:

        #print(msg)
        
        #####
        # def set_path():
            # t = 0
            # left_speed= MAX_SPEED
            # right_speed = MAX_SPEED
            # print("f")
            # l = Inertial.getRollPitchYaw()
            # theta = math.degrees(round(l[2],3))
            # if abs(theta_goal-theta)>4:
                # if (theta_goal-theta) > 0:
                    # left_speed= -MAX_SPEED
                    # right_speed = MAX_SPEED
                    # t = 0
                # if (theta_goal-theta) < 0:
                    # right_speed = -MAX_SPEED
                    # t = 0
            # if (theta_goal-theta)<4 and (theta_goal-theta)>-4:
                # t = 1
            # left_motor.setVelocity(left_speed)
            # right_motor.setVelocity(right_speed)
            # if t == 1:
                # return 1
            # return 0
       
        #####
        
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED
    # Enter here functions to read sensor data, like:
     # val = ds.getValue()
        gps_values = gps.getValues()
        msg = "GPS VALUES: "
        for each_value in gps_values:
            msg+=" "
            msg+=str(round(each_value,3))
        out = reached(gps_values)
        #print(msg)
        if out==1:
            left_motor.setVelocity(0)
            right_motor.setVelocity(0)
            exit()   
          
        flag[0] = flag[1]  
        flag[1] = 0
        print("b")
        for ps in distant_sensor:
            print("l")
            if ps.getValue() > 110:
                print("kkk")
                flag[1] = 1
                l = Inertial.getRollPitchYaw()
                angle = math.degrees(round(l[2],3))
                if opt == 0:
                    base_a = angle
                    opt = 1
                if abs(angle-base_a)>85 and abs(angle-base_a)<105:
                    p = 1
                if p==1:
                    right_speed = -MAX_SPEED
                    #print("right")
                if p==0:
                    left_speed = -MAX_SPEED
                    #print("left")

        if flag[0]==1 and flag[1]==0:
            print("Milgya")
            p = 0
            opt = 0
            left_motor.setVelocity(MAX_SPEED)
            right_motor.setVelocity(MAX_SPEED)
            k = 0
        if flag[0]==0 and flag[1]==0:
            k+=1
        if k==18:
            #print("yess")
            r = 1
        if r == 1:
            l = Inertial.getRollPitchYaw()
            theta = math.degrees(round(l[2],3))
            print(theta_goal-theta,"in")
            if abs(theta_goal-theta)<5:
                print(theta)
                r = 0
            if (theta_goal-theta) > 0:
                left_speed = -MAX_SPEED
            if (theta_goal-theta) < 0:
                right_speed = -MAX_SPEED
        
        
        
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed) 
        
            
                    



                    # left_motor.setVelocity(left_speed)
                # right_motor.setVelocity(right_speed)
                # while True:
                    # print("s")
                    # if distant_sensor[0].getValue() < 110:
                        # print("g")
                        # left_speed = 0
                        # right_speed = 0
                        # left_motor.setVelocity(left_speed)
                        # right_motor.setVelocity(right_speed)
                        # exit()
                        # break
                
        
          
   

         # l = Inertial.getRollPitchYaw()
        # theta = math.degrees(round(l[2],3))
        # theta_diff = math.atan2(math.sin(theta_goal - theta), math.cos(theta_goal - theta))
        # print("Theta_diff :",theta_diff)
        # if theta_diff > 0:
            # while(round(theta_diff,2) != 0):
                # left_motor.setVelocity(-1)
                # right_motor.setVelocity(0)
                # l = Inertial.getRollPitchYaw()
                # theta = math.degrees(round(l[2],3))
                # theta_diff = math.atan2(math.sin(theta_goal - theta), math.cos(theta_goal - theta))
        
        
    
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
         # motor.setPosition(10.0)
        pass
    
if (__name__ == "__main__" ):
    x_target = 0.4
    y_target = 0.4
    theta_goal = math.degrees(math.atan(y_target/x_target))
    print(theta_goal)
    my_robot = Robot()
    run_robot(my_robot)



