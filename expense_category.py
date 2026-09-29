def category_filter(expenses):
    L1=[]
    for i in expenses:
        L1.append(i["category"])
    L2=list(set(L1))

    print("Available Categories:")

    for i in L2:
        print("\n•",i)


    x=input("\nEnter category:").lower()

    if x not in L2:
        print("\nNo expenses of this category")

    for i in expenses:
        if x==i["category"].lower():
            print("\n",i)
    





    
