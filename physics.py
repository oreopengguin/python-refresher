import numpy as np
import math
import matplotlib.pyplot as plt

def calculate_bouyancy(V, density_fluid):
    """
    Function that calculates the bouyancy
    @param V: the volume of the object in cubic meters
    @param density_fluid: the density of the fluid in kg/m^3
    @ret Bouyancy force in newtons
    """
    return V*density_fluid*9.81

def will_it_float(V, mass):
    """
    Function that determines whether an object will float or sink in water
    @param V: the volume of the object in cubic meters
    @param mass: the mass of the objects in kilograms
    @ret True if object will float, False if the oebject sinks
    """
    if mass/V > 1:
        return False
    else:
        return True
    
def calculate_pressure(depth):
    """
    Function that calculates the pressure at a given depth in water
    @param depth: the depth in meters
    @ret the pressure in Pascals
    """
    return depth*9.81*1000

def calculate_acceleration(F, m):
    """
    Function that calculates the acceleration of an object given the force applied and its mass
    @param F: the force applied to the object in Newtons
    @param m: the mass of the object in kilograms
    @ret the acceleration of the object in m/s^2
    """
    return F/m

def calculate_angular_acceleration(tau, I):
    """
    Function that calculates the angular acceleration of an object given the torque applied to it and its moment of inertia.
    @param tau: the torque applied to the object in Newton-meters
    @param I: the moment of inertia of the object in kg*m^2
    @ret the angular acceleration
    """
    return tau/I

def calculate_torque (F_magnitude, F_direction, r):
    """
    Function that calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied.
    @param F_magnitude: the magnitude of force applied to the object in Newtons
    @param F_direction: the direction of the force applied to the object in degrees
    @param r: the distance from the axis of rotation to the point where the force is applied in meters
    @ret the torque
    """
    return F_magnitude * np.sin(math.radians(F_direction)) * r

def calculate_moment_of_inertia(m, r):
    """
    Function that calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object
    @param m: the mass of the object in kg
    @param r: the distance from axis of rotation to center of mass of the object in meters
    @ret the moment of inertia
    """
    return m * r**2

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100):
    force_vector = -1*np.array([np.cos(F_angle), np.sin(F_angle)])
    force_vector *= F_magnitude
    force_vector /= mass
    return force_vector

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):
    torque = calculate_torque(F_magnitude, math.degrees(F_angle), thruster_distance)
    return calculate_angular_acceleration(torque, inertia)


def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    T3 = theta + np.pi + alpha
    T2 = theta - alpha
    T1 = alpha + theta
    T4 = np.pi + theta - alpha
    
    # force_vector1 = -1*np.array([np.cos(T1), np.sin(T1)]) * T[0]
    # force_vector2 = -1*np.array([np.cos(T2), np.sin(T2)]) * T[1]
    # force_vector3 = -1*np.array([np.cos(T3), np.sin(T3)]) * T[2]
    # force_vector4 = -1*np.array([np.cos(T4), np.sin(T4)]) * T[3]
    # net_force_vector = force_vector1 + force_vector2 + force_vector3 + force_vector4
    # net_force_vector /= mass
    # return net_force_vector

    accel1 = calculate_auv_acceleration(T[0], T1, mass)
    accel2 = calculate_auv_acceleration(T[1], T2, mass)
    accel3 = calculate_auv_acceleration(T[2], T3, mass)
    accel4 = calculate_auv_acceleration(T[3], T4, mass)

    return accel1+ accel2 + accel3 + accel4




def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):
    T3 = np.pi + alpha
    T2 = -alpha
    T1 = alpha
    T4 = np.pi - alpha
    distance = np.sqrt(L**2 + l**2)
    ang_accel1 = calculate_auv_angular_acceleration(T[0], T1, inertia, distance)
    ang_accel2 = calculate_auv_angular_acceleration(T[1], T2, inertia, distance)
    ang_accel3 = calculate_auv_angular_acceleration(T[2], T3, inertia, distance)
    ang_accel4 = calculate_auv_angular_acceleration(T[3], T4, inertia, distance)

    return ang_accel1 + ang_accel2 + ang_accel3 + ang_accel4

def simulate_auv2_motion(T, alpha, L, l, mass = 100, inertia = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0 = 0):
    t = [0]
    theta = [theta0]
    x = [x0]
    y = [y0]
    v = [[0,0]]
    counter = 0
    omega = [0]
    a = [[[0,0], 0]]
    while t[counter] < t_final:
        t.append(t[counter] + dt)
        accel_vector = calculate_auv2_acceleration(T, alpha, theta, mass)
        v.append(v[counter]+accel_vector*dt)
        x.append(v[counter][0] * dt + 0.5 * accel_vector[0] * dt**2)
        y.append(v[counter][1] * dt + 0.5 * accel_vector[1] * dt**2)
        ang_accel = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)
        omega.append(omega[counter]+ang_accel*dt)
        theta.append(theta[counter] + omega[counter] * dt + 0.5* ang_accel * dt**2)
        # theta.append(theta[counter] + omega[counter+1] * dt)
        a.append([accel_vector, ang_accel])
        counter++

    return [np.ndarray(t), np.ndarray(x), np.ndarray(y), np.ndarray(theta), np.ndarray(v), np.ndarray(omega), np.ndarray(a)]

def plot_auv2_motion (t, x, y, theta, v, omega, a):
    plt.plot(x, y)
    plt.plot(t, v)

        

print(calculate_auv2_acceleration([10, 1, 4, 0], 0.12, 0.5, 100))
print(calculate_auv2_angular_acceleration([10, 1, 4, 0], 0.12, 5, 4, 1))
