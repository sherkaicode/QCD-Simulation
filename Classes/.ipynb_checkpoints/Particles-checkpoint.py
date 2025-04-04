import random
import math
import numpy as np
MeV = 1e6
class Particle:
    def __init__(self, pid, energy, momentum):
        dict_anti = ["", "", "Anti "]
        self.pid = pid              # Particle ID (e.g., 1 for quark, -1 for antiquark, etc.)
        self.energy = energy        # Energy of the particle
        self.momentum = momentum    # Momentum as a vector (px, py, pz)
        if np.abs(self.pid) == 1:
            self.charge = -1/3*np.sign(self.pid)
            self.name = f"Down {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 4.8*MeV
        elif np.abs(self.pid) == 2:
            self.charge = 2/3*np.sign(self.pid)
            self.name = f"Up {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 2.3*MeV
        elif np.abs(self.pid) == 3:
            self.charge = -1/3*np.sign(self.pid)
            self.name = f"Strange {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 95*MeV
        elif np.abs(self.pid) == 4:
            self.charge = 2/3*np.sign(self.pid)
            self.name = f"Charm {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 1275*MeV
        elif np.abs(self.pid) == 5:
            self.charge = -1/3*np.sign(self.pid)
            self.name = f"Bottom {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 4180*MeV
        elif np.abs(self.pid) == 6:
            self.charge = 2/3*np.sign(self.pid)
            self.name = f"Top {dict_anti[np.sign(self.pid)]}Quark"
            self.mass = 173210*MeV

    def __str__(self):
        return f"Particle(pid={self.pid}, name = {self.name}, energy={self.energy}, momentum={self.momentum}, mass = {self.mass}, charge = {self.charge}"

    def transverse_momentum(self):
        px, py, pz = self.momentum
        return math.sqrt(px**2 + py**2)
