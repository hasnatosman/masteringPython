indian = ['samusa', 'daal', 'nan']
thai = ['chicken', 'fry', 'soup']
italian = ['pizza', 'burger', 'pasta']

dish = input("Enter a food: ")
if dish in indian:
    print("Indian food.")
elif dish in thai:
    print("Thai food.")
elif dish in italian:
    print("Italian food")
else:
    print("May be local food")