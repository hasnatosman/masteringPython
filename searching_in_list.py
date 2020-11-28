key_location = 'room'
locations = ['garden', 'office', 'toilet', 'kitchen', 'room', 'pool']

for location in locations:
    if location == key_location:
        print("Key is found in ", location)
        break
    else:
        print('Key is not found in ', location)