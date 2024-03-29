import puppy_state
import state_eat
import state_play

class StateAsleep(puppy_state.PuppyState):
  def feed(self, puppy):
    puppy.change_state(state_eat.StateEat())
    puppy.inc_food()
    return 'The puppy wakes up and comes running to eat.'

  def play(self, puppy):
    return 'The puppy is asleep. It doesn\'t want to play right now.'