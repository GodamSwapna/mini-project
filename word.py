# file=open("userdetails.json","r") 
# f=file.read()
    
# print(f)
# r=5
# s=0
# while r>=1:
#     space=s
#     while space>0:
#         print(" ",end="")
#         space-=1
#     c=1
#     while c<=r:
#         print(c,end="")
#         c+=1
#     print()
#     r-=1
#     s+=1

# l=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# i=0
# list1=[]
# while i<len(l):
#     count1=l.count(l[i])
#     j=0
#     count2=0
#     while j<len(l):
#         if l[j]==l[i]:
#             count2+=1
#         j+=1
#     if count1==count2 and l[i] not in list1:
#         list1.append(l[i])
#         print("Last occurrence of ",l[i] ,"in the said list:",l.index(l[i]))
#     i+=1
name="swapna"
i=0
while i<len(name):
    
    if name[i]=="a" or name[i]=="s":
        continue
    i+=1
    print(name[i])
    # i+=1
