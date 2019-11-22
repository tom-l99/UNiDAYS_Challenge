class UnidaysChallenge():

    def __init__(self, rules):
        self.basket = {} # basket declared as dictionary to store quantities of items
        self.returnObj = {'total': 0, 'delivery': 0} # simple dictionary to store calculated total price and delivery values
        self.price = 0
        self.pricingRules = rules # take dictionary of pricing rules from main function

    def addItemToBasket(self, item):
        if item in self.basket:
            self.basket[item] += 1 # add another to item quantity if exists already
        else:
            self.basket[item] = 1 # set item quantity to 1 if not already in basket

    def calculateTotalCost(self):
        items = self.pricingRules
        
        """Loop through each item in basket, getting its respective price and, if applicable, discount rule(s)"""
        for item in self.basket.keys(): # for each item in list of dictionary keys
            amount = self.basket[item] # get quantity of each specific item in basket
            ruleSet = items[item]

            if 'discount' in ruleSet: # Only iterates if an item actually has a discount key
                discountRequirement = ruleSet['discount']['amount'] # take both numerical values stored for the discount rule
                noDiscount = amount % discountRequirement # remainder calculated to store how many items are ineligible for discount
                self.price += ruleSet['price'] * noDiscount

                discountAmount = (amount - noDiscount) / discountRequirement
                self.price += discountAmount * ruleSet['discount']['price']
            else:
              self.price += ruleSet['price'] * amount

        if self.price >= 50: # Calculate whether delivery charge is applicable
            self.returnObj['delivery'] = 0
        else:
            self.returnObj['delivery'] = 7

        self.returnObj['total'] = self.price # store calcualted total price in return object dictionary
        return self.returnObj
                              
if __name__ == '__main__':
    #3D dictionary to store ruleset, allowing expandability and additional rules to be added in future
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
    testCase.addItemToBasket('C')
    testCase.addItemToBasket('C')
    testCase.addItemToBasket('C')
    testCase.addItemToBasket('E')

    calculation = testCase.calculateTotalCost()
    totalCost = calculation['total']
    deliveryCost = calculation['delivery']
    overallCost = totalCost + deliveryCost

    print('Total price for items: £%.2f' % float(totalCost)) # Ensure the price is displayed as 2 decimal places

    if deliveryCost == 0:
        print('You have qualified for free delivery!')
    else:
        print('You have paid £%.2f for delivery' % float(deliveryCost))
        print('\nOverall price to pay: £%.2f' % float(overallCost))
