# 101pong

A 3D ball trajectory solver for a simplified version of Pong, written in Python. Given two successive ball positions, it computes the velocity vector, the position after a time shift, and the incidence angle if the ball reaches the paddle plane.

## Usage

```bash
./101pong.py x0 y0 z0 x1 y1 z1 n
./101pong.py -h
```

| Argument | Description |
|---|---|
| `x0 y0 z0` | Ball coordinates at time `t - 1` |
| `x1 y1 z1` | Ball coordinates at time `t` |
| `n` | Time shift (integer >= 0) |

Exits with `84` on invalid arguments.

## Examples

```bash
$ ./101pong.py 1 3 5 7 9 -2 4
The velocity vector of the ball is:
(6.00, 6.00, -7.00)
At time t + 4, ball coordinates will be:
(31.00, 33.00, -30.00)
The ball won't reach the paddle.
```

```bash
$ ./101pong.py 1.1 3 5 -7 9 2 4
The velocity vector of the ball is:
(-8.10, 6.00, -3.00)
At time t + 4, ball coordinates will be:
(-39.40, 33.00, -10.00)
The incidence angle is:
16.57 degrees
```

## Requirements

Python 3, standard library only.
