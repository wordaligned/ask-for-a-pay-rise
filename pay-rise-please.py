# The Art and Craft of Approaching your Head of Department to Submit a request for a Raise
# Georges Perec

START, END = 1, 1000000

nodes = {
    1: ("Go to see Mr X", 2),
    2: ("Is Mr X in his office?", 3, 15),
    3: ("Knock on the door", 4),
    4: ("Does he look up?", 5, 13),
    5: ("Encouragingly?", 6, 21),
    6: ("Enter", 7),
    7: ("Does he offer you a seat?", 8, 33),
    8: ("Relax", 9),
    9: ("Explain your problem", 10),
    10: ("Is it a T60 issue?", 11, 45),
    11: ("Go to the relevant office", 12),
    12: ("Go from office to office", 13),
    13: ("Think", 14),
    14: ("Make your mind up", 1),
    15: ("Hang around in the corridor", 16),
    16: ("Is Ms Y in her office?", 17, 44),
    17: ("Is she in a good mood?", 18, 44),
    18: ("Have a chat with Ms Y", 19),
    19: ("Can you see Mr X?", 20, 18),
    20: ("Find an excuse to leave", 13),
    21: ("Does he tell you to come back at two thirty?", 22, 13),
    22: ("Go back to your desk", 23),
    23: ("Is it Friday?", 24, 28),
    24: ("Find out the cafeteria lunch menu.", 25),
    25: ("Was fish on?", 26, 31),
    26: ("Did he swallow a bone?", 27),
    27: ("Wait until the next day", 13),
    28: ("Is it Lent?", 24, 29),
    29: ("Is it Monday?", 30, 27),
    30: ("Wait until two thirty", 13),
    31: ("Eggs?", 32, 30),
    32: ("Were they off?", 27, 30),
    33: ("Ask if one of his daughters has measles?", 34, 37),
    34: ("Is his face spotty?", 35, 8),
    35: ("Emergency", 36),
    36: ("Put Mr X in quarantine for 40 days!", 13),
    37: ("Ask if two of his daughters have measles?", 38, 39),
    38: ("Find an excuse to leave", 35),
    39: ("Ask if three of his daughters have measles?", 40, 41),
    40: ("Make a rapid exit", 35),
    41: ("And is the fourth OK?", 42, 43),
    42: ("Enough's enough", 9),
    43: ("Wait forty days", 13),
    44: ("Take a trip round the lab", 13),
    45: ("Can another department handle the enquiry?", 46, 56),
    46: ("Are they interested in your case?", 47, END),
    47: ("Do they think your question makes sense?", 48, END),
    48: ("Do they have time to deal with it?", 49, END),
    49: ("Do they really understand what you want?", 50, 54),
    50: ("Do they congratulate you?", 51),
    51: ("Sorry, nothing doing", 52),
    52: ("Return to your desk", 53),
    53: ("Ponder your next problem", 13),
    54: ("Send Mr X to T.V.1", 55),
    55: ("Leave him to absorb the message", 13),
    56: ("Do you want a pay rise?",  57, 52),
    57: ("Have you recently been involved in a major success?", 58, 64),
    58: ("Insist on a pay rise", 59),
    59: ("Did you get one?", 60),
    60: ("Nope", 61),
    61: ("Is there any hope?", 62, 63),
    62: ("Wait for six months", 13),
    63: ("Wait for six months", 53),
    64: ("Do you get on with the engineer?", 58, 52)
}


def main():
    state = START
    while state != END:
        message, *states = nodes[state]
        if len(states) == 1:
            print(message)
            state = states[0]
        else:
            yes, no = states
            if input(message + " ").lower() in {"y", "yes"}:
                state = yes
            else:
                state = no
    print("Nothing doing. Bye for now.")

main()
        
