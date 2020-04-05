import hospital
import simulation


def main():
    h = hospital.Hospital().get()
    s = simulation.Simulation(h)
    s.run()


main()
