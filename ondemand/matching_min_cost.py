"""
[Forests OA]
There are n products being sold on a shopping app. The price of the ith product is price[i]. The developers decided to give special gift cards to innovative customers. A gift card will be given if any customer buys a contiguous subsegment of products and at least 2 of the products have a matching price.
Find the minimum amount of money a customer needs to spend in order to get the gift card. If it is not possible for any customer to get a gift card, return -1.

Example:
price = [1, 2, 3, 1, 2, 1]

In the above example, the number of products n = 6. The subsegments where not all prices are distinct are (in increasing order of starting positions):

Subsegment	Remarks	Total Cost
[1, 2, 3, 1]	1 has a matching price	7
[1, 2, 3, 1, 2]	1 and 2 have a matching price	9
[1, 2, 3, 1, 2, 1]	1 and 2 have a matching price	10
[2, 3, 1, 2]	2 has a matching price	8
[3, 1, 2, 1]	1 has a matching price	7
[1, 2, 11	1 has a matching price	4
For all the other subsegments, all prices are distinct. The subsegment with the minimum price is from index 3 to 5 which costs 1 + 2 + 1 = 4. Return 4.

Parameters:
int price[n]: The prices of the products

Returns:
int: The minimum amount of money to be spent or -1

Constraints:

1 <= n <= 5 · 105
1 <= price[i] <= 106, 0 <= i <= n.
Other Cases:
Case 1:
price = [1, 2, 1, 2]
Output: 4
Explanation: The subsegments where not all prices are distinct are [1, 2, 1], [2, 1, 2] and [1, 2, 1, 2]. Of these, the minimum total price is 4.

Case 2:
price = [1, 100, 1, 7, 7]
Output: 14
Explanation: The subsegments where not all prices are distinct are: [1, 100, 1], [7, 7] and [1, 100, 1, 7, 7].
"""
def find_min_price(price):
    #* Prefix sum + Hashmap for leftmost position.
    lmost_positions = {} 
    best_costs = {}
    
    MAX = float('inf')
    best_cost = MAX
    prefix_sums = [0] * (len(price)+1)
    
    for i in range(len(price)):
        amount = price[i]
        prefix_sums[i+1] = prefix_sums[i] + amount
        if amount not in lmost_positions:
            best_costs[amount] = MAX
        else:
            #* Naive `sum(price[lmost_positions[cost]: i+1])` will cause TLE.
            new_cost = prefix_sums[i+1] - prefix_sums[lmost_positions[amount]]
            best_costs[amount] = min(best_costs[amount], new_cost)  
            best_cost = min(best_costs[amount], best_cost)
        lmost_positions[amount] = i
    
    return best_cost if best_cost < MAX else -1

