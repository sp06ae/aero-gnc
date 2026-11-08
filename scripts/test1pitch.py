import gnc
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "telemetry.csv")

print("Successful import! Initializing C++ PID Controller...")

# dt and steps
dt = 0.02
steps = 20

# Tuned gains: kp ki kd dt
pitchCntrl = gnc.PID(50.0, 1.0, 0.05, dt)

currentPitch = 10.0
targetPitch = 90.0

print(f"Starting Pitch: {currentPitch} degrees")
print(f"Target Pitch: {targetPitch} degrees\n")

with open(csv_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    for i in range(steps):
        currentTime = i * dt
        motorComms = pitchCntrl.run(targetPitch, currentPitch)

        csvwriter.writerow([currentTime, currentPitch, motorComms])

        # Move pitch proportional to our time step
        currentPitch += motorComms * dt

pitchCntrl.reset()
print("\nData saved to telemetry.csv")