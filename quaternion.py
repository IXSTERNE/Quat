import math

class Quaternion:


    def __init__(self, w = 0, x = 0, y = 0, z = 0):

        self.w = w
        self.x = x
        self.y = y
        self.z = z

        self.calculate_magnitude()


    def __str__(self):
        return f"({self.w}, {self.x}, {self.y}, {self.z})"
    
    
    def print_quat(self):
        print(Quaternion(self.w, self.x, self.y ,self.z))
    

    def calculate_magnitude(self):

        magnitude = math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.w = self.w / magnitude
        self.x = self.x / magnitude
        self.y = self.y / magnitude
        self.z = self.z / magnitude
    
    
    def __mul__(self, other):

        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w

        return Quaternion(w, x, y, z)
    
    
    def local_rotation(self, angle, axis_x, axis_y, axis_z):

        magnitude = math.sqrt(axis_x ** 2 + axis_y ** 2 + axis_z ** 2)
        axis_x = axis_x / magnitude
        axis_y = axis_x / magnitude
        axis_z = axis_x / magnitude

        local_rotation_w = math.cos(angle / 2)
        local_rotation_x = axis_x * math.sin(angle / 2)
        local_rotation_y = axis_y * math.sin(angle / 2)
        local_rotation_z = axis_z * math.sin(angle / 2)

        return Quaternion(local_rotation_w, local_rotation_x, local_rotation_y, local_rotation_z)
    




q1 = Quaternion(1, 2, 2, 1)
# q2 = Quaternion(3, 2, 3, 3)

# q1.print_quat()
# q2.print_quat()

# print(q1.local_rotation(45, 2, 2, 3))
print(q1 * q1.local_rotation(180, 2, 2, 3))
# print(q1 * q2)

