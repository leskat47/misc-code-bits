def get_Si(stocks):
    """ Take a series of n daily price quotes for a stock and we need to 
    calculate span of stock's price for all n days.
        >>> get_Si([100, 80, 60, 70, 60, 75, 85])
        [1, 1, 1, 2, 1, 4, 6]

    """

    Si = [1]

    for i in range(1, len(stocks)):
        print stocks[i]
        print stocks[0:i]
        Si.append(compare_stocks(stocks[i], stocks[0:i]))


    return Si


def compare_stocks(stock, stock_list):
    comp_stock = stock_list.pop()
    days = 1
    while comp_stock <= stock:
        days += 1
        comp_stock = stock_list.pop()
    return days


stocks = [100, 80, 60, 70, 60, 75, 85]

print get_Si(stocks)






