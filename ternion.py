import math

class Ternion:

    def __init__(self, w, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    

    def __mul__(self, other):

        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        
        return Ternion(w, x, y, z)


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

        return Ternion(w, x, y, z)


    def conjugate(self):
        return Ternion(self.w, -self.x, -self.y, -self.z)
    
    @staticmethod
    def pure_quaternion(x, y, z):
        return Ternion(0, x, y, z)





