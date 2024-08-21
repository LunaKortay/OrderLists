numberList = []


def numberInput(count):
    for x in range(count):
        try:
            numberList.append(int(input("Number to add to the list: ")))
        except ValueError:
            print("Please enter a valid number!!")
    print(numberList)
    sortAll(numberList)


def sortAll(List):
    List2 = []
    for k in range(len(List)):
        List2.append("-")
    for j in range(len(List)):
        listIndex = 0
        for i in range(len(List)):
            if j == i:
                print("equal")
            else:
                if List[j] < List[i]:
                    listIndex += 1
                    print(f" {List[j]}, {List[i]}, {listIndex}")
        List2[listIndex] = List[j]
    print(List2)


def main():

    while True:
        userInput = input("Would you like to input numbers? yes / no \n")
        if userInput == "yes":
            howMany = int(input("How many?\n"))
            numberInput(howMany)
            break
        elif userInput == "no":
            break
        else:
            print("please enter a valid option! \n")


if __name__ == "__main__":
    main()
