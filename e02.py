# vscode+git test.
# 2022-09-18
for i in range(0x1f30d,0x1f311):
    print(chr(i),end=" ")
    if i%16==15:
        print()

# https://unicode.org/Public/emoji/14.0/emoji-test.txt
# subgroup: place-map
u=[0x1f5fa,0x1f5fa,0x1f5f3,0x1f9ed]
for i in u:
    print(chr(i),end=" ")
    if i%16==15:
        print()

# subgroup: transport-ground
print ()
for i in range(0x1f682,0x1f69d):
    print(chr(i),end=" ")
    if i%16==15:
        print()

i=0x1f981
print()
print(chr(i),end=" ")

# 新冠病毒 Coronavirus
# https://unicode-table.com/cn/sets/coronavirus/
u=[0x1f9a0,0x1f451,0x1f912,0x1f637,0x1f915,0x1f927,0x1f92e,
   0x1f9fc,0x1f590,0x1f44f,0x1f932,0x1f6b0,0x1f4a6,0x1f9f3,
   0x1f489,0x1f48a,0x1f691,0x1f9fb,0x1f3e5,0x2623
]
print()
for i in u:
    print(chr(i),end=" ")
    if i%16==15:
        print()

#Mahjong Tiles
# https://unicode-table.com/en/blocks/mahjong-tiles/
print ()
for i in range(0x1f000,0x1f030):
    print(chr(i),end=" ")
    if i%16==15:
        print()
#
# 💲$ 0x1F4B2
#