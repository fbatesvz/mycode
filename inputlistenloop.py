#!/usr/bin/env  python3

def main():
    # Read in our liwt eqtq
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: #single line from our file is sline
            #append adds to tend of our list
            #rstrip removes and special charcters on the right of the str
            #split breaks our string into a list
            #the result is we add a list of driver qn ip to networklists
            networklists.append(sline.rstrip("\n").split(''))
    print(networklists) # display networklist to ensure rcrqted

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
