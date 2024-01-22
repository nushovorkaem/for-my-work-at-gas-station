#code for my job

while True:
    try:
        received_data = int(input('Stats - 1\nCalculate date for epire dates - 2\nCalculate time for unfreezing dates - 3\nTurn this fcking annoying programm off - 4\nWhich option do you want to use?: '))
        #There is plans like provide my schedule of shifts and check it, make notifications, set alarms automatically and to parse bus graffic 
        if received_data == 1:
            print('hui')
        elif received_data == 2:
            print('pizda')   
        elif received_data == 3:
            print('co jeszcze?')    
        elif received_data == 4:
            print('Bye Bye 😏🤫')
            break
    except ValueError as ve:
        print(f'Error. {ve}')