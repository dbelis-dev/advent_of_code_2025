

def read_ranges(filename):
    ranges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('-')
            if len(parts) != 2:
                continue
            try:
                a = int(parts[0])
                b = int(parts[1])
                ranges.append((a, b))
            except ValueError:
                continue
    return ranges

def find_first_in_ranges(ranges):
    extend = False
    for idx,ch in enumerate(ranges):
        start, end = ch
        print(f"Checking starting value {start}, finish value {end}, index {idx}")
        for r in ranges[idx+1:]:
            # print(f"   Checking range {r}")
            if start <= r[0] <= end:
                # print(f"      Start {r[0]} found within the range: {ch}")
                if r[1] >= end:
                    ranges[idx] = (ranges[idx][0], r[1])
                    # print(f"      Finish {r[1]} found bigger, extending range: {ranges[idx]}")
                    print(f"      extending range: {ranges[idx]}")
                print(f"      Removing range:  {r}")
                ranges.remove(r)
                extend = True
                # continue
            # elif start <= r[1] <= end:
            #     # print(f"      Finish {r[1]} found within the range: {ch}")
            #     if r[0] <= start:
            #         ranges[idx] = (r[0], ranges[idx][1])
            #         # print(f"      Start {r[0]} found smaller, extending range: {ranges[idx]}")
            #         print(f"      extending range: {ranges[idx]}")
            #     print(f"      Removing range:  {r}")
            #     ranges.remove(r)
            #     extend = True
                # continue
            else:
                # print(f"      No overlap with range: {r}")
                continue
    return ranges, extend

if __name__ == "__main__":
    ranges = read_ranges('day_5/input1.txt')
    print(f"Parsed ranges: {len(ranges)}")
    extend = True
    while extend:
        ranges, extend = find_first_in_ranges(list(sorted(ranges)))
        print(f"Parsed ranges: {len(ranges)}")
        print("---")
    
    print(f"Parsed ranges: {ranges}")
    
    sum = 0
    for r in ranges:
        start, end = r
        sum += end - start + 1
    print(f"Final sum: {sum}")

    sum = 0
    for r in ranges:
        sum += len(range(r[0], r[1]+1))
    print(f"Final sum: {sum}")

