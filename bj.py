import random, sys

def new_card():
    return random.randrange(2,12)


print('\nh = hit')
print('sp = split')
print('s = stand')
print('d = double down')
print('su = surrender')
print('i = insurance')
print('e to exit \n')

map = {}
map[2] = '2'
map[3] = '3'
map[4] = '4'
map[5] = '5'
map[6] = '6'
map[7] = '7'
map[8] = '8'
map[9] = '9'
map[10] = '10'
map[11] = 'A'

file = open('data.txt','r')
data = {}
it = 1
key = ''
value = ''
for line in file:
    it = 1
    for symbol in line.split():
        if it == 1:
            key = symbol + '_'
        elif it == 2:
            key += symbol + '_'
        elif it == 3:
            key += symbol
        elif it == 4:
            value = symbol
        it += 1
    data[key] = value

while True:
    tens = ['10','J','Q','K']
    card_1 = new_card()
    card_2 = new_card()
    dealer_card = new_card()
    if card_1 == 10:
        c1 = random.choice(tens)
    else:
        c1 = map[card_1]
    if card_2 == 10:
        c2 = random.choice(tens)
    else:
        c2 = map[card_2]
    if dealer_card == 10:
        c3 = random.choice(tens)
    else:
        c3 = map[dealer_card]
    print(c1, c2,'vs', c3)

    guess = input()
    guess = guess.strip()
    answer = data[str(card_1)+'_'+str(card_2)+'_'+str(dealer_card)].lower()
    if guess == 'e':
        sys.exit()
    elif guess == answer:
        print('correct')
    else:
        print('wrong, correct move is:',answer)
    print('')





