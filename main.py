len = int(input('length?'))
wid = int(input('width?'))

def build(len, wid):
   area = len * wid
   return area

print(build(len, wid))

rad = int(input('radius?'))

def calc(rad):
    circumference = 2 * 3.14 * rad
    return circumference

print(calc(rad))