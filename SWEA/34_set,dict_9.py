beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer_ex = {}
for name in beer.keys():
    beer_ex[name] = beer[name] * 1.05
print(beer)
print(beer_ex)