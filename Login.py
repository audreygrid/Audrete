#!/usr/bin/env python2.7
def MakePassword():
    attempts = 3
    print("WELCOME")
    print("Enter your username: ")
    UserName = input()
    print("Enter your password: ")
    Password = input()
    print('Login to your account')
    print("Enter your username: ")
    AttemptedUserName = input()
    can = True
    while can:
        if AttemptedUserName == UserName:
            print('Input your password now')
            AttemptedPassword = input()
            if AttemptedPassword == Password:
                print('You may proceed')
                can = False
            else:
                if attempts < 0 or attempts==0:
                    print('no more attempts')
                else:
                    print('Incorrect password')
                    AttemptedPassword = input()
        else:
            if attempts < 0 or attempts==0:
                print('No more attempts')
            else:
                print('Incorrect username')
                AttemptedUserName = input()

if __name__ == '__main__':
    MakePassword()