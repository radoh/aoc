from collections import Counter, defaultdict

numbers = [20, 9, 11, 0, 1, 2]
last_spoken_on = defaultdict(list)
last_spoken_on.update({v: [i + 1] for i, v in enumerate(numbers)})
cnt = Counter(numbers)

i = len(numbers) + 1
while i < 30000001:
    if cnt[numbers[-1]] == 1:
        numbers.append(0)
    else:
        numbers.append(last_spoken_on[numbers[-1]][-1] - last_spoken_on[numbers[-1]][-2])
    cnt.update({numbers[-1]: 1})
    last_spoken_on[numbers[-1]].append(i)
    if i == 2020:
        print(numbers[-1])
    if i % 1000000 == 0:
        print(i // 1000000, '...need to be patient...')
    i += 1

print(numbers[-1])