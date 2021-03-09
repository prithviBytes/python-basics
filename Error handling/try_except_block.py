try:
    foobar
except:
    print("Error")


def get_key(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get_key({'name': 'Prithvi'},'name')) # Prithvi
print(get_key({'name': "Prithvi"},'city')) # None