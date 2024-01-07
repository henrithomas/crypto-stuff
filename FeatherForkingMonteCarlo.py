# -*- coding: utf-8 -*-
"""
Henri Thomas
Bitcoin and Cryptocurrency Technologies
Feather Forking Monte Carlo Simulation
"""
import random
attacker_wins = 0
attacker_aborts = 0
iterations = 20000
state = 2
done = False
state_transitions = 0
expected_fork_time = 0.0
roll = 0.0
for alpha in [0.0,0.1,0.2,0.3,0.4,0.5,1.0]:
    state_transitions = 0
    attacker_wins = 0
    attacker_aborts = 0
    for i in range(iterations):
        done = False
        state = 2
        while not(done):
            roll = random.random()     
            if state == 0:
                attacker_aborts += 1
                done = True
            elif state == 1:
                state_transitions += 1
                if roll < alpha:
                    state = 2
                else:
                    state = 0
            elif state == 2:
                state_transitions += 1
                if roll < alpha:
                    state = 3
                else:
                    state = 1
            elif state == 3:
                state_transitions += 1  
                if roll < alpha:
                    state = 4
                else:
                    state = 2
            elif state == 4:
                attacker_wins += 1
                done = True
            
    print('alpha =',alpha)
    print('\tAttacker wins =',attacker_wins)
    print('\tP1 =',attacker_wins / iterations)
    print('\tAverage state transitions =', state_transitions / iterations)