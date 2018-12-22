import random as rnd


# Âûïîëíÿåò áûñòðîå âîçâåäåíèå â ñòåïåíü exp
# ÷èñëà base ïî ìîäóëþ m
def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return (expmod(base, exp // 2, m)) ** 2 % m
    else:
        return (base * expmod(base, exp - 1, m)) % m


# Òåñò Ôåðìà íà ïðîñòîòó ÷èñëà n
def fermat_test(n):
    a = rnd.randint(2, n - 1)
    return expmod(a, n - 1, n) == 1


# Òåñò ÷èñëà n íà ïðîñòîòó
# Âûïîëíÿåò òåñò Ôåðìà äëÿ ÷èñëà n max_test ðàç
def is_prime(n, max_test):
    for test in range(max_test):
        if not fermat_test(n):
            return False
    return True


# Âîçâðàùàåò required ñàìûõ áîëüøèõ ïðîñòûõ ÷èñåë
# èç äèàïàçîíà (2, max_num);
# Ïî óìîë÷àíèþ required=-1 çíà÷èò, ÷òî âîçâðàùàþòñÿ
# âñå ïðîñòûå ÷èñëà èç äàííîãî äèàïàçîíà
def find_primes(max_num, max_test, required=-1):
    primes = []
    for num in range(max_num, 2, -1):
        if is_prime(num, max_test):
            primes.append(num)
        if required >= 0 and len(primes) >= required:
            break
    return primes