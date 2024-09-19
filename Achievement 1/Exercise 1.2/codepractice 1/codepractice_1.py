import time

f = open('./codepractice1.txt', 'r')
lines = f.readlines()
# Remove spaces at the beginning and at the end of the string
[principal, rate, time_period] = [x.strip('\n') for x in lines]
f.close()

print(type(principal))
print(type(rate))
print(type(time_period))

print('\n Type Casting the variables "principla", "rate", and "time_period" \n')
principal = float(principal) 
rate = float(rate)
time_period = float(time_period)

print(type(principal))
print(type(rate))
print(type(time_period))
time.sleep(5)

compound_principal = principal*(1 + rate)//(time_period)
print("compound_principal=",compound_principal)
print(type(compound_principal))