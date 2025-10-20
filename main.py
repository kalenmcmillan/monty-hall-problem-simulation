import random

doors = [1, 2, 3]

def run_paradox(switch: bool) -> bool:
    prize = random.choice(doors)
    choice = random.choice(doors)
    possible_opens = [door for door in doors if door != choice and door != prize]
    opened = random.choice(possible_opens)
    if switch:
        remaining = [door for door in doors if door not in (choice, opened)]
        choice = remaining[0]

    return choice == prize

def simulate(trials: int = 100000, switch: bool = True) -> float:
    wins = sum(run_paradox(switch) for trial in range(trials))
    return wins / trials

if __name__ == '__main__':
    trials = 100000
    stay_prob = simulate(trials, switch = False)
    switch_prob = simulate(trials, switch = True)

    print(f'Trials: {trials} / Staying: {stay_prob:.5f}% / Switching: {switch_prob:.5f}%')
