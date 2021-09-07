# Eyerape for you Python-lovers right here:

def eat_ghost(power_pellet_active, touching_ghost):
    """
    If power pellet is active and ghost is touched, you eat it!
    """
    if power_pellet_active and touching_ghost:
        return True
    return False
  
def score(touching_power_pellet, touching_dot):
    """
    Add up to score when you touch a power pellet or a dot!
    """
    if touching_power_pellet or touching_dot:
        return True
    return False
  
def lose(power_pellet_active, touching_ghost):
    """
    If no power pellet is active and you touch a ghost, GG.
    """
    if power_pellet_active is False and touching_ghost:
        return True
    return False
  
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    When touching a ghost, if you have eaten all the dots and power pellet is active, or if
    you eat all the dots safely, you win!
 
    Otherwise, it's a loss.
    """
    if touching_ghost:
        if has_eaten_all_dots:
            if power_pellet_active:
                return True
            return False
    elif has_eaten_all_dots:
        return True
