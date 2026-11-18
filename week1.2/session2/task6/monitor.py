# Week 1.2, Session 2: Task 6

# Week 1.2, Session 2: Task 6

# Get user inputs
temperature = int(input("Please enter the machine's temperature in degrees Celsius: "))
pressure = int(input("Please enter the machine's pressure in PSI: "))
operation = int(input("Please enter operation status (1: operating, 0: stopped): "))

# Step 1: Evaluate temperature
if temperature > 80:
    print("The temperature is too high.")
    print("Shut down the machine.")
elif temperature >= 50:
    print("The temperature is within safe limits.")
else:
    print("The machine temperature is low. No action is needed.")

# Step 2: Evaluate pressure
if pressure > 100:
    print("High pressure detected.")
    print("Maintenance is recommended.")
elif pressure >= 70:
    print("The pressure is stable.")
else:
    print("The pressure is low. The system is operating normally.")

# Step 3: Determine machine status
if operation == 0:
    print("The machine is stopped. No immediate action is needed.")
elif operation == 1:
    if temperature > 80 or pressure > 100:
        print("The machine is running in unsafe conditions.")
        print("Shut down the machine.")
    else:
        print("The machine is running normally.")
else:
    print("Invalid operation status.")
