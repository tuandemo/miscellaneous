# -*- coding: utf-8 -*-

import random
import math


def clear():
    os = __import__('os')
    if os.name is 'nt':
        os.system('cls')
        os.system('title h-puzzle')
    else:
        os.system('clear')
        os.system('echo "\033]0;h-puzzle\007"')


def permute(n, k):

    n_list = [(x + 1) for x in range(n)]
    queue = []

    lower_bound = 0
    while True:
        if n is 0:
            break

        factor = math.factorial(n - 1)
        for i in range(n):
            if lower_bound + i * factor <= k <= lower_bound + (i + 1) * factor:
                queue += [n_list[i]]
                lower_bound += i * factor
                n_list.pop(i)
                n -= 1
                break

    return queue


def generate(n = 9):
    y = list((i + 1) for i in range(n))
    hiden_pos = random.randrange(0, n)
    y[hiden_pos] = None

    factorial_n = math.factorial(n)
    while True:
        random_permutation = random.randrange(0, factorial_n) + 1
        x = permute(n, random_permutation)
        x[x.index(hiden_pos + 1)] = None
        if solvable(x): break


    print('%d-puzzle game | %d-%d' % (n - 1, random_permutation, hiden_pos + 1))
    input('> start\r')

    show(y)
    print('  this is the target')
    input('> understand\r')

    return x, y


def show(x):
    clear()
    printed = 0
    n = int(math.sqrt(len(x)))
    for i in x:
        if i is None: print('%3s' % ('#'), end=' ')
        else: print('%3d' % (i), end=' ')
        printed += 1
        if (printed % n) is 0: print()


def move(x, state = 'x', no_state = 'x'):

    pos = x.index(None)
    n = len(x)
    sqrt_n = int(math.sqrt(len(x)))

    LEFT_POSITION = [i for i in range(0, n, sqrt_n)]
    RIGHT_POSITION = [i for i in range(sqrt_n - 1, n, sqrt_n)]
    TOP_POSITION = [i for i in range(sqrt_n)]
    BOTTOM_POSITION = [i for i in range(n - sqrt_n, n)]

    if state is 'l' and not no_state is 'r':
        if pos in LEFT_POSITION: return False
        else:
            temp = x[pos]
            x[pos] = x[pos - 1]
            x[pos - 1] = temp
    elif state is 'r' and not no_state is 'l':
        if pos in RIGHT_POSITION: return False
        else:
            temp = x[pos]
            x[pos] = x[pos + 1]
            x[pos + 1] = temp
    elif state is 'u' and not no_state is 'd':
        if pos in TOP_POSITION: return False
        else:
            temp = x[pos]
            x[pos] = x[pos - sqrt_n]
            x[pos - sqrt_n] = temp
    elif state is 'd' and not no_state is 'u':
        if pos in BOTTOM_POSITION: return False
        else:
            temp = x[pos]
            x[pos] = x[pos + sqrt_n]
            x[pos + sqrt_n] = temp
    else: return False

    if no_state is 'x': show(x)

    return True


def solve(x, y, solution):
    solution += ['Go', 'fuck', 'yourself']
    return solution


def help():
    print('--------')
    print('l - left')
    print('r - right')
    print('u - up')
    print('d - down')
    print('--------')
    print('h - help')
    print('x - exit')
    input('> understand\r')


def is_square_number(n):
    if n <= 0: return False
    return int(math.sqrt(n)) ** 2 is n


def solvable(x):
    N = []
    n = len(x)
    for num in x:
        if num is None: continue
        count = 0
        index = x.index(num)
        for i in range(index + 1, n):
            if x[i] is None: continue
            if x[i] < num: count += 1
        N += [count]

    square_n = int(math.sqrt(n))
    if square_n % 2 == 1:
        return sum(count for count in N) % 2 == 0
    else:
        if (x.index(None) % square_n) % 2 == 1:
            return sum(count for count in N) % 2 == 0
        else:
            return sum(count for count in N) % 2 == 1


def play(n = 9):

    if n > 100: n = 9 # i think it should be under-100-puzzle game
    if not is_square_number(n): n = 9

    x, y = generate(n)

    show(x)

    _ = 0 # dont care about this

    while True:
        state = input('  move the #\r')

        if state is 'x':
            print('  exited')
            return 0
        if state is 'h':
            help()
            continue
        if state is 's':
            input('> you want a solution?\r')
            print(solve(x[:], y, []))
            continue

        if not move(x, state):
            print('  cannot move')
            _ += 1
            if _ is 3:
                raise Exception('are you fucking blind?')
        else:
            _ = 0

        if x is y:
            print('  won')
            return 1


def wtf(ex):
    try:
        input('> what the fuck just happened?\r')
    except:
        print()
        print('  who cares?', end='\r')
    finally:
        print(' ', ex)


def main(arg = 9):
    clear()
    try:
        try: n = int(arg)
        except: n = 9
        play(n)
    except Exception as ex:
        wtf(ex)
    else:
        print('  see you again!')


if __name__ == '__main__':
    sys = __import__('sys')
    if len(sys.argv) > 1: main(sys.argv[1])
    else: main()
else:
    raise Exception('Just an exception bro!')

