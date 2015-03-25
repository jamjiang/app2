__author__ = 'jamjiang'
while True:
    s=raw_input('enter somthing<enter quit to exit>:')
    if s== 'quit':
        break
    if len(s)<3:
        print'too small'
        continue
    print('input is of sufficient length')
