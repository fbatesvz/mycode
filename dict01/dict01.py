#!/user/bin/env python3

def main():
    ##create dictionary
    switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version':'1.2', 'vendor': 'cisco'}

    ## display parts of the dictionary
    print( switch['hostname'])
    print(switch['ip'])

    ## request a 'fake' key
    #print( switch['lynx'])

    ## request a fake key with .get() method
    print( "First test - .get()")
    print( switch.get('lynx'))

    print("Second test - .get()")
    print( switch.get('lynx', "The KEY IS IN ANOTHER CASTLE"))
    print ( "Third test - .get()")
    print(switch.get('version'))

    print( "Forth Test - .keys()")
    print(switch.values())

    print( "Fifth test - .valuews()")
    print( switch.values())





main()

