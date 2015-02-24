def kinetic_energy(mass, velocity):
    ke = .5 * mass * (velocity * velocity)
    return ke

while True:
    try:
        mass = int(input("What is the objects mass? (in kg): "))
        velocity = int(input("What is the objects velocity? (in m/s): "))
        break
    except BaseException:
        print("Error")

print("The object's kinetic energy is", kinetic_energy(mass, velocity))
