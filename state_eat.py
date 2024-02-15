import puppy_state
import state_asleep
import state_play

class StateEat(puppy_state.PuppyState):
  def feed(self, puppy):
    puppy.inc_food()
    if puppy._eats == 3:
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return 'The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much that it fell asleep.'
    return 'The puppy continues to eat as you add another scoop of kibble to its bowl.'

  def play(self, puppy):
    puppy.change_state(state_play.StatePlay())
    puppy.inc_play()
    return 'The puppy looks up from its food and chases the ball you threw.'