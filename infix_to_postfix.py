# implementing stack on an array

def infixToPostfix(expression):
    stack= [] # build an empty stack
    output=[] # build an array to store the output

    dictionary= {'+': 1, '-': 1, '/': 2, '*': 2, '%':2} # create a dictionary where operators are keys and the order of their precedence is represented as values, meaning higher number has higher precedence per the later logic in the code 
    operators= set(dictionary.keys()) # take the keys in dictinoary and convert them into a set which is stored in the variable operators

    for item in expression.split(): # loop through every item in the expression and .split() here is used to allow for multi-digit numbers to be considered one item
        if item =="(": # if the item is opening bracket, it will be pushed into the stack
            stack.append(item)
        elif item== ")": # if the item is closing bracket, it will append what has been popped out of the stack to the output list
            while stack and stack [-1] != "(": # as long as stack is not empty, it will comntinue to pop the elements till it reaches the opening bracket
                output.append(stack.pop())
            stack.pop()
        elif item.isdigit(): # check if the item is a number
            output.append(item) # append it to output
        elif item in operators:
            while (stack and stack[-1] in operators and dictionary[item] <= dictionary[stack[-1]]): # as long as stack is not empty and the top of the stack is an operator and the operator we want to push has lower or equal precedence to the operator in the top of the stack, append what has been popped out of the stack to the output list
                output.append(stack.pop())
            stack.append(item)
    # the following 2 lines pop the remaining elements from the stack and append them into the output list
    while stack: 
        output.append(stack.pop())

    return ' '.join(output) # join all the elements in output into a single string but add space between the elements

# test run
stack = infixToPostfix("( 1 + 2 ) * 3")
print(stack)

# implementing stack on a linked list

class Node:
    # create a constructor that holds the value of the nodes and a referene to the next node
    def __init__(self, data):
        self.data= data
        self.next=None

class StackLinkedList:
    # create a constructor in which top is the last added node (the head of the linked list)
    def __init__(self):
        self.top =None

    # the push methods add a new node to the top of the stack
    def push(self,data):
        new_node= Node(data) # create a new node for the linked list
        new_node.next= self.top # point the new node to the current top tehn update top to the new node
        self.top= new_node

    # the pop method deleted the last node that has been pushed onto the stack
    def pop(self):
        if self.top is None:
            print("The linked list is empty.")
            return
        else:
            temp= self.top.data # take the value of the self.top and assign it to temp
            self.top= self.top.next # link the node after top.next to self.top so it becomes the "head" of the linked list
            return temp 
    # the peek method returns the last element that has been pushed onto the stack  
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    # this method is used in lieu of "while stack" to check if stack has elements or not
    def isEmpty(self):
        return self.top is None # so if it's empty, return that self.top is None
    
# the following function acts in the same manner as the infixToPostfix function in the array, the only difference here is that when dealing with a linked list, we use push instead of append (except for when we want to append to the list "output") and to check if there are elements in the list we use the method isEmpty and check the last element that has been pushed via the method peek
def infixToPostfix(expression):
    stack= StackLinkedList()
    output=[] 

    dictionary= {'+': 1, '-': 1, '/': 2, '*': 2, '%':2} 
    operators= set(dictionary.keys()) 
    for item in expression.split(): 
        if item =="(": 
            stack.push(item)
        elif item== ")": 
            while not stack.isEmpty() and stack.peek() != "(": 
                output.append(stack.pop())
        elif item.isdigit(): 
            output.append(item) 
        elif item in operators:
            while (not stack.isEmpty() and stack.peek() in operators and dictionary[item] <= dictionary[stack.peek()]): 
                output.append(stack.pop())
            stack.push(item)
    
    while not stack.isEmpty(): 
        output.append(stack.pop())
    return ' '.join(output)