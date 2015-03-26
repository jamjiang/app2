__author__ = 'jamjiang'
hostlist = ['n9k1', 'n7k1', 'n7k2', 'ucsd1']
print 'I have', len(hostlist),'hosts.'
print 'These hosts are:', # Notice the comma at end of the line
for item in hostlist:
	print item,
print '\nI also have to include apic1.'
hostlist.append('apic1')
print 'My hostlist  is now', hostlist
print 'I will sort my list now'
hostlist.sort()
print 'Sorted hostlist  is', hostlist
print 'The first host I will configure is', hostlist[0]
olditem = hostlist[0]
del hostlist[0]
print 'I got the', olditem
print 'My hostlist is now', hostlist
