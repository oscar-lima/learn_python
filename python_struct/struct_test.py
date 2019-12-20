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

@dataclass
class Fluent:
    """
    Class used to store a fluent using python decorators.
    Example usage:
    # option 1
    my_fluent = Fluent('RobotAt', [['Origin','Location']]) # avoid!

    # option 2
    my_fluent = Fluent('RobotAt', [FluentArg('Origin','Location'), FluentArg('Destination','Location')])
    my_fluent = Fluent('RobotAt', [FluentArg('Origin','Location'), FluentArg('Destination','Location')], Time(4.5, 6.3))

    # option 3 (recommended)
    my_fluent = Fluent.from_list('RobotAt', [['Origin','Location'], ['Destination','Location']], [4.5, 6.7])

    # add fluents as a dictionary
    fluents = {}
    fluents[0] = my_fluent

    print('fluent name : {0}'.format(fluents[0].name))
    print('fluent args : {0}'.format(fluents[0].args))
    print('fluent release time : {0}'.format(fluents[0].release_time))
    """
    name: str = ''
    args: List[FluentArg] = field(default_factory=list)
    release_time: Time = Time()

    @classmethod
    def from_list(self, fluent_name, fluent_args, fluent_release_time=[0.0, 0.0]):
        f = self()
        f.name = fluent_name
        for arg in fluent_args:
            f.args.append(FluentArg(arg[0], arg[1]))
        f.release_time.lower_bound = fluent_release_time[0]
        f.release_time.upper_bound = fluent_release_time[1]
        return f

if __name__ == '__main__':
    my_fluent = Fluent.from_list('RobotAt', [['Origin','Location'], ['Destination','Location']], [4.5, 6.7])
    print('fluent name : {0}'.format(my_fluent.name))
    print('fluent args : {0}'.format(my_fluent.args))
    print('fluent release time lower bound : {0}'.format(my_fluent.release_time.lower_bound))
