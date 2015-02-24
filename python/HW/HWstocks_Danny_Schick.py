# CS 21 HW
# Danny Schick
# Exercise 12 | Stock Transaction

##### DEFINING INITIAL VARIABLES #####
sharesNum = 2000
initPrice = 40
ComRate = .03 # Commission rate in %

### CALCULATING INITIAL BUY PRICES #####
stockCost = sharesNum * initPrice
initBroker = ComRate * stockCost

##### TWO WEEKS LATER ######
sellPrice = 42.75
stockSell = sharesNum * sellPrice
sellBroker = ComRate * stockSell

totalBroker = initBroker + sellBroker
profit = stockSell - stockCost - totalBroker
#### PRINTING ANSWERS ######
print("Joe paid", stockCost, "dollars for 2000 shares")
print("Joe paid his stockbroker", initBroker, "dollars initially" )
print("After two weeks, Joe sold his shares for ", stockSell, "dollars.")
print("He paid his broker ", sellBroker, "dollars for the liquidation")
print("He made", profit, "dollars overall.")

