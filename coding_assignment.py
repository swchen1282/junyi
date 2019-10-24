#1. (A.)  請寫⼀一個程式把裡⾯面的字串串反過來來。
# (B.)  請寫⼀一個程式把裡⾯面的字串串，每個單字本⾝身做反轉，但是單字的順序不變。

def rev_str(s):
    s_rev = s[::-1]
    return print(s_rev)


rev_str('flipped class room is important')


#2. 請寫⼀一個程式， Input  是⼀一個數字， Output  是從  1  到這個數字，扣除掉所有  3  的倍數以及  5  的倍數，但是需要保留留同時是  3  和  5  的倍數的總數字數。
def fun2(int):
    seq = list(range(1, int + 1))
    new_seq = []
    for num in seq:
        new_seq.append(num)
        if num % 15 == 0:
            pass
        elif num % 3 == 0:
            new_seq.remove(num)
        elif num % 5 == 0:
            new_seq.remove(num)
    return print(len(new_seq))


# fun2(15)

# 3.
list = ('pensil', 'pen', 'pensil + pen')

# 4.
order = 900
real_back = 750
fake_back = 90

