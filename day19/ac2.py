import random
import time
def getRandomDate(startDate, endDate):
    print("printing random date between ",startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%Y/%d"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strp(endDate, dateFormat))

    randomTime = startTime +randomGenerator *(endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ",getRandomDate("01/2025/01", "08/2025/29"))