def search(x: int, xs: [int], left_i: int = None, right_i: int = None) -> int:
    if left_i is None or right_i is None:
        return search(x, xs, 0, len(xs) - 1)
    if left_i == right_i:
        return xs[left_i] == x
    if left_i > right_i:
        return -1
    mid_i = (right_i + left_i) // 2
    if xs[mid_i] == x:
        return mid_i
    if xs[mid_i] > x:
        return search(x, xs, left_i, mid_i - 1)
    else:
        return search(x, xs, mid_i + 1, right_i)


if __name__ == '__main__':
    x = int(input())
    n = int(input())
    xs = [int(s) for s in input().split()]

    print(search(x, xs))

"""
[0, 1, 4, 6, 9]
0 4   >2
- 0 1   >0
  - 0 -1  >x
  - 1 1   >1
- 3 4   >3
  - 3 2   >x
  - 4 4   >4
"""
