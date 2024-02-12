import numpy as np

motor = {'torque_stall' : 170, 'torque_noload' : 0,
         'speed_noload' : 3.80, 'mass' : 5}

omega = None 
#idk what is going on with omega or where to find it 

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
tau dcmotor function
'''

speed_reducer = {'type' : 'reverted', 'diam_pinion' : 0.04,
                'diam_gear' : 0.07, 'mass' : 1.5}

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
gear ratio function
'''