while True:
    try:
        n = int(input())
        
        if n%400==0:
            print('閏年')
        elif n%100==0:
            print('平年')
        elif n%4==0:
            print('閏年')
        else:
            print('平年')

    except EOFError:
        break