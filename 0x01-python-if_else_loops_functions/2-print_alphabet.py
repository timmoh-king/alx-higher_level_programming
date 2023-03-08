#!/usr/bin/python3

#for alphabet in range (97,123):
    #print(chr(alphabet), end="")
for alpha_letters in range(ord('a'), ord('z')+1):
    print("{:c}".format(alpha_letters), end="")
