# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:10:27 2022

@author: jingy
"""

def mutualFriends(myFriends,yourFriends):
    mutualFriends = myFriends.intersection(yourFriends)
    mutualFriends = list(mutualFriends)
    mutualFriends.sort()
    return mutualFriends

def ourFriends(myFriends,yourFriends):
    ourFriends = myFriends.union(yourFriends)
    ourFriends = list(ourFriends)
    ourFriends.sort()
    return ourFriends

def theirFriends(myFriends,yourFriends):
    theirFriends = yourFriends.difference(myFriends)
    theirFriends = list(theirFriends)
    theirFriends.sort()
    return theirFriends

def primes(n):
    set_ints = [i for i in range(1, n+1)]
    set_composite = []
    p = 2
    while p < n:
        for i in range(p+1, n+1):
            if i % p == 0:
                set_composite.append(i)
        p += 1
    set_ints = set(set_ints)
    set_composite = set(set_composite)
    primes = set_ints.difference(set_composite)
    primes.remove(1)
    return primes

if __name__ == '__main__':
    myFriends = set(['Amanda', 'Bobby', 'Cathy', 'Dave', 'Ellen']) 
    yourFriends = set(['Adam', 'Brent', 'Cathy', 'Daniel', 'Ellen'])
    print(mutualFriends(myFriends,yourFriends))
    print(ourFriends(myFriends,yourFriends))
    print(theirFriends(myFriends,yourFriends))
    print(primes(10))
        