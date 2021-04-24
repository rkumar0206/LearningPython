n = int(input('Enter the number : '))

# FIRST WAY

# if n % 2 != 0:
#     print('Weird')
# elif n >= 2 and n <= 5:
#     print('Not Weird')
# elif n >= 6 and n < 20:
#     print('Weird')
# else:
#     print('Not Weird')


# SECOND WAY

# if n % 2 != 0:
#     print('Weird')
# elif 2 <= n <= 5:
#     print('Not Weird')
# elif 6 <= n < 20:
#     print('Weird')
# else:
#     print('Not Weird')


# THIRD WAY

if n % 2 != 0:
    print('Weird')
elif n in range(2, 5):
    print('Not Weird')
elif n in range(6, 20):
    print('Weird')
else:
    print('Not Weird')
