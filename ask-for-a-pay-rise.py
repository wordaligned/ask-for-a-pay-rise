# The Art and Craft of Approaching your Head of Department to Submit a request for a Raise
# Georges Perec

states = {
    2: ('Is Mr X in his office?', ('Knock on the door', 3), ('Hang around', 4)),
    3: ('Does he look up?', 7, ('Think', 'Make your mind up', 'Go to see Mr X', 2)),
    4: ('Is Miss Y in her office?', 5, ('Take a walk around the lab', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    5: ('Is she in a good mood?', ('Have a chat with Miss Y', 6), ('Take a walk around the lab', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    6: ('Can you see Mr X?', ('Make a rapid exit', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Have a chat with Miss Y', 6)),
    7: ('Affirmatively?', ('Enter', 16), 8),
    8: ('Are you told to come back at two thirty?', ('Go back to your desk', 9), ('Think', 'Make your mind up', 'Go to see Mr X', 2)),
    9: ('Is today Friday?', ('Find out cafeteria lunch menu', 10), ('Go to see Mr X', 2)),
    10: ('Was fish on?', 12, 13),
    11: ('Is it Lent?', ('Find out cafeteria lunch menu', 10), 15),
    12: ('Did he swallow a bone?', ('Wait until the next day', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Wait for two thirty', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    13: ('Eggs?', 14, ('Wait for two thirty', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    14: ('Were they off?', ('Wait until the next day', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Wait for two thirty', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    15: ('Is today Monday?', ('Wait until the next day', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Wait for two thirty', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    16: ('Does he ask you to be seated?', ('Relax', 'Explain the problem', 22), 17),
    17: ('Ask if one of his daughters has measles', 18, 19),
    18: ('Is his face spotty?',  ('Emergency', 'Put Mr X in quarantine for 40 days!', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Relax', 'Explain the problem', 22)),
    19: ('Ask if both his daughters have measles', ('Make rapid exit', 'Emergency', 'Put Mr X in quarantine for 40 days!', 'Think', 'Make your mind up', 'Go to see Mr X', 2), 20),
    20: ('Ask if his three daughters have measles', 21, ('Go to see Mr X', 2)),
    21: ('And is the fourth OK?', ('Enough\'s enough', 'Explain the problem', 22), ('Wait 40 days', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    22: ('Is it a T.60 issue?', ('Go to the relevant office', 'Go from office to office', 'Think', 'Make your mind up', 2), 23),
    23: ('Can another department handle the enquiry?', 24, 25),
    24: ('Are they interested in your case?', 29, 100000),
    25: ('Do you want a pay rise?',  26, ('Return to your desk', 'Ponder your next problem',  'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    26: ('Have you recently been involved in a major success?', ('Ask for a pay rise', 28), 27),
    27: ('Do you get on with the engineer?', ('Ask for a pay rise', 'You don\'t get a pay rise', 28),  ('Return to your desk', 'Ponder your next problem',  'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    28: ('Are you given reasons for hoping?', ('Wait 6 months', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Wait 6 months', 'Ponder your next problem', 'Think', 'Make your mind up', 'Go to see Mr X', 2)),
    29: ('Do they consider your question to be an intelligent one?', 30, 100000),
    30: ('Do they have time to deal with it?', 31, 100000),
    31: ('Do they really understand what you want?', ('Sorry, nothing doing', 'Return to your desk', 'Ponder your next problem', 'Think', 'Make your mind up', 'Go to see Mr X', 2), ('Send Mr X to T.V.1', 'Leave him to absorb the message', 'Think', 'Make your mind up', 'Go to see Mr X', 2))
}


def tupletize(v):
    try:
        return tuple(v)
    except TypeError:
        return (v,)

def main():
    print('Go to see Mr X')

    state = 2
    while state in states:
        prompt, yes, no = states[state]
        yes = tupletize(yes)
        no = tupletize(no)
        if input(prompt + ' ').lower() in {'y', 'yes'}:
            *info, state = tupletize(yes)
        else:
            *info, state = tupletize(no)
        if info:
            print(*info, sep='\n')

    print('Give up.')

main()
        
