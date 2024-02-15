import state_asleep

'''
Attributes:
  _state (StateAsleep): The current state of the puppy.
  _eats (int): The number of times the puppy has eaten. 
  _plays (int): The number of times the puppy has played.
'''

class Puppy:
  def __init__(self):
    self._state = state_asleep.StateAsleep()
    self._plays = 0
    self._eats = 0

  def change_state(self, new_state):
    self._state = new_state

  def throw_ball(self):
    return self._state.play(self)

  def give_food(self):
    return self._state.feed(self)

  def inc_food(self):
    self._eats += 1

  def inc_play(self):
    self._plays += 1

  def reset(self):
    self._plays = 0
    self._eats = 0