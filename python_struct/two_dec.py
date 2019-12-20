#!/usr/bin/env python3.6
# NOTE: requires python 3.6, you get a syntax error otherwise

from dataclasses import dataclass
from typing import List
from dataclasses import field

@dataclass
class Time:
    lower_bound: float = 0.0
    upper_bound: float = 0.0

@dataclass
class FluentArg:
    name: str = None
    type: str = None

# @args_sanity_check (definition)
def args_sanity_check(f):
    """
    decorator to ensure that function input data is in the correct format (type and size)
    NOTE: this decorator works for class methods only, c -> class (self)
    """
    def check_time_interval(time_interval_as_list, name):
        assert(isinstance(time_interval_as_list, list)), '{0} must be a list of 2 elements containing lower and upper bound'.format(name)
        assert(len(time_interval_as_list) == 2), '{0} must be a list of 2 elements containing lower and upper bound'.format(name)
        assert(isinstance(time_interval_as_list[0], (int, float))), '{0} lower bound must be an int or float'.format(name)
        assert(isinstance(time_interval_as_list[1], (int, float))), '{0} upper bound must be an int or float'.format(name)
        assert(time_interval_as_list[0] <= time_interval_as_list[1]), '{0} upper bound must be greater than {0} lower bound'.format(name)

    def function(self, name, args, **kwargs):
        #assert(isinstance(c, class)), 'c must be a class'
        assert(isinstance(name, str)), 'name must be a string'
        assert(isinstance(args, list)), "args must be a list of lists, e.g. [['Origin','Location'],['Destination','Location']]"
        for arg in args:
            assert(isinstance(arg, list)), "args must be a list of lists, e.g. [['Origin','Location'],['Destination','Location']]"
            assert(len(arg) == 2), "Length of arg must be 2"
            assert(isinstance(arg[0], str)), "arg[0] must be a string"
            assert(isinstance(arg[1], str)), "arg[1] must be a string"
        if 'release' in kwargs:
            check_time_interval(kwargs['release'], 'release')
        if 'deadline' in kwargs:
            check_time_interval(kwargs['deadline'], 'deadline')
        if 'constraint' in kwargs:
            assert(isinstance(kwargs['constraint'], str)), 'constraint must be a string'
        if 'negative' in kwargs:
            assert(isinstance(kwargs['is_negative'], bool)), 'is_negative must be a boolean'
        f(self, name, args, **kwargs)
    return function

@dataclass
class Fluent:
    name: str = ''
    args: List[FluentArg] = field(default_factory=list)
    release_time: Time = Time()

    @classmethod
    def from_list(self, fluent_name, fluent_args, release=[0.0,0.0]):
        self.check_args(self, fluent_name, fluent_args, release=release)
        f = self()
        f.name = fluent_name
        for arg in fluent_args:
            f.args.append(FluentArg(arg[0], arg[1]))
        f.release_time.lower_bound = release[0]
        f.release_time.upper_bound = release[1]
        return f

    @args_sanity_check
    def check_args(self, name, args, release=[0,0]):
        pass

if __name__ == '__main__':
    my_fluent = Fluent.from_list('RobotAt', [['Origin','Location'], ['Destination','Location']], release=[4.5, 6.7])
    print('fluent name : {0}'.format(my_fluent.name))
    print('fluent args : {0}'.format(my_fluent.args))
    print('fluent release time lower bound : {0}'.format(my_fluent.release_time.lower_bound))
