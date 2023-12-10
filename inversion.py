from atcoder.fenwicktree import FenwickTree

# 転倒数
def inversion(arr):
    
    # 座圧
    def shrink(arr):
        shrinked_set = sorted(set(arr))
        shrinked_dict = {s: i for i, s in enumerate(shrinked_set)}
        
        shrinked = [shrinked_dict[a] for a in arr]
        return shrinked
    
    shrinked_arr = shrink(arr)
    MAX = max(shrinked_arr)
    bit = FenwickTree(MAX + 1)
    
    result = 0
    for a in shrinked_arr:
        # 「aより左にあるaより大きい数」の個数を足す
        result += bit.sum(0, MAX+1) - bit.sum(0, a+1)
        bit.add(a, 1)
    
    return result
