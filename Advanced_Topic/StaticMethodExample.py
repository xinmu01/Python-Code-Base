class A():
    
    x = "hi" # x is the static attribute 

    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)    


print("The static variable in Class A is {}.".format(A.x))
a=A()
print("The static variable in Object A is {}.".format(a.x))

a.foo(1)
#A.foo(1); this is wrong!!

a.class_foo(2)
A.class_foo(3)

a.static_foo(4)
A.static_foo(5)

#Static Variable in Function
def static_var_1(): 
    static_var_1.a += 1
    print (static_var_1.a)

static_var_1.a =0
#Because we have function static_var_1, we can define var static_var_1.a.

static_var_1()
static_var_1()
static_var_1()

