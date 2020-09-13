def test_refs(gogu):
    gogu["l"] = "hobo"


_mapp = {
    1: "a",
    2: "b",
    "c": 3
}

print(_mapp)
test_refs(_mapp)
print(_mapp)




def test_refs_int(a):
    a = 99



b = 100
print(b)
test_refs_int(b)
print(b)


def test_refs_arr(arr):
    arr.append(99)

ax = [100]
print(ax)
test_refs_arr(ax)
print(ax)