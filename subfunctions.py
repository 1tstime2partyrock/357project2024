#team subfunctions document

import numpy as np

'''
starting dictionary 
with all initial data
'''

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


'''
tau dcmotor
'''


#DELETE ME LATER!!!
omega = None 
#idk what is going on with omega or where to find it so I use a placeholer

def tau_dcmotor(omega, motor):
    if type(omega) == np.ndarray:
        if omega.ndim ==1:
            None
    
    elif type(omega) == float:
        None
    
    else:
        raise Exception('omega data type is not a scalar or vector/n'
                         'data type must be scalar or numpy array')

    if type(motor) == dict:
        None

    else: 
        raise Exception('motor data type is not a dict/n'
                        'data type of motor must be dict')
    
    omega = list[omega]

    tau = []

    for dimension_speed in omega:
        if dimension_speed > motor['speed_noload']:
            tau.append(motor['torque_noload'])

        if dimension_speed < 0:
            tau.append(motor['torque_stall'])

        if 0 <= omega <= motor['speed_noload']:
            tau_value = omega * (motor['torque_stall'] - ((motor['torque_stall'] - motor['torque_noload'])/motor['speed_noload']))
            tau.append(tau_value)

tau = tau_dcmotor(omega, motor)

'''
gear ratio
'''

def get_gear_ratio(speed_reducer):


    if type(speed_reducer) == dict:
        None
    else:
        raise Exception('Data type of speed_reducer is not a dictionary/n'
                         'Data type must be a dictionary')

    if speed_reducer['type'].lower() == 'reverted':
        None
    else:
        raise Exception('Speed reducer type is not "reverted", please change to "reverted"')

    gear_ratio = ((speed_reducer['diam_pinion'])/(speed_reducer['diam_gear']))**2
    return(gear_ratio)
    

Ng = get_gear_ratio(speed_reducer)


'''
get mass
This function computes rover mass in kilograms. It accounts for the chassis, power subsystem, science payload,
and six wheel assemblies, which itself is comprised of a motor, speed reducer, and the wheel itself.
This function should validate that (a) the input is a dict. If this condition fails, call raise 
Exception(‘<message here>’) with a meaningful message to the user
'''

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
    

'''
f_rolling function
'''

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
        

    
'''
Alex functions
'''
    
    
    
    
    
    
    
    
    
    
    