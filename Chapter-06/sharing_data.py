from multiprocessing import Array, Process, Value


def increment_value(shared_int: Value):
    shared_int.value += 1


def increment_array(shared_array: Array):
    for index in range(len(shared_array)):
        shared_array[index] += 1


if __name__ == "__main__":
    integer = Value("i", 0)
    integer_array = Array("i", [0, 0])

    procs = [
        Process(target=increment_value, args=(integer,)),
        Process(target=increment_array, args=(integer_array,)),
    ]

    [p.start() for p in procs]
    [p.join() for p in procs]

    print(integer.value)
    print(integer_array[:])
