def ask_ok(prompt, restries=4, complaint='Yes or No'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        restries = restries - 1
        if restries < 0:
            raise IOError('refusnik user')
        print complaint
# return = exit
# ask_ok('Do you really want to quit?')

# ask_ok('OK to write file', 2)
ask_ok('OK to write', 3, 'come on')


