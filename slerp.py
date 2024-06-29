import math

def slerp(q1, q2, t):
    
    theta = math.acos(q1[0] * q2[0] + q1[1] * q2[1] + q1[2] * q2[2] + q1[3] * q2[3])

    s0 = math.sin((1 - t) * theta) / math.sin(theta)
    s1 = math.sin(t * theta) / math.sin(theta)

    quat1 = [s0 * q1[0], s0 * q1[1], s0 * q1[2], s0 * q1[3]]
    quat2 = [s1 * q2[0], s1 * q2[1], s1 * q2[2], s1 * q2[3]]

    q = [quat1[0] + quat2[0], quat1[1] + quat2[1], quat1[2] + quat2[2], quat1[3] + quat2[3]]

    return q


