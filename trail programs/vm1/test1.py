sp=-1
import hello
import dis 
stack_limit=1000
stack=[]
byte_code_length=0

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




import sys

orig_stdout = sys.stdout
f = file('byte_code.txt', 'w')
sys.stdout = f

print(dis.dis(hello.hello))
sys.stdout = orig_stdout
f.close()

'''with open('byte_code.txt') as f:
    lines = f.read().splitlines()

print("byte_code as list form")
print lines'''

with open('byte_code.txt') as f:
    lines=f.read().splitlines()
#print lines

i=0
byte_code=[]


while(i<len(lines)):
    list=lines[i].split()
    #while(5>len(list)):
    #list.insert(0,'0')
    byte_code.append(list)
    i=i+1


print("byte_code to list")
print byte_code

print('\n\n')
print("OUTPUT")






def load_global(item):
    #print item
    stack_push(item)

 
def load_const(item):
    if(item!='(None)'):
        stack_push(item)


def store_fast():
    print("store_fast")
    return


def printing():
    item=stack_pop()
    print(item)



############################################################################################################
#print(dis.dis(hello.hello))


constants=hello.hello.__code__.co_consts  #list for storing constants
local_variables=hello.hello.__code__.co_varnames #list for local variables
var_names=hello.hello.__code__.co_varnames #list for variable names

#print constants
#print local_variables
#print var_names

'



byte_code_length=0
while(byte_code_length<len(byte_code)-1):
    instruction=byte_code[byte_code_length]
    byte_code_length=byte_code_length+1
    if(len(instruction)==5):
        operator=instruction[2]
    else:
        operator=instruction[1]
    if(operator=='LOAD_GLOBAL'):
        if(len(instruction)==5):
            item=instruction[4]
            #print item
            load_global(item)
    elif(operator=='LOAD_CONST'):
        if(len(instruction)==4):
            item=instruction[3]
        load_const(item)
    elif(operator=='STORE_FAST'):
        store_fast()

    elif(operator=='PRINT_ITEM'):
        printing()
        

print("end of the program")

