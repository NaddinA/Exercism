# did u just click a file called lasagna.py? Lmao       anyway... enjoy lasagna

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Returns remaining bake time

    This function takes one argument representing the number elapsed baking time
    and subtracts it from the total expected baking time of a lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Returns the number of minutes it would take to prepare a layer of lasagna
    assuming that each layer takes two minutes to prepare.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Returns the total number of elapsed time in minutes to cook a full lasagna

    This function adds the elapsed baking time to the number of minutes it takes to cook and add
    'n' number of layers to the lasagna being prepared.
    """
    return elapsed_bake_time + (number_of_layers * 2)
