# import math


# def slerp(sample_q1, sample_q2, t):

#     for q1, q2 in zip(sample_q1, sample_q2):

#         print(q1, q2)

#         theta = math.acos(q1[0] * q2[0] + q1[1] * q2[1] + q1[2] * q2[2] + q1[3] * q2[3])

#         s0 = math.sin((1 - t) * theta) / math.sin(theta)
#         s1 = math.sin(t * theta) / math.sin(theta)

#         quat1 = [s0 * q1[0], s0 * q1[1], s0 * q1[2], s0 * q1[3]]
#         quat2 = [s1 * q2[0], s1 * q2[1], s1 * q2[2], s1 * q2[3]]

#         q = [quat1[0] + quat2[0], quat1[1] + quat2[1], quat1[2] + quat2[2], quat1[3] + quat2[3]]

#     return q

import math

def slerp(sample_q1, sample_q2, t):
    result = []

    for q1, q2 in zip(sample_q1, sample_q2):
        # Compute the dot product
        dot = q1[0] * q2[0] + q1[1] * q2[1] + q1[2] * q2[2] + q1[3] * q2[3]
        
        # Clamp dot product to be in the range [-1, 1]
        dot = max(min(dot, 1.0), -1.0)
        
        if dot < 0.0:
            q2 = [-q2[0], -q2[1], -q2[2], -q2[3]]
            dot = -dot
        
        if dot > 0.9995:
            result = [(1 - t) * q1[i] + t * q2[i] for i in range(4)]
            result_length = math.sqrt(sum(x*x for x in result))
            result = [x / result_length for x in result]
            result = [result]
        else:
            theta_0 = math.acos(dot)
            theta = theta_0 * t
            sin_theta = math.sin(theta)
            sin_theta_0 = math.sin(theta_0)

            s0 = math.cos(theta) - dot * sin_theta / sin_theta_0
            s1 = sin_theta / sin_theta_0

            result = [[s0 * q1[i] + s1 * q2[i] for i in range(4)]]
            
    return result
