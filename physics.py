import numpy as np

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
    return F_magnitude * np.sin(F_direction*np.pi/180) * r

def calculate_moment_of_inertia(m, r):
    """
    Function that calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object
    @param m: the mass of the object in kg
    @param r: the distance from axis of rotation to center of mass of the object in meters
    @ret the moment of inertia
    """
    return m * r**2

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    force_vector = -1*np.array([np.cos(F_angle), np.sin(F_angle)])
    force_vector *= F_magnitude/mass
    return force_vector

def calculate_auv_angular_acceleration(F_magnitude, f_angle, inertia = 1, thruster_distance = 0.5):
    