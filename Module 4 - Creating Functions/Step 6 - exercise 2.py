def target(age, resting, intensity):
    return (220 - age - resting) * intensity + resting

age = 35
rest_heart = 65
intensity = .7
print(target(age,rest_heart,intensity))