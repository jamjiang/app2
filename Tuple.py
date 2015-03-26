__author__ = 'jamjiang'
cloud_hosts = ('nova1', 'neutron1', 'horizon')
print 'Number of hosts in the cloud is', len(cloud_hosts)
dc_hosts = ('db1', 'web1', cloud_hosts)
print 'Number of hosts in the datacenter is', len(dc_hosts)
print 'All hosts in datacenter are', dc_hosts
print 'hosts  from cloud are', dc_hosts[2]
print 'Last host from cloud is', dc_hosts[2][2]

mylist = [1,2,3]
ListInTuple = ('a','b',mylist)
print ('mylist in tuple is:'),
print ListInTuple
