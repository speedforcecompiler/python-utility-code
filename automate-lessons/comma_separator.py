spam = []

def separator(lister):
    if len(lister) != 0:
        for key,item in enumerate(lister):
            if (len(lister) - key) != 1:
                print(item+",", end=" ")
            else:
                print("and "+item)
    else:
        print("The list is empty")

separator(spam)