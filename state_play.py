import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
  def feed(self, puppy):
    return 'The puppy is too busy playing with the ball to eat right now.'

  def play(self, puppy):
    puppy.inc_play()
    if puppy._plays == 3:
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return 'You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much that it fell asleep.'
    return 'You throw the ball again and the puppy excitedly chases it.'