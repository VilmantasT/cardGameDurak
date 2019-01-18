import random
GOAL = list(input('Enter your text: '))
goal_len = len(GOAL)

def generator(tempstring=[]):
    letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
    letters.append(' ')
    if len(tempstring) == 0:
        for i in range(goal_len):
            tempstring.append(random.choice(letters))
    else:
        for i in range(len(tempstring)):
            if tempstring[i] != GOAL[i]:
                tempstring[i] = random.choice(letters)
            else:
                continue
    return tempstring

def score(gstring):
    points = 0
    for i in list(range(goal_len)):
        if GOAL[i] == gstring[i]:
            points +=1
        else:
            continue
    return points * 100 / goal_len

def check():
    count = 0
    b_score = 0
    b_string = []
    t_string = generator()
    t_score = score(t_string)

    while b_score != 100.0:
        count += 1
        thousands = 0
        if count == 1000:
            print('Biggest score so far is: {}'.format(b_score))
            print('Best string generated {}'.format(b_string))
            count = 0
            thousands += 1
        elif b_score < t_score:
            b_score = t_score
            b_string = t_string
            t_string = generator(b_string)
            t_score = score(t_string)
        else:
            t_string = generator(b_string)
            t_score = score(t_string)

    return 'The word \'{}\' generated at {} % accuracy per {} runs.'.format(''.join(b_string), b_score, thousands * 1000 + count)
print(check())
