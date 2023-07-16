from __future__ import print_function
import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """
    bestShop = None
    minCost = float('inf')  # Initialize with a high cost

    for fruitShop in fruitShops:
        totalCost = fruitShop.getPriceOfOrder(orderList)

        if totalCost is not None and totalCost < minCost:
            minCost = totalCost
            bestShop = fruitShop

    return bestShop


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders", orders, "the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders:", orders, "the best shop is", shopSmart(orders, shops).getName())
