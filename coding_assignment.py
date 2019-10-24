#1. (A.)  請寫⼀一個程式把裡⾯面的字串串反過來來。
# (B.)  請寫⼀一個程式把裡⾯面的字串串，每個單字本⾝身做反轉，但是單字的順序不變。

def rev_str(s):
    s_split = s.split(" ")
    s_rev = []
    for string in s_split:
        s_rev.append(string[::-1])
    return print(s_rev)


rev_str('flipped class room is important')


#2. 請寫一個程式， Input 是一個數字， Output 是從 1 到這個數字，扣除掉所有 3 的倍數以及 5 的倍數，但是需要保留留同時是 3 和 5 的倍數的總數字數。
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
# 先選擇標籤為鉛筆或原子筆的袋子，若取出鉛筆，則標籤不為鉛筆的袋子內即為鉛筆；若取出原子筆，則標籤不為原子筆的袋子內即為原子筆。

# 4.
# 正常情況下，ABC三個人各出300元，套餐特價750元；不正常情況下，服務生拿走了60元，這60元應該要還給三個人
# 因此 810 - 60 = 750，此為實際上三人應付出的價格。
#
