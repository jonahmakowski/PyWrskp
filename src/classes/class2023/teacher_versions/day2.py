'''
name = input('what is your name? ')  # this information here is only for the reader


hello = 13
s=' hello'
print('hello', name," is your age ",13.5, True)
print(10, 12.5 )
a=10
v=12.5
h=False

j="john's house"
l='john said "goodbye" '
age = input (name,' what is your age')



a= 10+2
b= 10-2
c=10*2
d= 10/2
e =10+2.0


s= 'john'+'25'+'me'+str(10.5)

age = input(name+', what is your age? ')
age_int = int(age)
print(name,'in 2 years will be ',age_int+2)
print(name,'in 2 years will be ',int(age) +2)

print(name*13)

for  i in range(2,6):  #i =2,3,4,5
    print('i=',i)
    for j in range(4) : #j=0,1,2,3
        print('     j=',j, end='')
    print()


    for j in range(3): #j=0,j=1,j=2
        print(j,end='')

print()

*
* *
* * *
* * * *


star = ' *'
for line in range(1,4): #i= 1,2,3,4
    print(line, star)  


here is another homework challenge:

---- *
--- * *
-- * * *
- * * * *

you can uses the following two variables only once each in the program
space = "-"
star = " *"
I would also include the following variable

max_num_lines = 4  # if you change this number to let's saw 10 the program should print ten lines of stars




-----------------------------------------------------------------------------------------------------------------------------
I M P O R T A N T        I M P O R T A N T      I M P O R T A N T        I M P O R T A N T
There is further help down this page....  If you don't need it don't look down any further.
Infact you will find the answer to the fist homework challenge below
-----------------------------------------------------------------------------------------------------------------------------
    


















run the following lines ...........

--------------------------------------------
star = ' *'
for line in range(1,4): #i= 1,2,3,4
    print(line, star)  
---------------------------------------------

you should see this

1 *      <===== we want only 1  star on this line
2 *      <===== we want two stars on this line
3 *      <===== we want three stars on this line.
4 *

so ask your self  how many stars do we want on the first line:
what about the second line
..and the third and so on.

Im hoping that you will see the number of starts that you would like to print is EXTACTLY equal to the line variable.
  



so  we could try this following code
-----------------------------------------------------------
 
star = ' *'
for stars in range(1):
    print(star,end='')
print()

for stars in range(2):
    print(star,end='')
print()

for stars in range(3):
    print(star,end='')
print()


for stars in range(4):
    print(star,end='')
print()

---------------------------------------

so this works but my challenge was to ONLY use the print(star,end='') ONCE in the entire program.
Did you notice that in the program above the ONLY numberthat is different in each of the prints is the number that is in
the range() . It first is 1 then 2, 3 and 4
so we could exchange these numbers with avariable that starts at 1 and goes to 4.
we could do that with a for loop and avaialbe called line

like the following:

for line in range(1,5):  #line=1,2,3,4
    for stars in range(line):     # this is the same as above but we are using line instead of a literal number
        print(star,end='')
    print()

    









'''

  

    








