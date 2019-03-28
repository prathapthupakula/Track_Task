# import numpy as np
# # l1=[[1,2,3],[4,5,6],[7,8,9]]
# # a1=np.array(l1)
# # n=a1[0].size
# # print(a1[0].size)
# # k=1
# # for i in range(0,n):
# #     for j in range(n,0,-1):
# #         if(j == n-k):
# #             print(a1[i][j] , end='')
# #     k+=1
# # exit()
# # print(a1)
# # print(type(a1))
# # exit()
# # l2=[(x,y) for (x,y),value in np.ndenumerate(a1)]
# # l3=[]
# # l4=[]
# # l5=[]
# # for (x,y),value in np.ndenumerate(a1):
# #     if value == 4 or value ==6:
# #         value=''
# #     if x==0:
# #         l3.append(value)
# #     elif x==1:
# #         l4.append(value)
# #     else:
# #         l5.append(value)
# # l6=[l3,l4,l5]
# # a2=np.array(l6)
# # print(l6)
# # print(a2)
#
# # print(l2)
# # print(a1[l2[0]],a1[l2[-1]])
# # l3=[a1[l2[0]],a1[l2[-1]]
# # print ("hello")
# list1=[1,2,3,4,5]
# print(list1[::-1])
#
# np.set_printoptions(suppress=True)
# import os
# path=os.path.abspath("C://Users//prathap_thupakula//Desktop//TerTest3.csv")
# print(path)
# exit()
#
# # print(path)
# # exit()
# # Import data from csv file url
# # C:\Users\prathap_thupakula\Desktop
# # path = 'C://Users//prathap_thupakula//Desktop//TerTest2.xls'
# data = np.genfromtxt(path, delimiter=',', skip_header=1,dtype='object')
# data1=data.tolist()
# print(type(data1))
# print(data1)
#
# # outtweets = [[tweet.text.encode("utf-8").decode("utf-8")] for tweet in data1]
# # print(outtweets)
# # exit()
# for i in data1:
#     for j in i:
#         print(j)
#         exit()
#     # pass
#     # mylist=[i.split(',')[0] for j in i]
#     # print(mylist)
#     # exit()
# exit()
# data[:3]  # see first 3 rows
# # en(a[1])
#
# a = np.array([[1,2,3],[4,5,6],[8,20,30]])
# max1=np.argmax(a)
# print(type(max1))
# for i in range(len(a[1])):
#     for j in range(len(a[1])):
#         print(a[i][j], end="")
# # d1=np.tile(a,10)
# # print(d1)
# # a.tolist()
# # print(a)
# # print(type(a))
#
# arr1d_obj = np.array([1, 'a'], dtype='object')
# print(type(arr1d_obj))
# arr1d_obj.tolist()
# print(type(arr1d_obj))
# int1=np.linspace(start=1, stop=50, num=10, dtype=int)
# print(int1)
# exit()
# # a.shape = (1,5)
# print (a)
#
# b=np.arange(10)
# print(b)
# # print(b.ndim)
# b.shape=(5,2)
# c=b.reshape(2,5)
# print(b)
# print(c)
# exit()
#
# arr = [[4, 5, 6],
#        [1, 2, 3],
#        [7, 8, 9]]
#
# n = len(arr[0])
# # print(n)
# i = 0
# # for j in range(0, n - 1):
# #     print(arr[i][j], end=" ")
# # for j in range(n,0,-1):
# #     print(j)
# #
# # exit()
# k = 1
# for i in range(0, n):
#     for j in range(n, 0, -1):
#         if (j == n - k):
#             # print(i,j)
#             print(arr[i][j], end=" ")
#             break;
#     k += 1
# exit()
# # Print last row
# i = n - 1;
# for j in range(0, n):
#     print(arr[i][j], end=" ")

# s1="July"
# print(s1[1:])
#
# data=[{'name': 'ALDER', 'operator': 523, 'offshore': True, 'id': 550}]
# print(data[0]['operator'])
# d1=dict

l1=["how", "are", "you", "prathap"]

# l3=[1,2,3,4,5]
# l4=[]
# for i in l3:
#     l4.append(i)
# print(l4)
# print(",".join(l1)+" Data.")

# l3=[{'name': 'ALISON', 'operator': 1, 'offshore': True, 'id': 1}, {'name': 'ALISON KX', 'operator': 2, 'offshore': True, 'id': 2}]
# for di in l3:
#     print(di['name'])
#     print(di['operator'])



# a="hai"
# b="hai"
# if a is not b:
#     print(True)
# else:
#     print(False)
l2=[10,15,16,18,19,29,30]
l1=[10,20,30,40]

n1=[]
n2=[]
n3=[]
filedList=[]
# row1=["Prathap","Roy","Ram","Hello"]
# row2=[{"name":"Prathap"},{"name":"Hello"},{"name":"Raj"}]
# for r1 in row1:
#     name=r1
#     for r2 in row2:
#         name1=r2['name']
#         # if name1 not in n3:
#         n3.append(name1)
#         if name is not name1:
#             n2.append(name)
# print(n3)
# print(set(n2)-set(n3))

# l1=["dataa"]
# print "dtataa",l1

# prime numbers between 1 to 100

# list3=[]
# for i in range(2,101):
#     isPrime=True
#     for j in range(2,i):
#         if i%j==0:
#             isPrime=False
#     if isPrime:
#         list3.append(i)
# print(list3)
# data='3,6'
# d1=data.replace(',','.')
# print(d1)
#
# st1="243"
# if "qh" not in st1 and "":
#     print("inside")
# else:
#     print("outside")

# l1=[{"id":23},{"id":24},{"id":23}]
# for i in l1:
#     print(i)

# l1=[{'GAS_DAY': '02/07/2019', 'FLOW': '-69515.138999999996', 'STOCK_LEVEL': '2532336.2519999999', 'OPERATOR': 'EDISON STOCCAGGIO'},
#     {'GAS_DAY': '02/07/2019', 'FLOW': '-69515.123', 'STOCK_LEVEL': '2532336.2519999999', 'OPERATOR': 'EDISON STOCCAGGIO'},
#     {'GAS_DAY': '02/08/2019', 'FLOW': '-69515.138999999996', 'STOCK_LEVEL': '2532336.2519999999', 'OPERATOR': 'EDISON STOCCAGGIO'}]
# l2=[]
# j=0
# for i in l1:
#     # print(i)
#     # print("GAS_DAY:"+i["GAS_DAY"])
#     print(l1[j]['GAS_DAY'])
#     # if "GAS_DAY:"+i["GAS_DAY"] in l1[j]:
#     #     print("data")
#         # print(j)
#     j+=1
    # if
    # if i["GAS_DAY"]:
    # if i["GAS_DAY"] not in l2:
    #     l2.append(i)
    #     if len(l2) !=0:
    #         if l2[j]["GAS_DAY"] == i["GAS_DAY"]:
    #             l2.remove(j)
    #     j +=1
        # if k["GAS_DAY"] and k["OPERATOR"] not in l2[i.k]:
        #     l2.append(i)
    # l2 +=i["GAS_DAY"]
# print(l2)
# s1="1234.3455"
# print(s1.isdigit())
a = [[1, 2, 3], [3, 6, 5], [7, 11, 2]]
b=[]
for i in a:
    print(i)
    c=sorted(i)
    print(c)
    b.append(c)
d=sorted(b)
print(d)

b=sorted([sorted(i) for i in a])
print(b)