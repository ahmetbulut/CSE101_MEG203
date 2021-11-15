

def countdown_to_zero(n):

    print('Start the countdown...')

    while n > 0:
        print(n)

        if n == 11:
            break

        n = n - 1

    print('We are done!')



countdown_to_zero(20)