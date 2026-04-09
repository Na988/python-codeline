l = [1,2,3,4,5,6,7,8,9,10]
def get_count_to_infinity():
    i = 1
    while True:
        yield i
        i += 1
    
counter_gen = get_count_to_infinity()
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))