from line_profiler import LineProfiler

def expensive_op(n):
    return n * (999 * 1000) // 2

def slow_func(lst):
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result

def profile_main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")

if __name__ == "__main__":
    profiler = LineProfiler()
    profiler.add_function(expensive_op)
    profiler.enable()
    profile_main()
    profiler.disable()
    profiler.print_stats()