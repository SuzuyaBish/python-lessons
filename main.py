# Find two numbers in the list that equal the target

# len of the list == 7
# range of the list == 0..6


def twoSum(numberList, target):
    for i in range(len(numberList) - 1):
        if numberList[i] + numberList[i + 1] == target:
            return True
    return False


listOfNumbers = [0, 3, 6, 9, 12, 15, 18]
target = 9

result = twoSum(listOfNumbers, target)

if result:
    print("Target in list of numbers!")
else:
    print("Target not in list of numbers!")


# WHATS UP BITCH
