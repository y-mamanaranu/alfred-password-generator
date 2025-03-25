import random, string

def loader(pattern: str):
    _last = ""
    _flag = False
    for c in pattern:
        if c == "-":
            if _flag:
                raise ValueError("-- is not appropriate pattern")
            _flag = True
            pass
        else:
            _flag, flag = False, _flag
            _last, last = c, _last
            if flag:
                if last == "":
                    raise ValueError(f"-{c} is not appropriate pattern")
                if last in string.ascii_lowercase and c in string.ascii_lowercase:
                    i_s = string.ascii_lowercase.find(last)
                    i_e = string.ascii_lowercase.find(c)
                    if i_s > i_e:
                        raise ValueError(f"{last}-{c} is not appropriate pattern")
                    for _c in string.ascii_lowercase[i_s+1:i_e+1]:
                        yield _c
                elif last in string.ascii_uppercase:
                    i_s = string.ascii_uppercase.find(last)
                    i_e = string.ascii_uppercase.find(c)
                    if i_s > i_e:
                        raise ValueError(f"{last}-{c} is not appropriate pattern")
                    for _c in string.ascii_uppercase[i_s+1:i_e+1]:
                        yield _c
                elif last in string.digits:
                    i_s = string.digits.find(last)
                    i_e = string.digits.find(c)
                    if i_s > i_e:
                        raise ValueError(f"{last}-{c} is not appropriate pattern")
                    for _c in string.digits[i_s+1:i_e+1]:
                        yield _c
                elif last in "!@#^&*"  and c in "!@#^&*":
                    i_s = "!@#^&*".find(last)
                    i_e = "!@#^&*".find(c)
                    if i_s > i_e:
                        raise ValueError(f"{last}-{c} is not appropriate pattern")
                    for _c in "!@#^&*"[i_s+1:i_e+1]:
                        yield _c
                else:
                    raise ValueError(f"{last}-{c} is not appropriate pattern")
            else:
                yield c

def passgen(pattern: str, n: int):
    arr = list(loader(pattern))
    return ''.join(random.choices(arr, k=n))

def passgen_split(pattern: str, n: int, by: int):
    if n < by:
        raise ValueError(f"'n' must be larger than 'by': n={n}, by={by}")
    if n % by != 0:
        raise ValueError(f"'n' must be multiple of 'by': n={n}, by={by}")
    arr = list(loader(pattern))
    return "-".join([''.join(random.choices(arr, k=by)) for _ in range(n//by)])