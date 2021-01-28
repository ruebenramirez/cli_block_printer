def determin_low_and_high(input):
    low = high = None
    for num in input:
        if low is None or num < low:
            low = num
        if high is None or num > high:
            high = num
    # print(str(low) + " " + str(high))
    return low, high


def print_number_sizes(input):
    sizes = ['▃', '▄', '▅', '▆', '▇', '█']

    low, high = determin_low_and_high(input)
    for num in input:
        size = round(((num-1 * low) / high) * len(sizes))
        print(sizes[size], end=' ')


if __name__ == '__main__':
    line = list(map(int, input().split()))
    print_number_sizes(line)
