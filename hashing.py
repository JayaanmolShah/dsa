
telephonebook=[]
size=int(input("N : "))
for i in range(0,size):
    telephonebook.append(0)
print(telephonebook)
choice=input("1.Liner 2.Quadratic : ")
if choice=='1':
    for i in range (size):
        num=int(input("NUMBER : "))
        place=num%size
        if(telephonebook[place]==0):
            telephonebook[place]=num
        else:
            while(telephonebook[place]!=0):
                place=(place+1)%size
            telephonebook[place]=num
elif choice=='2':
    for i in range(size):
        num=int(input("NUMBER : "))
        place=num%size
        if(telephonebook[place]==0):
            telephonebook[place]=num
        elif(telephonebook[place]!=0):
            for i in range(1,10):
                place=(place+(i*i))%size
                if(telephonebook[place]==0):
                    telephonebook[place]=num
                    break
        else:
            print('non-valid')
print(telephonebook)
search=int(input("NUM : "))
if choice=='1':
    location=search%size
    # print(location)
    if telephonebook[location]==search:
        print(location)
    else:
        location=search%size
        while(telephonebook[location]!=search):
            location=(location+1)%size
        print(location)
elif choice=='2':
    location=search%size
    if telephonebook[location]==search:
        print(location)
    else:
        location=search%size
        while(telephonebook[location]!=search):
            for i in range (size):
                location=(location+i^2)%size
                if(telephonebook[location]==search):
                    print(location)

# SIZE = 100

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class HashTableC:
#     def __init__(self):
#         self.ht = [Node(-1) for _ in range(SIZE)]
        
#     def hashFunction(self, data):
#         return data % SIZE
    
#     def insert(self, data):
#         index = self.hashFunction(data)
#         if self.ht[index].data == -1:
#             print("No collision occurred while inserting")
#             self.ht[index].data = data
#         else:
#             print("Collision occurred while inserting!")
#             node = self.ht[index]
#             while node.next:
#                 node = node.next
#             node.next = Node(data)
            
#     def printHashTable(self):
#         for i in range(SIZE):
#             node = self.ht[i]
#             while node:
#                 print(node.data, end=" -> ")
#                 node = node.next
#             print("None")
    
#     def search(self, data):
#         index = self.hashFunction(data)
#         node = self.ht[index]
#         while node:
#             if node.data == data:
#                 print("Phone Number found in the directory!")
#                 return
#             node = node.next
#         print("Phone Number not present in the directory!")

# class HashTableLP:
#     def __init__(self):
#         self.ht = [-1] * SIZE
        
#     def hashFunction(self, data):
#         return data % SIZE
    
#     def insert(self, data):
#         index = self.hashFunction(data)
#         if self.ht[index] == -1:
#             print("No collision occurred while inserting")
#             self.ht[index] = data
#         else:
#             print("Collision occurred while inserting")
#             while True:
#                 index += 1
#                 if index == SIZE:
#                     index = 0
#                 if self.ht[index] == -1:
#                     self.ht[index] = data
#                     return
                    
#     def printHashTable(self):
#         for data in self.ht:
#             if data != -1:
#                 print(data)
    
#     def search(self, data):
#         index = self.hashFunction(data)
#         if self.ht[index] == data:
#             print("Phone Number found in the directory!")
#             return
#         temp = index
#         while True:
#             index += 1
#             if index == SIZE:
#                 index = 0
#             if index == temp:
#                 print("Phone Number not found in the directory!")
#                 break
#             if self.ht[index] == data:
#                 print("Phone Number found in the directory!")
#                 return

# method = int(input("Enter 1 for chaining method\nEnter 2 for linear probing method\n"))

# if method == 1:
#     ht = HashTableC()
# elif method == 2:
#     ht = HashTableLP()
# else:
#     print("Please enter a valid method!")

# while True:
#     choice = int(input("Enter 1 to insert a Phone Number in the directory\n"
#                        "Enter 2 to search a Phone Number in the directory\n"
#                        "Enter 3 to Print the directory\n"
#                        "Enter 4 to quit\n"))
#     if choice == 1:
#         n = int(input("Enter the count of Phone Numbers to be inserted: "))
#         for _ in range(n):
#             x = int(input("Enter the Phone Number to be inserted: "))
#             if len(str(x)) != 10:
#                 print("Please enter a valid number!")
#             else:
#                 ht.insert(x)
#     elif choice == 2:
#         x = int(input("Enter the Phone Number to be searched in the directory: "))
#         ht.search(x)
#     elif choice == 3:
#         ht.printHashTable()
#     elif choice == 4:
#         print("Thanks for trying out my code :)")
#         break
#     else:
#         print("Please Enter a valid choice!")










# class HashingDemo:
#     def __init__(self):
#         self.size=int(input("Enter the size of the hash table: "))
#         self.HashTable = list(0 for i in range(self.size))
#         self.num_of_elements=0
#         self.comparisons=0

#     def isTableFull(self):
#         if self.num_of_elements==self.size:
#             return True
#         else:
#             return False
        
#     def HashFun(self,element):
#         return element%self.size

