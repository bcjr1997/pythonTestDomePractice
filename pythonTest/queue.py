#Works for simple examples but not huge ones
movingTotalDict = dict()
currentList = list()
class MovingTotal:

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        global currentList
        
        if len(currentList) == 0:
            currentList = numbers
        else:
            for i in range(len(numbers)):
                currentList.pop(0)
                currentList.append(numbers[i])
            
        if str(currentList) not in movingTotalDict:
            total = 0
            for number in currentList:
                total += number
            movingTotalDict[str(currentList)] = total

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        
        for key in movingTotalDict.keys():
            if total == movingTotalDict[key]:
                return True
        
        return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))