from collections import defaultdict

instances = defaultdict(list)

instances['InsLocation'].append('roomA')
instances['InsLocation'].append('roomB')

print(instances)

for key, value in instances.items():
    print(key)
    print(value)
    print('---')
