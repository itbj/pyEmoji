for i in range(0x1f600,0x1f650):
    print(chr(i),end=" ")
    if i%16==15:
        print()

for i in range(0xe250,0xe350):
    print(chr(i),end=" ")
    if i%16==15:
        print()
