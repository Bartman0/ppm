from PPMSimulator import PPMSimulator
from PPM import PPM

sim = PPMSimulator(conf_limit=0.2)
ppm = PPM(conf_limit=0.3)

while True:
    #print(sim.read_cars())
    print(ppm.read_cars())
