

import numpy as np

############ get_mass #############

wheel = {'radius' : 0.3, 'mass' : 1}
speed_reducer = {'type' : 'reverted', 'diam_pinion' : 0.04,
                 'diam_gear' : 0.07, 'mass' : 1.5}
motor = {'torque_stall' : 170, 'torque_noload' : 0,
         'speed_noload' : 3.80, 'mass' : 5}

wheel_assembly = {'wheel' : wheel, 'speed_reducer' : speed_reducer,
                  'motor' : motor}

chassis = {'mass' : 659}

science_payload = {'mass' : 75}

power_subsys = {'mass' : 90}

rover = {'wheel_assembly' : wheel_assembly, 'chassis' : chassis,
         'science_payload' : science_payload, 'power_subsys' : power_subsys}

planet = {'g' : 3.72}

#This function computes rover mass in kilograms. It accounts for the chassis, power subsystem, science payload,
# and six wheel assemblies, which itself is comprised of a motor, speed reducer, and the wheel itself.
#This function should validate that (a) the input is a dict. If this condition fails, call raise 
#Exception(‘<message here>’) with a meaningful message to the user
def get_mass(rover):
    
    if not isinstance(rover, dict):
        raise Exception('rover is not a dictionary')
    
    m = 0
    
    m += rover['chassis']['mass']
    
    m += rover['power_subsys']['mass']
    
    m += rover['science_payload']['mass']
    
    ## 6 wheels. 6 speed reducers, 6 motors
    m += (rover['wheel_assembly']['wheel']['mass'] + rover['wheel_assembly']['speed_reducer']['mass'] + rover['wheel_assembly']['motor']['mass']) * 6
    
    return m   # should be 869
    

def F_rolling(omega, terrain_angle, rover, planet, Crr):
    
    if not isinstance(omega, np.array()):
        raise Exception('omega is not a numpy array')
        
    if not isinstance(terrain_angle, np.array()):
        raise Exception('terrain_angle is not a numpy array')
        
    if not isinstance(rover, dict):
        raise Exception('rover is not a dictionary')
        
    if not isinstance(planet, dict):
        raise Exception('planet is not a dictionary')
        
    if not isinstance(Crr, (float, int)):
        raise Exception('Crr is not an scalar')
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    