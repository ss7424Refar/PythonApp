args = [1, 6, 7]
print list(range(*args))

def parrot(voltage, state='stuff', action='voom'):
    print "parrot", voltage, state, action

words = {"voltage": "hello", "state": "save", "action": "voo"}
parrot(words)
parrot(**words)