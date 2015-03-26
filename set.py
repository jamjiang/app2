__author__ = 'jamjiang'
from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersection
fulltime_management = managers - engineers - programmers # difference
engineers.add('Marvin')                                  # add element
print engineers


print 'before update employees:',employees.issuperset(engineers)     # superset test
employees.update(engineers)         # update from another set
print 'after update employees:', employees.issuperset(engineers)
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')          # unconditionally remove element
    print group