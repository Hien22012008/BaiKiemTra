Username = input('Input username:')
Password = int(input('Input password:'))
Email = input('Input email:')

if Username == 'admin' and Password == '12345' and Email == 'abc@gmail.com':
    print('Register successfully')
else:
    print('Register failed')