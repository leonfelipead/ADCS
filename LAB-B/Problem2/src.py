from random import randint

def commonMembers_h(a, b, acc):
	if not a or not b:
		return acc
	if a[0] == b[0]:
		idx = 0
		acc.append(a[0])
		while(len(a) > idx and a[idx] == b[0]):
			idx = idx + 1
		return commonMembers_h(a[idx:],b[1:],acc)
	elif a[0] < b[0]:
		return commonMembers_h(a[1:], b, acc)
	else:
		return commonMembers_h(a, b[1:], acc)
		
def commonMembers(a,b):
	a.sort()
	b.sort()
	return commonMembers_h(a, b, [])
	
def commonMembersOneLiner(a,b):
	return list(set(a).intersection(b))
	
def createLists(listA,listB,listCommon):
	for n in range(randint(5,10)):
		num = randint(0,10)
		listA.append(num)
		listB.append(num)
		listCommon.append(num)
	for n in range(randint(0,4)):
		num = randint(1,5)
		listA.append(num)
		num = randint(6,10)
		listB.append(num)
	listA.sort()
	listB.sort()
	listCommon = list(set(listCommon))
	listCommon.sort()
	return listA, listB, listCommon

