from parlai.core.agents import Agent


class HomeWorldAgent(Agent):
    """
    This class implements an agent to operate in the simple Home World example of Narasimhan 2015
    """
    def __init__(self, opt, shared=None):
        super().__init__(opt, shared)
        self.observation = None

    def act(self):
        """Return an observation/action dict based upon given observation."""
        if hasattr(self, 'observation') and self.observation is not None:
            print('agent received observation:')
            print(self.observation)

        t = {}
        t['text'] = 'hello, teacher I am saying something new now!'
        print('agent sending message:')
        print(t)
        return t