# AEROGNC: Simple PID Controller

## Project Structure
```text
AEROGNC/
├── CMakeLists.txt        # CMake build configuration and pybind11 fetching
├── include/
│   └── PID.h             # C++ header for PID class
├── src/
│   ├── PID.cpp           # C++ controller logic
│   └── bindings.cpp      # pybind11 wrapper
└── scripts/
    └── test1pitch.py     # Python step-response example
```
## Prerequisites (Tested)
- C++17 compiler
- CMake 3.18+
- Miniconda/Anaconda environment Python 3.x

## Building
- Build CMake
    After building there will be a gnc.pyd created in the scripts folder
- Run the python script :)
    The python script in /script is just an example. You can create your own python file to utilise the PID code. Here are some important notes for the python script:

```python
#import the gnc file
import gnc

#the constructors and methods are as follows
controller = gnc.PID(kp, ki, kd, dt) 
command = controller.run(target value, current value) #inside the physics loop

#clean memory
controller.reset()
```

- After running the testing script, the data will be outputted into a .csv file and the dataGrapher.py can be used to graph the output.
  
