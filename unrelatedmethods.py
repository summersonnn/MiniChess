import torch
import dqn

def extract_tensors(experiences):
	# Convert batch of Experiences to Experience of batches
	batch = dqn.Experience(*zip(*experiences))

	state_batch = torch.cat(batch.state, 0)
	action_batch = torch.cat(batch.action)
	nextState_batch = torch.cat(batch.next_state, 0)
	reward_batch = torch.cat(batch.reward)

	return (state_batch, action_batch, reward_batch, nextState_batch)



