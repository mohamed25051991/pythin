num_of_try = 0

while num_of_try != 3:
    username = input('username :')
    password = input('password :')
    if username == 'mohamed' and password == '91':
        print ('welcome')
        exit()
    elif username == 'mohamed' and password != '91':   
        print ('pass incorect')
        num_of_try += 1
        print('you have' + str(3- num_of_try) +'tries')
    else:
        print('error')
        num_of_try +=1
        print('you have' + ' ' +str(3- num_of_try) + ' ' + 'tries')