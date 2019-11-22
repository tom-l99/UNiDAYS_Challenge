class UnidaysChallenge():

    def __init__(self, rules):
        self.basket = {} # basket declared as dictionary to store quantities of items
        self.returnObj = {'total': 0, 'delivery': 0}
        self.pricingRules = rules # take dictionary of pricing rules from main function
        self.price = 0

    def addItemToBasket(self, item):
        if item in self.basket:
            self.basket[item] += 1 # add another to item quantity if exists already
        else:
            self.basket[item] = 1 # set item quantity to 1 if not already in basket

    def calculateTotalCost(self):
        items = self.pricingRules
        total = 0
        
        """Loop through each item in basket, getting its respective price and, if applicable, discount rule(s)"""
        for item in self.basket.keys(): # for each item in list of dictionary keys
            amount = self.basket[item]
            ruleSet = items[item]

            if 'discount' in ruleSet:
                discountRequirement = ruleSet['discount']['amount']
                noDiscount = amount % discountRequirement
                self.price += ruleSet['price'] * noDiscount

                discountAmount = (amount - noDiscount) / discountRequirement
                self.price += discountAmount * ruleSet['discount']['price']
            else:
              self.price += ruleSet['price'] * amount

        self.returnObj['total'] = self.price
        if self.price >= 50:
            self.returnObj['delivery'] = 0
        else:
            self.returnObj['delivery'] = 7

        return self.returnObj
                              
if __name__ == '__main__':
    #3D dictionary to store ruleset, allowing expandability 
    rules = {
            'A': {'price': 8},
            'B': {'price': 12, 'discount': {'amount': 2, 'price': 20}},
            'C': {'price': 4, 'discount': {'amount': 3, 'price': 10}},
            'D': {'price': 7, 'discount': {'amount': 2, 'price': 7}},
            'E': {'price': 5, 'discount': {'amount': 3, 'price': 10}}}

    testCase = UnidaysChallenge(rules)
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('B')
    testCase.addItemToBasket('C')


    totalCost, deliveryCost = testCase.calculateTotalCost()
    overallTotal = totalCost + deliveryCost

    print('\nTotal cost to pay: £%' % float(totalCost)) # Ensure the price is displayed as 2 decimal places

    if deliveryCost == 0:
        print("You have qualified for free delivery!")
    else:
        print('You have paid £%.2f for delivery' % float(deliveryCost))
