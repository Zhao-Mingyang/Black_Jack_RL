from rlcard import make
from rlcard.agents.dqn_agent import DQNAgent
import torch
from rlcard.agents.nfsp_agent import  NFSPAgent
from rlcard.agents.random_agent import RandomAgent

env = make("blackjack")
print("Number of actions:", env.num_actions)
print("Number of players:", env.num_players)
print("Shape of state:", env.state_shape)
print("Shape of action:", env.action_shape)

agent = DQNAgent(
    num_actions=env.num_actions,
    state_shape=env.state_shape[0],
    mlp_layers=[64,64],
)

# agent = NFSPAgent(
#     num_actions=env.num_actions,
#     state_shape=env.state_shape[0],
#     hidden_layers_sizes=[64,64],
#     q_mlp_layers=[64,64],
# )

# agent = RandomAgent(env.num_actions)

env.set_agents([agent for _ in range(env.num_players)])

from rlcard.utils import (
    tournament,
    reorganize,
    Logger,
    plot_curve,
)

best_score = -1
with Logger("experiments/leduc_holdem_dqn_result/") as logger:
    for episode in range(10000): # 1000->1000

        # Generate data from the environment

        trajectories, payoffs = env.run(is_training=True)
        # trajectories, payoffs = env.run(is_training=False)

        # Reorganaize the data to be state, action, reward, next_state, done
        trajectories = reorganize(trajectories, payoffs)

        # Feed transitions into agent memory, and train the agent
        for ts in trajectories[0]:
            agent.feed(ts)

        # Evaluate the performance.
        if episode % 50 == 0:
            score = tournament(env, 10000, )[0]
            if score > best_score:
                torch.save(agent.q_estimator.qnet.state_dict(), 'model_cifar.pt')
                print('Model Saved Score from', best_score, 'to', score)
                best_score = score
            logger.log_performance(
               str( episode)+" " + str(env.timestep),
            score
            )

    # Get the paths
    csv_path, fig_path = logger.csv_path, logger.fig_path

