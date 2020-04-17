def kids(chore_func):
    def kid_chore(*args, **kwargs):
        line = chore_func()
        return f"{line} by the kids"
    return kid_chore

def mom(chore_func):
    def mom_chore(*args, **kwargs):
        line = chore_func()
        return f"{line} by mom"
    return mom_chore

def dad(chore_func):
    def dad_chore(*args, **kwargs):
        line = chore_func()
        return f"{line} by dad"
    return dad_chore
@kids
def laundry():
    return "The dirty laundry was cleaned"
@mom
def garbage():
    return "The garbage was taken out"
@kids
def dust():
    return "The house was dusted"
@dad
def groom():
    return "The dog was brushed"

print(laundry())
print(garbage())
print(dust())
print(groom())
