###------------- *args kullanımı ------------------
# input olarak *args alan fonksiyonlar default olarak tuple tutar


"""def s(nums):
    res = 0
    print(type(nums))
    print(nums)
    for e in nums:
        res += e
    return res

def sum(*numbers):
    res = 0
    print(type(numbers))
    print(numbers)    
    for e in numbers:
        res += e
    return res

nums = [1, 2, 3, 4]

print(sum(1,2,3,4))
print(s([1, 2, 3, 4]))
print(s(nums))
print(sum(nums))"""

###------------- kwargs kullanımı ------------------

# input olarak **kargs alan fonksiyonlar default olarak dictionary tutar

"""def foo(**kwargs):
    for v in kwargs.values():
        print(v)

def students(**stu):
    print(stu)
    for k in stu:
        print(k)

d = {"name":"Jake", "student_number":"471"}

foo(name="Jake", student_number="471")
students(name="Jake", student_number="471")"""


###-------- *args ve **kwargs birlikte kullanımı -------------

"""def weird(*args, **kwargs):
    res = 0
    for e in args:
        res += e

    for k, v in kwargs.items():
        print(k, ":", v)

    return res

#d = {"name":"Jake", "student_number":"471"}

weird(1, 2, 3, name="Jake", student_no="471")"""


###-------- * ile Unpacking kullanımı -------------

l = [1, 2, 3, 4]
m = [20, 21]

print(l)
print(*l)

merged_lm = [*l, *m]

print(merged_lm)
print(*merged_lm)

d1 = {"name":"Oğuz", "student_number":471}
d2 = {"name":"Gençer", "grade":3.06}

# Merge yaparken, aynı key değerleri için, son sırada yazılan dictionary'deki value esas alınır.
# name --> d1 içindeki value'ya eşit olacak
d1_merged = {**d2, **d1}
# name --> d2 içindeki value'ya eşit olacak
d2_merged = {**d1, **d2}

print(d1_merged)
print(d2_merged)


str_list1 = ["Hello world!"]
str_list2 = [*"Hello world!"]

print(str_list1)
print(*str_list1)
print(str_list2)
print(*str_list2)
