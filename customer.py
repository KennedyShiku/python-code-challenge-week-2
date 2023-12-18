from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)
    
    def get_given_name(self):
        return self._given_name
    
    def get_family_name(self):
        return self._family_name
    
    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    def restaurants(self):
        return list(set(review.restaurant() for review in Review.all_reviews if review.customer() == self))
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def all(cls):
        return cls.all_customers