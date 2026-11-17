#!/usr/bin/env python3

import sys
import math

def calculate_velocity(x0, y0, z0, x1, y1, z1):
    vx = x1 - x0
    vy = y1 - y0
    vz = z1 - z0
    return vx, vy, vz

def calculate_position(x, y, z, vx, vy, vz, n):
    new_x = x + n * vx
    new_y = y + n * vy
    new_z = z + n * vz
    return new_x, new_y, new_z

def calculate_incidence_angle(vx, vy, vz):
    angle_radians = math.atan(abs(vz) / math.sqrt(vx**2 + vy**2))
    return math.degrees(angle_radians)

def main():
    if sys.argv[1] == "-h" and len(sys.argv) == 2:
        print("""USAGE
    ./101pong x0 y0 z0 x1 y1 z1 n

DESCRIPTION
    x0  ball abscissa at time t - 1
    y0  ball ordinate at time t - 1
    z0  ball altitude at time t - 1
    x1  ball abscissa at time t
    y1  ball ordinate at time t
    z1  ball altitude at time t
    n   time shift (greater than or equal to zero, integer)""")
        sys.exit(0)
    elif len(sys.argv) != 8:
        print("Usage: ./101pong x0 y0 z0 x1 y1 z1 n")
        sys.exit(84)

    try:
        x0, y0, z0 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
        x1, y1, z1 = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
        n = int(sys.argv[7])
    except ValueError:
        print("Error: arguments must be numbers")
        sys.exit(84)

    vx, vy, vz = calculate_velocity(x0, y0, z0, x1, y1, z1)
    print(f"The velocity vector of the ball is:\n({vx:.2f}, {vy:.2f}, {vz:.2f})")

    new_x, new_y, new_z = calculate_position(x1, y1, z1, vx, vy, vz, n)
    print(f"At time t + {n}, ball coordinates will be:\n({new_x:.2f}, {new_y:.2f}, {new_z:.2f})")

    if (z1 > 0 and new_z <= 0) or (z1 < 0 and new_z >= 0):
        angle = calculate_incidence_angle(vx, vy, vz)
        print(f"The incidence angle is:\n{angle:.2f} degrees")
    else:
        print("The ball won't reach the paddle.")

if __name__ == "__main__":
    main()
