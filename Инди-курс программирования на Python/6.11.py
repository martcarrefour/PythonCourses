words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']

print(len({word for word in words if len(word) > 6}))


my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'preference',
    'fascinate', 'earthflax', 'meadow', 'bitter', 'march', 'feel', 'wind', 'location',
    'need', 'adviser', 'error', 'pneumonia', 'concert', 'value', 'value', 'disclose',
    'glasses', 'tank', 'national', 'soup', 'feel', 'few', 'concert', 'wrestle',
    'proposal', 'soup', 'sail', 'brown', 'service', 'proposal', 'winter', 'jacket',
    'mention', 'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national', 'tradition',
    'government', 'mention', 'proposal', 'sunrise', 'refund', 'formulate', 'despise', 'hobby',
    'noble', 'parameter', 'update', 'serious', 'potential', 'entry', 'week',
    'tenant', 'debut', 'dentist', 'explode', 'default', 'slam'
}

#my_set.difference_update(('noble', 'offend', 'error', 'eagle', 'sail'))

# my_set.discard('noble')
# my_set.discard('offend')
# my_set.discard('error')
# my_set.discard('eagle')
# my_set.discard('sail')

[my_set.discard(i) for i in ('noble', 'offend', 'error', 'eagle', 'sail')]
print(my_set)


for i in range(int(input())):
    print(len(set(input().split())))
