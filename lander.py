# const

F = 1.5  # 逆噴射の加速度を決定する係数
G = 9.80665

# retrofire()関数


def retrofire(t, tf):
    if t >= tf:
        return - F * G
    else:
        return 0.0


t = 0.0
h = 0.01

v = float(input("input v0"))
x0 = float(input("initial x0"))
tf = float(input("逆噴射開始時刻tfを入力してください"))

x = x0

print("{:.7f} {:.7f} {:.7f}".format(t, x, v))

while (x >= 0) and (x <= x0):
    t += h
    v += (G + retrofire(t, tf)) * h
    x -= v * h

    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))
