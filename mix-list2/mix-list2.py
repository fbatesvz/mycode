#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print (proto)
proto.append('dns') #will add dns to ernd of line
protoa.append('dns') #will add dns to ernd of line
print (proto)
proto2= [ 22, 80, 443, 53] #list of common ports
proto.extend(proto2) #pass proto ptoto2 as an argumentto extendmethod
print (proto)
protoa.append(proto2) #Pass proto2 as n argument to append 
print (protoa)


