def firstSundays():
    firstSuns = 0
    days = 6
    for year in range(1, 101):
        days = (days + 31) % 7 #Jan 1st
        if days == 0:
            firstSuns += 1
            
        days = (days + 31) % 7 #Feb 1st
        if days == 0:
            firstSuns += 1
            
        if (year % 4) == 0: #March 1st
            days = (days + 29) % 7
        else:
            days = (days + 28) % 7
        if days == 0:
            firstSuns += 1

        days = (days + 31) % 7 #April 1st
        if days == 0:
            firstSuns +=1

        days = (days + 30) % 7 #May 1st
        if days == 0:
            firstSuns += 1

        days = (days + 31) % 7 #June 1st
        if days == 0:
            firstSuns += 1

        days = (days + 30) % 7 #July 1st
        if days == 0:
            firstSuns += 1

        days = (days + 31) % 7 #August 1st
        if days == 0:
            firstSuns += 1

        days = (days + 31) % 7 #September 1st
        if days == 0:
            firstSuns += 1

        days = (days + 30) % 7 #October 1st
        if days == 0:
            firstSuns += 1

        days = (days + 31) % 7 #November 1st
        if days == 0:
            firstSuns += 1

        days = (days + 30) % 7 #December 1st
        if days == 0:
            firstSuns += 1

    return firstSuns

print(firstSundays())
