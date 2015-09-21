import sys
import hello
import dis
 
stack_limit=1000
byte_code_length=0
sp=-1
store=False

const=[]
stack=[]

    
def stack_push(item):
    global sp
    global stack
    sp=sp+1
    #print sp
    if(sp==stack_limit-1):
        print("error stack is full")
    else:
        stack.append(item)
        #print stack


def stack_pop():
    global sp
    global stack
    if (sp==-1):
        print("error stack is empty")
    else:
        item=stack.pop()
        sp=sp-1
        return item

#print byte code of the hello.py to byte_code.txt

orig_stdout = sys.stdout
f = file('byte_code.txt', 'w')
sys.stdout = f

print(dis.dis(hello.hello))
sys.stdout = orig_stdout
f.close()
''' code for bytecode->a list called byte code and some formatting to the list'''
#convert each line to list named list
with open('byte_code.txt') as f:
    lines=f.read().splitlines()
#print lines

i=0
byte_code=[]

#convert single list to different lists

while(i<len(lines)):
    list=lines[i].split()
    byte_code.append(list)
    i=i+1

'''this is end of formatting of the byte_code list'''
#print("byte_code to list")
#print byte_code

print("OUTPUT")

def load_fast(item):
    stack_push(str(const[int(item)]))
   # print "\n inside load_fast"
   # print stack
    


def load_global(item):
   # print "\n inside load_global"
    stack_push(item)

 
def load_const(item):
    #print("\n inside load const")
    global store
    global const
    if(store):
        const.append(item)
    elif(item!='(None)'):
        stack_push(item)
    #print "printing const list"
    #print const


def store_fast():
    #print("inside store_fast")
    return
    


def printing():
    item=stack_pop()
    print(item)

def binary_add():
    #print"inside binaryb add"
    #num1=stack_pop()
    #print num1[1:-1]

    item=int(stack_pop()[1:-1])+int(stack_pop()[1:-1])
    #print "result"
    #print str(item)
    stack_push(str(item))
    return


def binary_sub():
    #print("binary_sub")
    item=int(stack_pop()[1:-1])-int(stack_pop()[1:-1])
    stack_push(str(item))

def binary_mul():
    item=int(stack_pop()[1:-1])*int(stack_pop()[1:-1])
    stack_push(str(item))

def binary_div():
    item2=int(stack_pop()[1:-1])
    item1=int(stack_pop()[1:-1])
    item=item1/item2
    stack_push(str(item))

'''
constants=hello.hello.__code__.co_consts  #list for storing constants
local_variables=hello.hello.__code__.co_varnames #list for local variables
var_names=hello.hello.__code__.co_varnames #list for variable names

print constants
print local_variables
print var_names'''

byte_code_length=0
while(byte_code_length<len(byte_code)-1):
    instruction=byte_code[byte_code_length]
    #print("instruction")
    #print instruction
    instruction_next=byte_code[byte_code_length+1]
    
    
    instruction_next=byte_code[byte_code_length+1]
    
    if(len(instruction)==5):
        operator=instruction[2]
    
    elif(len(instruction)==4):
        operator=instruction[1]

    elif(len(instruction)==2):
        operator=instruction[1]
    
    if(operator=='LOAD_GLOBAL'):
        if(len(instruction)==5):
            item=instruction[4]
            #print item+"hello error"
            load_global(item)
    
    elif(operator=='LOAD_CONST'):
        #print instruction_next[1]
        if(len(instruction)==4):
            item=instruction[3] #item is const to be stores
        elif(len(instruction)==5):
             item=instruction[4]
        if instruction_next[1]=='STORE_FAST':
            store=True
        load_const(item)
    
    elif(operator=='STORE_FAST'):
        store_fast()
    
    elif(operator=='BINARY_ADD'):
        binary_add()
    
    elif(operator=='BINARY_SUBTRACT'):
        binary_sub()
    elif(operator=='BINARY_MULTIPLY'):
        binary_mul()
    elif(operator=='BINARY_DIVIDE'):
        binary_div()
    
    elif(operator=='PRINT_ITEM'):
        printing()
    elif(operator=='LOAD_FAST'):
	if(len(instruction)==5):
		item=instruction[3]
		#print "ERROR"
		#print item
		load_fast(item)
	else:
		item=instruction[2]
		load_fast(item)
    
        
    byte_code_length=byte_code_length+1
        
#print const
#print("end of the program")

