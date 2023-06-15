a = list(input())
numbers = ['0','1','2','3','4','5','6','7','8','9']
number_freaq = []
for i in numbers:
    number_freaq.append(a.count(i))
print(number_freaq.index(max(number_freaq)))
    