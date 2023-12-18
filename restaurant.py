from review import Review

class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name
    
    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant() == self]
    
    def customers(self):
        return list(set(review.customer() for review in self.reviews()))