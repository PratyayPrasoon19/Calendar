def printmonth(mm,yyyy):
    lpyr=0
    for i in range(1900,yyyy):
        if (i%4==0 and i%100!=0 or i%400==0):
            lpyr+=1
    no_of_days = (yyyy-1900)*365+lpyr
    for i in range(1,mm):
        if i==2:
            if (yyyy%4==0 and yyyy%100!=0 or yyyy%400==0):
                no_of_days+=1
            else :
                no_of_days+=0
        elif i in [1,3,5,7,8,10,12]:
            no_of_days+=31
        elif i in [4,6,9,11]:
            no_of_days+=30
    weekday=no_of_days%7

    month={1:'January',2:'Febuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    print('\n\n\t\t\t',month.get(mm),yyyy,'\n\n\tMon\tTue\tWed\tThur\tFri\tSat\tSun\n')

    if mm in [1,3,5,7,8,10,12]:
        td=31
    elif mm in [4,6,9,11]:
        td=30
    elif mm==2:
        if (yyyy%4==0 and yyyy%100!=0 or yyyy%400==0):
            td=29
        else:
            td=28
    for i in range(0,weekday+1):
        print("\t",end='')
    for i in range(1,td+1):
        if (weekday%7==6):
            print(i,'\n\t',end="")
        else:
            print(i,'\t',end="")
        weekday+=1
def printyear(yyyy):
    for i in range (1,13):
        printmonth(i,yyyy)
