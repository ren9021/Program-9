#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         9
#
#  File Name:         Program9.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          11-4-19
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapters # 1-7
#
#  Description:
#     This program reads and displays the contents of a file.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#***************************************************************

def main():
    developerInfo()
    print('RAINFALL STATS FOR THE YEAR')
    print('')
    print('')
    rainfile = Convert()
    total = TotalRain(rainfile)
    AvgRain(total)
    Months = AllMonths(rainfile)
    
#***************************************************************
#
#  Function:     Convert
# 
#  Description:  Opens and converts the file's contents into a float
#
#  Parameters:   None
#
#  Returns:      The full list converted to float values
#
#***************************************************************   

def Convert():
    infile = open('Program9.txt', 'r')
    Rainfall = infile.readlines()
    infile.close()
    index = 0
    while index < len(Rainfall):
        Rainfall[index] = float(Rainfall[index])
        index += 1
    return Rainfall

#***************************************************************
#
#  Function:     TotalRain
# 
#  Description:  Adds up all the inches of rain for the year
#
#  Parameters:   inches
#
#  Returns:      The total inches of rain
#
#***************************************************************

def TotalRain(inches):
    total = 0
    for num in inches:
        total += num
    print('The total rainfall for the year is', format(total, '.2f'))
    print('')
    return total

#***************************************************************
#
#  Function:     AvgRain
# 
#  Description:  Calculates the average total of the rain for the year
#
#  Parameters:   inches
#
#  Returns:      Nothing
#
#***************************************************************

def AvgRain(inches):
    average = inches / 12
    print('The average of monthly rainfall is', format(average, '.2f'))
    print('')
    
#***************************************************************
#
#  Function:     AllMonths
# 
#  Description:  Determines the months with the highest and lowest
#                inches of rain for the year
#
#  Parameters:   rain
#
#  Returns:      Nothing
#
#***************************************************************

def AllMonths(rain):
    MonthList = [['Jan'],['Feb'],['Mar'],['Apr'],['May'],['Jun'],['Jul'],['Aug'],['Sep'],['Oct'],['Nov'],['Dec']]
    min_value = min(rain)
    max_value = max(rain)
    IdxMin = rain.index(min_value)
    IdxMax = rain.index(max_value)
    MonMin = MonthList[IdxMin]
    MonMax = MonthList[IdxMax]
    print('The month with the lowest amounts of rainfall is', min(MonMin))
    print('')
    print('The month with the highest amounts of rainfall is', max(MonMax))

#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Course:   Programming Fundamentals I')
    print('Program:  9')
    print()
    # End of the developerInfo function

# Call the main function.
main()



