#!/usr/bin/env python3.6
# NOTE: requires python 3.6, you get a syntax error otherwise

from dataclasses import dataclass
from typing import List, Set
from dataclasses import field

@dataclass
class FluentArg:
    name: str = None
    type: str = None

@dataclass
class OperatorResource:
    name: str
    value: int

@dataclass
class DomainFluent:
    name: str
    args: List[FluentArg] = field(default_factory=list)
    #resources: 

    @classmethod
    def init_from_list(self, name, args):
        df = self(name)
        for arg in args:
            df.args.append(FluentArg(arg[0], arg[1]))
        return df

if __name__ == '__main__':
    my_fluent = DomainFluent.init_from_list('RobotAt', [['Origin','Location'], ['Destination','Location']])
    print('fluent name : {0}'.format(my_fluent.name))
    print('fluent args : {0}'.format(my_fluent.args))
