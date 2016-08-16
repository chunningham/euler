facts1 = filter(lambda x: x%5==0 or x%3==0, range(0, 1000) )
facts2 = [x for x in range(0, 1000) if x%5==0 or x%3==0]
print(sum(facts1))