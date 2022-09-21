from env import BlackjackEnv

bj_env = BlackjackEnv()
bj_env.reset(seed = 33)
print(bj_env.step(1))