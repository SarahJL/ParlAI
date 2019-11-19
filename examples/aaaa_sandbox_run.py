from parlai.core.params import ParlaiParser
from parlai.core.agents import Agent, create_agent, get_agent_module
from parlai.core.worlds import create_task
from parlai.utils.logging import logger
import time

parser = ParlaiParser()
parser.add_argument('-m', '--model', default='parlai.agents.aaaa_sandbox.aaaa_sandbox:HomeWorldAgent', type=str)
opt = parser.parse_args()

agents = []
agents.append(get_agent_module(opt['model'])(opt))

world_train = create_task(opt, agents)

for i in range(10):

    world_train.parley()

print('done')