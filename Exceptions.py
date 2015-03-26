__author__ = 'jamjiang'
#can't run this program inside Pycharm, please run in CLI

import sys
try:
    s = raw_input('enter something ->')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error/exception occurred.'
print 'Done'