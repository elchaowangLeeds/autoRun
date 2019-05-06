
import pyautogui as pag
import os
import time
import datetime


ISOTIMEFORMAT_Y = '%Y'
ISOTIMEFORMAT_m = '%m'
ISOTIMEFORMAT_d = '%d'
ISOTIMEFORMAT_H = '%H'
ISOTIMEFORMAT_M = '%M'

def autoRun():
    pag.rightClick(500,500)
    time.sleep(2)
    pag.moveTo(570, 565)
    time.sleep(1)
    pag.click(570, 565)
    print('I am waiting for remote')
    time.sleep(20)
    return True

def main():
    print('please input the time you want this program to stop')
    print('Month:')
    endMonth = input()
    endMonth = int(endMonth)
    print('Day:')
    endDay = input()
    endDay = int(endDay)
    print('Hour:')
    endHour = input()
    endHour = int(endHour)
    print('Minutes:')
    endMin = input()
    endMin = int(endMin)

    print('Please select the task you want the PC do when time is up:')
    print('0: nothing,  1: turn off')
    endCMD = input()
    endCMD = int(endCMD)
    while True:
        currentTime_m = datetime.datetime.now().strftime(ISOTIMEFORMAT_m)
        currentTime_m = int(currentTime_m)

        currentTime_d = datetime.datetime.now().strftime(ISOTIMEFORMAT_d)
        currentTime_d = int(currentTime_d)

        currentTime_H = datetime.datetime.now().strftime(ISOTIMEFORMAT_H)
        currentTime_H = int(currentTime_H)

        currentTime_M = datetime.datetime.now().strftime(ISOTIMEFORMAT_M)
        currentTime_M = int(currentTime_M)
        print(currentTime_H)
        if currentTime_m == endMonth and currentTime_d == endDay and currentTime_H == endHour and currentTime_M >= endMin:
            print('program end!')
            break
        else:
            autoRun()
    if endCMD == 1:
        print('system will shutdown in 60 seconds')
        os.system('shutdown -s -t 60')
        while True:
            cancelCMD = input()
            if cancelCMD == 'cancel':
                os.system('shutdown /a')
                break

    return True

if __name__ == '__main__':
    main()