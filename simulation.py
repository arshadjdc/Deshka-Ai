import random

class Agent:
    def __init__(self, id):
        self.id = id
        self.state = random.uniform(0, 1)

    def update(self):
        change = random.uniform(-0.05, 0.05)
        self.state += change
        self.state = max(0, min(1, self.state))


def calculate_instability(agents):
    values = [a.state for a in agents]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance


def racs_correction(agents):
    for a in agents:
        a.state += (0.5 - a.state) * 0.1


def simulate(num_agents=1000, steps=50):
    agents = [Agent(i) for i in range(num_agents)]

    for step in range(steps):
        for a in agents:
            a.update()

        instability = calculate_instability(agents)
        print(f"Step {step} | Instability: {instability:.4f}")

        if instability > 0.02:
            racs_correction(agents)


# Run simulation
simulate()