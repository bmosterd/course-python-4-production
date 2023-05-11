def even_nr():
    num = 0
    while True:
        yield num
        num += 2

even_gen = even_nr()

total_count = 0
for _ in range(5):
    total_count += next(even_gen)
print(total_count)
