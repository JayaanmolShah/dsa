'''
To create ADT that implement the "set" concept. 
a. Add (new Element) -Place a value into the set , b. Remove 
(element) Remove the value c. Contains (element) Return 
true if element is in collection, d. Size () Return number of 
values in collection Iterator () Return an iterator used to loop 
over collection, e. Intersection of two sets , f. Union of two 
sets, g. Difference between two sets, h. Subset 
'''
aset=[]
bset=[]

anum=int(input('size of set A '))
for i in range(anum):
    val=int(input('val '))
    aset.append(val)
print(aset)

bnum=int(input('size of set B '))
for i in range(bnum):
    val=int(input('val '))
    bset.append(val)
print(bset)

while True:
    print("\na. Add (new Element) -Place a value into the set\nb. Remove (elementRemove the value \nc. Contains (element) Return true if element is in collection, \nd. Size () Return number of values in collection Iterator ()Return an iterator used to loop over collection, \ne. Intersection of two sets , \nf. Union of two sets, \ng. Difference between two sets, \nh. Subset\ni.TO STOP")
    choice=input('option ')
    if choice=='a':
        cset=input('set? ')
        if cset=='a':
            num=int(input('NUM '))
            aset.append(num)
        elif cset=='b':
            num=int(input('NUM '))
            bset.append(num)
    elif choice=='b':
        cset=input('set? ')
        if cset=='a':
            num=int(input('NUM '))
            aset.remove(num)
        elif cset=='b':
            num=int(input('NUM '))
            bset.remove(num)
    elif choice=='c':
        cset=input('set? ')
        if cset=='a':
            num=int(input('NUM '))
            if num in aset:
                print('true')
            else:
                print('false')
        elif cset=='b':
            num=int(input('NUM '))
            if num in bset:
                print('true')
            else:
                print('false')
    elif choice=='d':
        cset=input('set? ')
        if cset=='a':
            print(len(aset))
        elif cset=='b':
            print(len(bset))
    elif choice=='e':
        for i in aset:
            if i in bset:
                print(i,end=",")
    elif choice=='f':
        uset=aset
        for i in bset:
            if i not in aset:
                uset.append(i)
        print(uset)
    elif choice=='g':
        cset=input('set? ')
        if cset=='a':
            for i in aset:
                if i not in bset:
                    print(i,end="")
        elif cset=='b':
            for i in bset:
                if i not in aset:
                    print(i,end="")
    elif choice=='h':
        cset=input('set? ')
        if cset=='a':
            n = len(aset)
            sublists = []
            for start in range(n):
              for end in range(start + 1, n + 1):
                  sublists.append(aset[start:end])
            print(sublists)
        elif cset=='b':
            n = len(bset)
            sublists = []
            for start in range(n):
              for end in range(start + 1, n + 1):
                  sublists.append(bset[start:end])
            print(sublists)
    elif choice=='i':
        break 
# def create_set():
#     my_set=[]
#     choice='y'
#     while(choice[0]=='y'):
#         print("\nEnter the number: ")
#         num=int(input())
#         my_set.append(num)
#         print("\n Do you want to enter more number?(y/n)")
#         choice=input()
#     return my_set

# def Add_element(A,num):
#     print("\nEnter the positon at which you want to insert the element:")
#     pos=int(input())
#     for i in range(len(A)):
#         if(i==pos):
#             A=A[:pos]+[num]+A[pos:]
#     print(A)

# def Remove_element(A,num):
#     count=0
#     for i in range(len(A)):
#         if(A[i]==num):
#             count=count+1
#     if(count>=1):
#         pos=A.index(num)
#         new_A=A[:pos]+A[pos+1:]
#         print(new_A)
#     else:
#         print("element not found in array")

# def Union_Function(setA,setB):
#     C=list({i:i for i in setA+setB}.values())
#     print("union set: ",C)

# def Intersection_Function(setA,setB):
#     C=[i for i in setA if i in setB]
#     print("Intersection set: ",C)

# def Difference_Function(setA,setB):
#     C=[element for element in setA if element not in setB]
#     print("Difference set:",C)

# def Contains_Element(A,num):
#     found=False
#     for i in range(len(A)):
#         if(A[i]==num):
#             found=True
#             break
#         else:
#             found=False
#     return found

# def Size_of_Set(A,B):
#     count=0
#     for i in range(len(A)):
#         count=count+1
#     return count

# def Subset_Function(A,B):
#     status=False
#     if(all(i in A for i in B)):
#         status=True
#     if(status):
#         print("\nYes,Subset exists")
#     else:
#         print("\nNo, Subset does not exist")

# A={}
# print("\nCreate set A")
# A=create_set()
# print("A= ",A)
# B={}
# print("\nCreate set B")
# B=create_set()
# while(True):
#     print("Main Menu")
#     print("1.Add an element to the set")
#     print("2.Remove an element from the set")
#     print("3.Membership of element")
#     print("4.Size of Set")
#     print("5.Union")
#     print("6.Intersection")
#     print("7.Difference")
#     print("8.Check Subset")
#     print("9.Exit")
#     print("Enter the choice")
#     choice=int(input())
#     if choice==1:
#         print("A= ",A)
#         print("Enter the element to be added in the set: ")
#         num=int(input())
#         Add_element(A,num)
#     elif choice==2:
#         print("A= ",A)
#         print("Enter the element to be removed in the set: ")
#         num=int(input())
#         print(A)
#         Remove_element(A,num)
#     elif choice==3:
#         print("A= ",A)
#         print("Enter the element to be searched in the set: ")
#         num=int(input())
#         if(Contains_Element(A,num)):
#             print("\nThe element is present in the set")
#         else:
#             print("\nthe element is not present in the set")
#     elif choice==4:
#         print("A= ",A)
#         print("\nThe size of the set is: ",Size_of_Set(A,B))
#     elif choice==5:
#         print("A= ",A)
#         print("B= ",B)
#         Union_Function(A,B)
#     elif choice==6:
#         print("A= ",A)
#         print("B= ",B)
#         Intersection_Function(A,B)
#     elif choice==7:
#         print("A= ",A)
#         print("B= ",B)
#         Difference_Function(A,B)
#     elif choice==8:
#         print("A= ",A)
#         print("B= ",B)
#         Subset_Function(A,B)
#     else:
#         print("Exiting")
#         break