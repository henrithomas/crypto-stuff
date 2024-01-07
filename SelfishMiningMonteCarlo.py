# -*- coding: utf-8 -*-
"""
Henri Thomas
Bitcoin and Cryptocurrency Technologies
Selfish Mining Monte Carlo Simulation
"""
import random
gamma = 0.0
state = 0
honest_reward = 0
selfish_reward = 0
iterations = 20000
roll = 0.0

for alpha in [0.1,0.2,0.3,0.4]:
    print('alpha =',alpha)
    for gamma in [0.0,0.5,1.0]:
        for k in range(iterations):
            roll = random.random()
            if state == 0:
                if roll <= alpha:
                    state = 2
                else:
                    honest_reward += 1
            elif state == 1:
                state = 0
                if roll <= alpha:
                    selfish_reward += 2
                elif roll > alpha and roll <= (alpha + gamma * (1 - alpha)):
                    selfish_reward += 1 
                    honest_reward += 1
                else:
                    honest_reward += 2
            elif state == 2:
                if roll <= alpha:
                    state = 3 
                    selfish_reward += 2
                else:
                    state = 1
            elif state == 3:
                if roll <= alpha:
                    selfish_reward += 1
                    state = 4
                else:
                    state = 0 
            else:
                if roll <= alpha:
                    state += 1
                    selfish_reward += 1
                else:
                    state -= 1
        print('\n\tgamma =',gamma,'\tselfish miner relative revenue =',selfish_reward / (selfish_reward + honest_reward))
        print('\t\t\thonest miner relative revenue =',honest_reward / (selfish_reward + honest_reward))
        print('\t\t\tselfish miner revenue =',selfish_reward,'\thonest miner revenue =',honest_reward)
        honest_reward = 0
        selfish_reward = 0
        state = 0
    
