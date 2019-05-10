from mylistings.core.service.listingsManager import ListingsManager

baseDirectory = 'data2'

manager = ListingsManager(baseDirectory)

print(manager.get_names())

print(manager.get_listing_data('things'))

manager.add('things', 'potatoe')

manager.add('things', 'calçot')

manager.add('languages', 'japanese')

print(manager.get_listing_data('things'))
print(manager.get_listing_data('languages'))

print(manager.get_names())
