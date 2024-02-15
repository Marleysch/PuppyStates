import puppy
import check_input

def main():
  puppy_obj = puppy.Puppy()

  print('Congratulations on your new puppy!')
  done = False
  while not done:
    user_choice = check_input.get_int_range('What would you like to do:\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ', 1, 3)
    if user_choice == 1:
      print(puppy_obj.give_food())
      print()

    elif user_choice == 2:
      print(puppy_obj.throw_ball())
      print()

    else:
      done = True


main()