import random

# The host knew the coin's position beforehand.
# You choose one card, then the host will pick up another card which
# has no coin, and ask you whether to choose another card
def gen_problem():
    p = [0] * 3
    p[random.randint(0, 2)] = 1  #[0, 2]
    # suppose you choose card[0]
    # now if the card[1] has coin, host will pick up card[2] and
    # tell that you can change your mind and choose card[1]
    return p, 1 if p[1] == 1 else 2

def guess(p):
    # choose card[0] or the other one
    choice = random.choice((0, p[1]))
    return choice, p[0][choice] == 1

def test(epoch):
    count1 = 0
    right1 = 0
    count2 = 0
    right2 = 0

    for i in range(epoch):
        p = gen_problem()
        ret = guess(p)
        if ret[0] == 0:
            count1 += 1
            if ret[1]:
                right1 += 1
        else:
            count2 += 1
            if ret[1]:
                right2 += 1
    print "Guess A:", float(right1) / count1
    print "Guess the other:", float(right2) / count2

test(100000)

