G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)  # Mass of Earth
m = 7.34 * (10 ** 22)  # Mass of the moon
r = 3.84 * (10 ** 8)

Fg = G*M*m/(r ** 2)
print(Fg)
print(round(Fg))
print("Gravitational force value: " + format(Fg,".2f"))