import math
import numpy as np

class Quaternion:

    def __init__(self, w, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        self.w = w


    def __repr__(self):

        w_rounded = f"{round(self.w, 5):.5f}"
        x_rounded = f"{round(self.x, 5):.5f}"
        y_rounded = f"{round(self.y, 5):.5f}"
        z_rounded = f"{round(self.z, 5):.5f}"
        return f"{w_rounded}, {x_rounded}i, {y_rounded}j, {z_rounded}k"
    

    def __mul__(self, other):

        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        
        return Quaternion(w, x, y, z)


    @staticmethod
    def compute_rotation(theta, x, y, z):

        vector_magnitude = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        normalized_x = x / vector_magnitude
        normalized_y = y / vector_magnitude
        normalized_z = z / vector_magnitude

        angle_rad = math.radians(theta)

        w = math.cos(angle_rad / 2)
        x = normalized_x * math.sin(angle_rad / 2)
        y = normalized_y * math.sin(angle_rad / 2)
        z = normalized_z * math.sin(angle_rad / 2)

        return Quaternion(w, x, y, z)


    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)
    
    @staticmethod
    def pure_quaternion(x, y, z):
        return Quaternion(0, x, y, z)





