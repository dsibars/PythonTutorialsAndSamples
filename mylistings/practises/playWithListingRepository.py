from mylistings.core.data.listingRepository import ListingRepository

baseDirectory = 'data'

myNamesListing = ListingRepository(baseDirectory, 'names')


print(myNamesListing.data)

myNamesListing.add('brandiluis')
myNamesListing.add('rodri')

print(myNamesListing.data)

myHeroesListing = ListingRepository(baseDirectory, 'heroes', '|')

print(myHeroesListing.data)
myHeroesListing.add('saitama')
myHeroesListing.add('goku')
print(myHeroesListing.data)
