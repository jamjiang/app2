__author__ = 'jamjiang'
def total(*numbers, **keywords):
    count = 0
    for number in numbers:
        count += number
        print count
    print '\n'
    for key in keywords:
        count += keywords[key]
        print count
    print '\n'
    return count

print (total (1,2,3,vegetables=40,n9k=60,fruits=100))
