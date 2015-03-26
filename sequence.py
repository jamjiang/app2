__author__ = 'jamjiang'
#!/usr/bin/python
# Filename: seq.py
hostlist = ['n9k1', 'n7k1', 'n5k1', 'n5k2']
print hostlist [2][1]
# Indexing or 'Subscription' operation
print 'Item 0 is', hostlist[0]
print 'Item 1 is', hostlist[1]
print 'Item 2 is', hostlist[2]
print 'Item 3 is', hostlist[3]
print 'Item -1 is', hostlist[-1]
print 'Item -2 is', hostlist[-2]
# Slicing on a list
print 'Item 1 to 3 is', hostlist[1:3]
print 'Item 2 to end is', hostlist[2:]
print 'Item 1 to -1 is', hostlist[1:-1]
print 'Item start to end is', hostlist[:]
# Slicing on a string
name = 'n9k1'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]