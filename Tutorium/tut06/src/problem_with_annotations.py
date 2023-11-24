from mylist import MyList

lst: MyList[int] = MyList()
lst.push_back(0)
lst.push_back(1)
print(lst)  # [0, 1]
lst.push_back("haha not a number")
print(lst)  # [0, 1, haha not a number]
