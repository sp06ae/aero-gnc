import gnc

print("Successful import! Initializing C++ PID Controller...")

# Tuned gains: kp ki kd dt
pitchCntrl = gnc.PID(20.0, 1.0, 0.05, 0.02)

currentPitch = 10.0
targetPitch = 90.0

print(f"Starting Pitch: {currentPitch} degrees")
print(f"Target Pitch: {targetPitch} degrees\n")

for i in range(20):
    motorComms = pitchCntrl.run(targetPitch, currentPitch)

    # Move pitch proportional to our 0.02s time step
    currentPitch += motorComms * 0.02

    print(f"Loop {i+1:2d} | Cmd: {motorComms:8.2f} | Current Pitch: {currentPitch:6.2f}°")

pitchCntrl.reset()
print("\nController memory wiped clean successfully.")