from random import shuffle

def radix_sort(toSort):

    # we don't want to mutate the list, so we'll work with a copy
    new = toSort[:]

    # for every digit in the longest number of toSort..
    for exponent in range(len(str(max(toSort)))):
    
        index = (exponent + 1) * (- 1)
        buckets = [[] for i in range(10)]

        for number in new:
            # get the digit we're currently concerned with
            try:
                digit = int(str(number)[index])
            except IndexError:
                # IndexError means the digit isn't there so we set it to zero
                digit = 0

            # put that number into the bucket it belongs with
            buckets[digit].append(number)

        # 'render', or place the values in these buckets into new
        new = []
        for numeral in buckets:
            new.extend(numeral)

    return new

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 
                355, 689, 621, 183, 182, 524, 1]
                
shuffle(unsorted_list)

print(radix_sort(unsorted_list))
