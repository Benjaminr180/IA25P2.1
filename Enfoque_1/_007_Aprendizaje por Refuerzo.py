import numpy as np
print(np.__version__)
import random

class QLearningAgent:
    def __init__(self, states, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.states = states
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((states, actions))
    
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.actions - 1)  # Exploración
        return np.argmax(self.q_table[state, :])  # Explotación
    
    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        td_target = reward + self.gamma * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.alpha * td_error

# Ejemplo de uso
env_states = 5
env_actions = 2
agent = QLearningAgent(env_states, env_actions)

# Simulación de actualización de valores Q
for _ in range(10):
    state = random.randint(0, env_states - 1)
    action = agent.choose_action(state)
    reward = random.randint(-10, 10)
    next_state = random.randint(0, env_states - 1)
    agent.update(state, action, reward, next_state)

print(agent.q_table)
