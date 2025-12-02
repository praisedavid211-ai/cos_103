print("PHYSICS FORMULA CALCULATOR")
print("Choose a formula:")
print("1. Speed = Distance / Time")
print("2. Force = Mass * Acceleration")
print("3. Pressure = Force / Area")
print("4. Ohm's Law: Voltage = Current * Resistance")
print("5. Kinetic Energy = 1/2 * Mass * Velocity^2")

choice = input("Enter the number of the formula you want to use (1-5): ")

if choice == "1":
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    speed = distance / time
    print("Speed =", speed, "m/s")

elif choice == "2":
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    force = mass * acceleration
    print("Force =", force, "N")

elif choice == "3":
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m^2): "))
    pressure = force / area
    print("Pressure =", pressure, "Pa")

elif choice == "4":
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ω): "))
    voltage = current * resistance
    print("Voltage =", voltage, "V")

elif choice == "5":
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * (velocity ** 2)
    print("Kinetic Energy =", ke, "J")

else:
    print("Invalid choice! Please run the program again.")