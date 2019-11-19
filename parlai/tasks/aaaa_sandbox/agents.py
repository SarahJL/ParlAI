from parlai.core.agents import Teacher, Agent

class HomeWorldTeacher(Teacher):
    """
    This class implements the simple Home World example of Narasimhan 2015
    """
    def __init__(self, opt, shared=None):
        super().__init__(opt, shared)
        self.observation = None

    # store observation for later, return it unmodified
    def observe(self, observation):
        self.observation = observation
        return observation

    # return state/action dict based upon passed state
    def act(self):
        """Act upon the previous observation."""
        if self.observation is not None and 'text' in self.observation:
            t = {'text': 'Hello agent!'}
        else:
            t = {'text': 'Hello agent, you havent said anything to me yet!'}
        return t




class DefaultTeacher(HomeWorldTeacher):
    pass