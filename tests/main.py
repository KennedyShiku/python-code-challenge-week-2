import pytest
from customer import Customer
from restaurant import Restaurant
from review import Review

def test_customer_methods():
    customer = Customer("John", "Doe")

    assert customer.given_name() == "John"
    assert customer.family_name() == "Doe"
    assert customer.full_name() == "John Doe"

def test_restaurant_methods():
    restaurant = Restaurant("Best Bites")

    assert restaurant.name() == "Best Bites"

def test_review_methods():
    customer = Customer("Alice", "Johnson")
    restaurant = Restaurant("Tasty Grill")
    review = Review(customer, restaurant, 4)

    assert review.rating() == 4

def test_object_relationship_methods():
    customer = Customer("Bob", "Smith")
    restaurant = Restaurant("Delicious Deli")
    review = Review(customer, restaurant, 5)

    assert review.customer() == customer
    assert review.restaurant() == restaurant
    assert restaurant.reviews() == [review]
    assert restaurant.customers() == [customer]
    assert customer.restaurants() == [restaurant]

def test_aggregate_association_methods():
    customer = Customer("Eve", "Miller")
    restaurant = Restaurant("Yum Yum Burgers")
    review1 = Review(customer, restaurant, 3)
    review2 = Review(customer, restaurant, 4)

    assert customer.num_reviews() == 2
    assert Customer.find_by_name("Eve Miller") == customer
    assert Customer.find_all_by_given_name("Eve") == [customer]
    assert restaurant.average_star_rating() == 3.5

if __name__ == "__main__":
    pytest.main()
