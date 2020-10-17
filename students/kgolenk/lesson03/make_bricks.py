# ---------------------------------------------------------------------------- #
# Title: Lesson 03
# Description: Booleans
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/13/2020, Created script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables

# Functions ------------------------------------------------------------------ #
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
  """
        check if we have enough small and big bricks to build the goal

        :param small: the brick with length 1 inch
        :param big: the brick with length 5 inches
        :param goal: a row of bricks that we want to build from given bricks

        function should return True if we enough small and big bricks to build a row, and False if not
  """

  if goal > (big*5 + small):
    return False
  elif goal % 5 == 0:
    return True
  elif goal % 5 <= small:
    return True
  else:
    return False

if __name__ == "__main__":

    # run some tests
    assert make_bricks(1, 2, 15) == False
    assert make_bricks(1, 6, 15) == True
    assert make_bricks(1, 3, 15) == True
    assert make_bricks(0, 3, 15) == True
    assert make_bricks(1, 1, 10) == False
    assert make_bricks(100, 10, 101) == True
    assert make_bricks(100, 5, 150) == False

    print("Pests passed")