from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class WhiskyEnv(MiniGridEnv):
    """
    Whisky shift environment.
    """

    def __init__(
        self,
        width=9,
        height=7,
        agent_start_pos=(1,1),
        agent_start_dir=0,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
        self.goal_pos = (width-2, 1)

        super().__init__(
            width=width,
            height=height,
            max_steps=4*width*height,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
        self.put_obj(Goal(), *self.goal_pos)

        # Place the whiskey block
        self.place_obj(Whisky())
        # self.grid.set(3, 1, Whisky())

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

register(
    id='MiniGrid-Whisky-v0',
    entry_point='gym_minigrid.envs:WhiskyEnv'
)
