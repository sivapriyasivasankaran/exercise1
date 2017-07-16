months=['jan','feb','mar','apr']
months.append('may')
months.append('july')
print "adding may and july",months
months.insert(5,'june')
print "printing the current list",months
print "print index of may is",months.index('may')
months.remove('june')
print "june is removed.the new list is",months
