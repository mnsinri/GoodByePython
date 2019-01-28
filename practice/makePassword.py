from inorilib import Minase

pin = Minase()
limit = input('How do you want the length of your pin code to be ? :')

new_pin = pin.makePassword(limit)
print('your pin code({0} charactors) is : {1}'.format(limit, new_pin))
