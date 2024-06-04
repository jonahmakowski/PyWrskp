from scipy.integrate import odeint
import numpy as np
m1 = 3
m2 = 1
L1 = 1.4
L2 = 1
g = 9.8
key = input("enter your key: ")
texttoencrypt = input("enter your text: ")
keydigit = 1
keynumbers1 = [ord(l) - 96 for l in key.lower()]
encryptnumbers1 = [ord(l) - 96 for l in texttoencrypt.lower()]
keycount = 0
for i in range(len(keynumbers1)):
    keycount += int(keynumbers1[i])
while keycount > 334:
    keycount -= 164
velocitytobeused = keynumbers1[int(len(keynumbers1)) - 1]


def double_pendulum(u, t, m1, m2, L1, L2, g):
    du = np.zeros(4)

    c = np.cos(u[0] - u[2])
    s = np.sin(u[0] - u[2])

    du[0] = u[1]
    du[1] = (m2 * g * np.sin(u[2]) * c - m2 * s * (L1 * c * u[1] ** 2 + L2 * u[3] ** 2) - (m1 + m2) * g * np.sin(
        u[0])) / (L1 * (m1 + m2 * s ** 2))
    du[2] = u[3]
    du[3] = ((m1 + m2) * (L1 * u[1] ** 2 * s - g * np.sin(u[2]) + g * np.sin(u[0]) * c) + m2 * L2 * u[
        3] ** 2 * s * c) / (L2 * (m1 + m2 * s ** 2))

    return du


def run(thing1, thing2, thing3, thing4):
    u0 = [thing1, thing2, thing3, thing4]

    tfinal = 30.0
    Nt = 751
    t = np.linspace(0, tfinal, Nt)

    sol = odeint(double_pendulum, u0, t, args=(m1, m2, L1, L2, g))

    u0 = sol[:, 0]
    u1 = sol[:, 1]
    u2 = sol[:, 2]
    u3 = sol[:, 3]
    print(str(np.array(u0).tolist()[keydigit]) + ", " + str(np.array(u2).tolist()[keydigit]) + "\n")


for i in range(len(encryptnumbers1)):
    run(int(encryptnumbers1[i]) + keycount, velocitytobeused / 10, int(keycount + 26 - encryptnumbers1[i]), velocitytobeused / 10)
