#from collections import defaultdict
#from typing import List
#from dataclasses import dataclass
#from dataclasses import field

#def fac():
    #return defaultdict(list)

#@dataclass
#class Test:
    #instances: defaultdict(list) = field(default_factory=fac) # works!

    #def add_instance(self, instance_type, instance_name):
        #self.instances[instance_type].append(instance_name)

#b = Test()

#b.add_instance('Location', 'Origin')
#b.add_instance('Location', 'Destination')
#b.add_instance('foo', 'bar')

#print(b.instances)

# ---------- decorator

def my_decorator(f):
    def wrapper(msg, **kwargs):
        f(msg, **kwargs)
    return wrapper

@my_decorator
def add_fluent(msg, release=[0,0]):
    print(msg)
    print(release[0])

@my_decorator
def add_fluent2(msg, release=[0,0], deadline=[0,0]):
    print(msg)
    print(release[0])

add_fluent('RobotAt', [1,1])
add_fluent2('RobotAt', release=[2,2], deadline=[3,3])
