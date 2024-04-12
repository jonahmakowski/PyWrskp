from time import time, sleep


def ticks_ms():
    return time() * 1000


def acceleration(accel, target, current, last_time):
    now = ticks_ms()
    accel_ms = accel * 0.001
    difference = now - last_time
    accel_add = accel_ms * difference
    new = current + accel_add
    accel_done = False
    if new >= target:
        new = target
        accel_done = True

    return int(new), now, accel_done


def decceleration(accel, target, current, last_time):
    now = ticks_ms()
    accel_ms = accel * 0.001
    difference = now - last_time
    accel_add = accel_ms * difference
    new = current - accel_add
    accel_done = False
    if new <= target:
        new = target
        accel_done = True

    return int(new), now, accel_done


if __name__ == '__main__':
    t = 500
    a = 100
    c = 0
    l = ticks_ms()
    done = False

    while not done:
        sleep(0.5)
        c, l, done = acceleration(a, t, c, l)
        print(c)

    t = 0
    a = 200
    c = 500
    l = ticks_ms()
    done = False
    while not done:
        sleep(0.5)
        c, l, done = decceleration(a, t, c, l)
        print(c)
