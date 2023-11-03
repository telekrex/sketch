#!/usr/bin/env python3
# Written by telekrex
from random import choice


def pick(file):

    with open(f'{file}.txt', 'r', encoding='UTF-8') as f:

        return choice(f.read().split('\n'))


try:

    for i in range(99):

            subject = str(pick("Sketch-Library/subjects")[:100])
            action = str(pick("Sketch-Library/actions")[:100])
            environment = str(pick("Sketch-Library/environments")[:100])
            # modifiers only appear 25%
            # of the rolls
            if choice([1, 2, 3, 4]) == 4:
                modifier = str(pick("Sketch-Library/modifiers")[:100])
                print(f'\n Try to draw -> {subject} {modifier} {action} {environment}\n')
            else:
                print(f'\n Try to draw -> {subject} {action} {environment}\n')
            
            input(' Press any key to go again\n or CTRL + C to exit.')
    
    print('\n\n Program is tired! Restart to keep playing.')

except KeyboardInterrupt:
    print('\n\n Goodbye!')
