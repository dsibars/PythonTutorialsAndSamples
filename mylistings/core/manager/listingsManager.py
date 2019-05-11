from mylistings.core.data.listingRepository import ListingRepository


class ListingsManager(object):

    def __init__(self, where):
        self.delimiter = '|'
        self.where = where
        self.namesListing = ListingRepository(where, '__internal__names', self.delimiter)
        self.listings = dict()
        self.reload()

    def reload(self):
        for name in self.namesListing.data:
            self.listings[name] = ListingRepository(self.where, name, self.delimiter)

    def get_listing(self, name):
        if name in self.namesListing.data:
            return self.listings[name]
        else:
            newlisting = ListingRepository(self.where, name, self.delimiter)
            self.namesListing.add(name)
            self.listings[name] = newlisting
            return newlisting

    def get_listing_data(self, name):
        return self.get_listing(name).data

    def add(self, name, value):
        self.get_listing(name).add(value)

    def get_names(self):
        return self.namesListing.data






