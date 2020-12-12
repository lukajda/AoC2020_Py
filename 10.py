input_list = [
54,
91,
137,
156,
31,
70,
143,
51,
50,
18,
1,
149,
129,
151,
95,
148,
41,
144,
7,
125,
155,
14,
114,
108,
57,
118,
147,
24,
25,
73,
26,
8,
115,
44,
12,
47,
106,
120,
132,
121,
35,
105,
60,
9,
6,
65,
111,
133,
38,
138,
101,
126,
39,
78,
92,
53,
119,
136,
154,
140,
52,
15,
90,
30,
40,
64,
67,
139,
76,
32,
98,
113,
80,
13,
104,
86,
27,
61,
157,
79,
122,
59,
150,
89,
158,
107,
77,
112,
5,
83,
58,
21,
2,
66]


il1 = [16,
10,
15,
5,
1,
11,
7,
19,
6,
12,
4]

il2 = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]


from typing import List


def advent_of_code_2020_10_1(il: List[int]) -> None:
    """"""
    sl = [0] + sorted(il)
    sl.append(sl[-1] + 3)
    incl = [0] * 3
    for i in range(len(sl) - 1):
        incl[sl[i+1] - sl[i] - 1] += 1
    print(incl[0] * incl[2])


# def recurs(sl: List[int], index: int, count: int) -> int:
#     """"""
#     for j in range(index + 1, min(index + 4, len(sl))):
#         if sl[j] - sl[index] <= 3:
#             if j == len(sl) - 1:
#                 count += 1
#             else:
#                 count = recurs(sl, j, count)
#         else:
#             break
#     return count
#
#
# def advent_of_code_2020_10_2(il: List[int]):
#     """"""
#     sl = [0] + sorted(il)
#     sl.append(sl[-1] + 3)
#     count = recurs(sl, 0, 0)
#     print(f'count: {count}')


def advent_of_code_2020_10_2(il: List[int]) -> None:
    """"""
    sl = [0] + sorted(il)               # sort input list and add 0 to beginning
    sl.append(sl[-1] + 3)               # add largest +3 to end
    cl = [0] * (sl[-1] + 1)             # prepare list of counters
    cl[0] = 1                           # set 1st counter list element to 1
    for i in sl:                        # for each element in input list
        for j in range(i + 1, i + 4):   # for next 3 elements in input list
            if j in sl:                 # if element in input list
                cl[j] += cl[i]          # add current element path count to +1/+2/+3 counter
    print(cl[sl[-1]])                   # print last counter


if __name__ == '__main__':
    advent_of_code_2020_10_1(il=input_list)
    advent_of_code_2020_10_2(il=input_list)
