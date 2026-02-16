# Stupid thing that probably doesn't work

# Might be useful get the commutator subgroup of a certain group
# of bijections between Z/nZ and Z/nZ

from math import gcd

n = 22
alist = []
for a in range(1, n):
    if gcd(a, n) != 1:
        continue
    for b in range(n):
        # This gets us f(x)
        a_inv = pow(a, -1, n)
        g = gcd(a, n)

        # AI solving ad + b \cong_n 0 for d (hopefully)
        a_reduced = a // g
        b_reduced = -b // g
        n_reduced = n // g
        d = (a_inv * b_reduced) % n_reduced 

        # Now we've created f. We need another function g
        for a1 in range(1, n):
            if gcd(a1, n) != 1:
                continue
            for b1 in range(n):
                a1_inv = pow(a1, -1, n)
                g1 = gcd(a1, n)

                # AI solving ad + b \cong_n 0 for d (hopefully)
                a1_reduced = a1 // g1
                b1_reduced = -b1 // g1
                n1_reduced = n // g1
                d1 = (a1_inv * b1_reduced) % n1_reduced 

                new_list = []
                for x in range(n):
                    new_list.append(((a * a1* a_inv * a1_inv * x) + (a * a1 * a_inv * d1) + (a * a1 * d) + (a * b1) + b) % n)
                alist.append(new_list)

seen = set()
unique_items = []

for item in alist:
    item_tuple = tuple(item)  # make it hashable
    if item_tuple not in seen:
        seen.add(item_tuple)
        unique_items.append(item)

print(unique_items)
print(len(unique_items))