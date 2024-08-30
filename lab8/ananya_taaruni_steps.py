
def feet_to_steps(feet_walked):
    steps_walked = feet_walked/2.5
    return int(steps_walked)

feet_walked = float(input('Please enter the distance walked in feet: '))

print(f'{feet_to_steps(feet_walked)} steps')