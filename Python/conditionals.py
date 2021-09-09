# SRC: https://exercism.org/tracks/python/exercises/meltdown-mitigation

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
 
    Efficiency can be grouped into 4 bands:
 
    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient
 
    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage = (generated_power / theoretical_max_power) * 100
    if percentage >= 80:
        return 'green'
    if percentage >= 60:
        return 'orange'
    if percentage >= 30:
        return 'red'
    return 'black'
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return safety range.
 
    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """
    criticality = temperature * neutrons_produced_per_second
    if criticality < threshold * 0.4:
        return 'LOW'
    if threshold * 0.9 <= criticality <= threshold * 1.1:
        return 'NORMAL'
    return 'DANGER'
