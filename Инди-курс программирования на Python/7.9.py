nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}

def flatten_dict(d: dict) -> dict:
    res = {}
    for key, val in d.items():
        if isinstance(val, dict):
            for k, v in flatten_dict(val).items():
                res[f'{key}_{k}'] = v
        else:
            res[key] = val
    return res

print(flatten_dict(nested))