#     def InsertElement_Linear(self,element):
#         if self.isTableFull():
#             print("Hash Table Full")
#             return False
#         OccupiedStatus=False
#         position= self.HashFun(element)
#         if self.HashTable[position]==0:
#             self.HashTable[position]=element
#             print("Telephone Number "+" at position "+str(position))
#             OccupiedStatus=True
#             self.num_of_elements +=1
#         else:
#             print("Collision has occured for Telephone number "+str(element)+"at index"+str(position))
#             position=self.LinearProbing(element,position)
#             self.HashTable[position]=element
#             OccupiedStatus=True
#             self.num_of_elements +=1
#         return OccupiedStatus

#     def LinearProbing(self,element,position):
#         while self.HashTable[position]!=0:
#             position +=1
#             if position >=self.size:
#                 position=0
#         return position

#     def InsertElement_Quadratic(self,element):
#         if self.isTableFull():
#             print("Hash Table Full")
#             return False
#         OccupiedStatus=False
#         position=self.HashFun(element)
#         if self.HashTable[position]==0:
#             self.HashTable[position]=element
#             print("Telephone Number "+str(element)+" at position "+str(position))
#             OccupiedStatus=True
#             self.num_of_elements += 1
#         else:
#             print("Collision has occured for Telephone number "+str(element)+" at index "+str(position))
#             OccupiedStatus, position=self.quadraticProbing(element,position)
#             if OccupiedStatus:
#                 self.HashTable[position]=element
#                 self.num_of_elements +=1
#             self.HashTable[position]=element
#             OccupiedStatus=True
#             self.num_of_elements +=1
#         return OccupiedStatus

#     def quadraticProbing(self,element,position):
#         Found =False
#         limit=50
#         i=1
#         while i<=limit:
#             newPosition=position + (i**2)
#             newPosition=newPosition%self.size
#             if self.HashTable[newPosition]==0:
#                 Found=True
#                 break
#             else:
#                 i +=1
#         return Found,newPosition
        
#     def search(self,element):
#         found=False
#         position=self.HashFun(element)
#         self.comparisons+=1
#         if(self.HashTable[position]==element):
#             return position
#             isFound=True
#         else:
#             temp=position-1
#             while position<self.size:
#                 if self.HashTable[position]!=element:
#                     position+=1
#                     self.comparisons +=1
#                 else:
#                     return position
#             position=temp
#             while position>=0:
#                 if self.HashTable[position]!=element:
#                     position-=1
#                     self.comparisons+=1
#                 else:
#                     return position
#         if not found:
#             print("element not found")
#             return False
        
#     def display(self):
#         print("\n")
#         print("--------------------------")
#         print("\nPosition\tTelephone Number\n")
#         print("--------------------------")
#         for i in range(self.size):
#             print("\t"+str(i)+"===>"+str(self.HashTable[i]))
            
# hash_object1=HashingDemo()
# print("\nInserting the telephone numbers in the Hash Table..\n")
# print("\nCollision Resolution using Linear Probing\n")
# hash_object1.InsertElement_Linear(1111111112)
# hash_object1.InsertElement_Linear(3333333331)
# hash_object1.InsertElement_Linear(4444444442)
# hash_object1.InsertElement_Linear(5555555552)
# hash_object1.InsertElement_Linear(6666666662)
# hash_object1.InsertElement_Linear(7777777772)
# hash_object1.InsertElement_Linear(8888888882)
# hash_object1.InsertElement_Linear(9999999992)
# hash_object1.display()
# print()
# print("The position of number 3333333331 is:"+str(hash_object1.search(3333333331)))
# print("The position of number 6666666662 is:"+str(hash_object1.search(6666666662)))
# print("The position of number 9999999992 is:"+str(hash_object1.search(9999999992)))
# print("\n--------------------------------------------------------------------------")
# print("\nTotal number of comparisons done for searching = "+str(hash_object1.comparisons))
# print("\n--------------------------------------------------------------------------")
# print("\n\n\n********************************************************************************\n")
# hash_object2=HashingDemo()
# print("\nInserting the telephone number in the hash table\n")
# print("\nCollision Resolution using Quadratic probing\n")
# hash_object2.InsertElement_Quadratic(1111111112)
# hash_object2.InsertElement_Quadratic(3333333331)
# hash_object2.InsertElement_Quadratic(4444444442)
# hash_object2.InsertElement_Quadratic(5555555552)
# hash_object2.InsertElement_Quadratic(6666666662)
# hash_object2.InsertElement_Quadratic(7777777772)
# hash_object2.InsertElement_Quadratic(8888888882)
# hash_object2.InsertElement_Quadratic(9999999992)

# hash_object2.display()
# print()
# print("The position of number 3333333331 is:"+str(hash_object2.search(3333333331)))
# print("The position of number 6666666662 is:"+str(hash_object2.search(6666666662)))
# print("The position of number 9999999992 is:"+str(hash_object2.search(9999999992)))
# print("\n--------------------------------------------------------------------------")
# print("\nTotal number of comparisons done for searching = "+str(hash_object2.comparisons))
# print("\n--------------------------------------------------------------------------")
# print("\n\n\n********************************************************************************\n")
