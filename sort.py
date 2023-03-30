# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
cnt = 0
def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)

def around(v, w):
	dl = []
	idx = 0
	dl.append(v[w])
	for i in range(w):
		if i == w:
			break
		dl.append(v[i])

	return dl

input_line = input()
l1 = input()
l2 = input()

out = "No"
v = l2
datalen = int(input_line) - 1
for i in range(int(input_line)):
	v = around(v, datalen)
	work=''.join(v)
	if l1 == work:
		out = "Yes"
		break

print(out)