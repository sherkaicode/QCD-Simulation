from Classes.Particles import Particle
import numpy as np
import math
MeV = 1e6

def gen_initial(N, CoM, e_initial):
    quark_types = {
        1: (-1/3, 4.8 * MeV),   # Down
        2: (2/3, 2.3 * MeV),    # Up
        3: (-1/3, 95 * MeV),    # Strange
        4: (2/3, 1275 * MeV),   # Charm
        5: (-1/3, 4180 * MeV),  # Bottom
        6: (2/3, 173210 * MeV)  # Top
    }
    
    allowed_charges = [-2/3, -1/3, 1/3, 2/3]

    def is_valid_charge_combo(combo):
        return math.isclose(sum(combo), e_initial, abs_tol=1e-3)

    def generate_charge_combo():
        attempts = 0
        while attempts < 10000:
            charges = [np.random.choice(allowed_charges) for _ in range(N)]
            if is_valid_charge_combo(charges):
                return charges
            attempts += 1
        raise ValueError("Unable to generate valid charge combo.")

    charges = generate_charge_combo()
    particles = []
    total_mass = 0

    for charge in charges:
        possible_pids = []
        for pid, (q_charge, mass) in quark_types.items():
            if math.isclose(q_charge, charge, abs_tol=1e-3):
                possible_pids.append(pid)
            elif math.isclose(-q_charge, charge, abs_tol=1e-3):
                possible_pids.append(-pid)
                
        np.random.shuffle(possible_pids)
        for pid in possible_pids:
            test_particle = Particle(pid, 0, (0, 0, 0))
            if total_mass + test_particle.mass < CoM:
                total_mass += test_particle.mass

                p_mag = np.random.uniform(0, 1e6)
                theta = np.random.uniform(0, math.pi)
                phi = np.random.uniform(0, 2 * math.pi)
                px = p_mag * math.sin(theta) * math.cos(phi)
                py = p_mag * math.sin(theta) * math.sin(phi)
                pz = p_mag * math.cos(theta)
                energy = math.sqrt(p_mag**2 + test_particle.mass**2)

                particle = Particle(pid, energy, (px, py, pz))
                particles.append(particle)
                break
        else:
            raise ValueError("Could not assign particle under mass constraint.")

    return particles
