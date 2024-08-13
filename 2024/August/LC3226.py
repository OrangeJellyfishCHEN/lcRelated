def minChanges(n: int, k: int) -> int:
    if (n == k):
        return 0
    bin_n = bin(n).replace("0b", "")
    bin_k = bin(k).replace("0b", "")
    if len(bin_n) > len(bin_k):
        bin_k = "0" * (len(bin_n) - len(bin_k)) + bin_k
    else:
        bin_n = "0" * (len(bin_k) - len(bin_n)) + bin_n
    l = len(bin_n)
    res = 0
    for i in range(l):
        cur_n = bin_n[i]
        cur_k = bin_k[i]
        if cur_n != cur_k:
            if cur_n == "0":
                return -1
            res += 1
    return res


def minChanges_another_approach(n: int, k: int) -> int:
    if (n == k):
        return 0
    bin_n = bin_to_dec(n)
    bin_k = bin_to_dec(k)
    if len(bin_n) > len(bin_k):
        bin_k = "0" * (len(bin_n) - len(bin_k)) + bin_k
    else:
        bin_n = "0" * (len(bin_k) - len(bin_n)) + bin_n
    l = len(bin_n)
    res = 0
    for i in range(l):
        cur_n = bin_n[i]
        cur_k = bin_k[i]
        if cur_n != cur_k:
            if cur_n == "0":
                return -1
            res += 1
    return res


def bin_to_dec(num: int) -> str:
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res
