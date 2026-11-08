import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

time = []
pitch = []
cmd = []

try:
    with open('telemetry.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            time.append(float(row[0]))
            pitch.append(float(row[1]))
            cmd.append(float(row[2]))

except FileNotFoundError:
    print("File not found")

# 2. Plot the Dashboard
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

# Top Graph: Pitch Angle vs. Target
ax1.plot(time, pitch, label="Current Pitch (°)", color="royalblue", linewidth=2.5)
ax1.set_ylabel("Pitch Angle (deg)", fontsize=11)
ax1.set_title("GNC PID Controller Step Response", fontsize=13, fontweight="bold")
ax1.set_ylim(0, 105)
ax1.yaxis.set_major_locator(MultipleLocator(15))
ax1.legend(loc="lower right", frameon=True)
ax1.grid(True, linestyle="--", alpha=0.4)

# Bottom Graph: Motor Command Output
ax2.plot(time, cmd, label="Motor Command", color="darkorange", linewidth=2.5)
ax2.axhline(0.0, color="gray", linestyle=":", linewidth=1)
ax2.set_xlabel("Time (seconds)", fontsize=11)
ax2.set_ylabel("Control Effort", fontsize=11)
ax2.xaxis.set_major_locator(MultipleLocator(0.1))
ax2.legend(loc="upper right", frameon=True)
ax2.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()



