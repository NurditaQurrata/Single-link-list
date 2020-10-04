# Panah Satu
class Node :
    def __init__(self,initdata) :
        self.data = initdata
        self.next = None
    def getData(self) :
        return self.data
    def getNext(self) :
        return self.next
    def setData(self,newdata) :
        self.data = newdata
    def setNext(self,newnext) :
        self.next = newnext

class orderedlist :
    def __init__(self) :
        self.head = None
    def show (self) :
        current = self.head
        print("Head --->", end = " ")
        while current != None :
            current = current.getNext()
        print("None")
    def isEmpty (self) :
        return self.head == None
    def add(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found :
            #item taruk di depan current.getData
            if current.getData() > item :
                found = True
            else :
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None :
            temp.setNext(self.head)
            self.head = temp
        else :
            temp.setNext(current)
            previous.setNext(temp)
    def search (self,item) :
        current = self.head
        found = False
        while current != None and not found :
            if current.getData() == item :
                found = True
                print("Data in list")
            else :
                if current.getData() > item :
                    found = True
                else :
                    current = current.getNext()
        if found == False :
            print("Data not in list")
        return found
    def remove (self,item) :
        current = self.head
        previous = None
        found = False
        while current != None and not found :
            if current.getData() == item :
                found = True
                print("Data in list")
            else :
                previous = current
                current = current.getNext()
        if previous == None :
            self.head = current.getNext()
        else :
            if current != None :
                previous.setNext(current.getNext())
        if current == None :
            print("Data not in list")
# main program
linklist = orderedlist()
linklist.add(11)
linklist.add(44)
linklist.add(56)
linklist.add(100)
linklist.add(23)
linklist.add(20)
linklist.show()
linklist.search(120)
linklist.remove(102)
linklist.show()

