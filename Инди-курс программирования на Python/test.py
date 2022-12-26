from pprint import pprint

raw_dicts = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
             {"key2": "value2"}]

unique_dicts = [dict(s) for s in set(frozenset(d.items()) for d in raw_dicts)]

# frozenset(d.items()) for d in m - достаём  клюи/значения и кладём их в frozenset'ы(frozenset - поскольку нам нужны hashable тип данных)
# Чтоб исключить дубликаты и сложить их в set
# Из set'a собираем словари

print(unique_dicts)

pprint(list(frozenset(d.items()) for d in raw_dicts))
print('-'*10)
pprint(set(frozenset(d.items()) for d in raw_dicts))
