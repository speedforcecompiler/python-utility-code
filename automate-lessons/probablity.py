import random

samples = []
streaks = []
streak = 1
current_compare = 0
streak_counter = 1
summarized_result = []
possible_outcomes = ['T','H']

for cycle in range(10000):
    outcome = possible_outcomes[random.randint(0,1)]
    samples.append(outcome)

for key,sample in enumerate(samples):
    if key !=0:
        if samples[key-1] == samples[key]:
            streak += 1
            if key == len(samples)-1:
                streaks.append(streak)
                streak = 1
        else:
            streaks.append(streak)
            streak = 1
            if key == len(samples)-1:
                streaks.append(streak)
                streak = 1

# print(samples)
# print(streaks)

streaks.sort()
# print(streaks)

for key,item in enumerate(streaks):
    if key!=0:
        if streaks[key-1] == streaks[key]:
            streak_counter += 1
        else:
            result = []
            result.append(streaks[key-1])
            result.append(streak_counter)
            summarized_result.append(result)
            streak_counter = 1
        if key == len(streaks) - 1:
            result = []
            result.append(streaks[key])
            result.append(streak_counter)
            summarized_result.append(result)
            streak_counter = 1


print(summarized_result)
print("Streak\t\tPrecentage")
for key,value in enumerate(summarized_result):
    print(str(value[0])+"\t\t"+str(round((value[1]/10000)*100,2)))
    