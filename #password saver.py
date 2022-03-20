#password saver
twitter_pass = '123'
facebook_pass = '123'
google_pass = '123'
amazon_pass = '123'
tiktok_pass = '123'
netflix_pass = '123'
arlo_cams_pass = '123'
pass_access_select = input('Welcome! What password do you want to access?').lower()
if pass_access_select == 'twitter':
    security_pin = input('What is your security pin? ')
    if security_pin == '123':
        print('Ok, your twitter password is', twitter_pass)
    else:
        quit()
if pass_access_select == 'facebook':
    security_pin = input('What is your security pin? ')
    if security_pin == '123':
        print('Ok, your facebook password is', facebook_pass)
    else:
        quit()
if pass_access_select == 'google':
    security_pin = input('What is your security pin? ')
    if security_pin == '123':
      print('Ok, your google password is', google_pass)
    else:
        quit()

if pass_access_select == 'amazon':
    security_pin = input('What is your security pin? ')
    if security_pin == '123':
        print('Ok, your Amazon password is', amazon_pass)
    else:
        quit()

if pass_access_select == 'tiktok':
    input('What is your security pin? ')
    if security_pin == '123':
        print('Ok, your tiktok password is', tiktok_pass)
    else:
        quit()
restart = input('Do you want to access another password? ').lower()
if restart == 'yes':
    pass_access_select = input('This is your final view. To view more than 2 passwords, relaunch the program. What password do you want to access?').lower()
    if pass_access_select == 'twitter':
     security_pin = input('What is your security pin? ')
     if security_pin == '123':
        print('Ok, your twitter password is', twitter_pass)
     else:
        quit()
    if pass_access_select == 'facebook':
     security_pin = input('What is your security pin? ')
     if security_pin == '123':
        print('Ok, your facebook password is', facebook_pass)
     else:
        quit()
    if pass_access_select == 'google':
     security_pin = input('What is your security pin? ')
     if security_pin == '123':
      print('Ok, your google password is', google_pass)
     else:
        quit()

    if pass_access_select == 'amazon':
     security_pin = input('What is your security pin? ')
     if security_pin == '123':
        print('Ok, your Amazon password is', amazon_pass)
     else:
        quit()

    if pass_access_select == 'tiktok':
     security_pin = input('What is your security pin? ')
     if security_pin == '123':
        print('Ok, your tiktok password is', tiktok_pass)
     else:
        quit()
if restart == 'no':
    quit()
