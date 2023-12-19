# Object Relations Code Challenge - Restaurants

## Domain Overview
In this assignment, we are working with a Yelp-style domain consisting of three models:
- `Restaurant`
- `Customer`
- `Review`

For our purposes:
- A `Restaurant` has many `Reviews`.
- A `Customer` has many `Reviews`.
- A `Review` belongs to a `Customer` and to a `Restaurant`.

The relationship between `Restaurant` and `Customer` is a many-to-many relationship.

**Note**: Before starting coding, draw your domain on paper or on a whiteboard, and identify a single source of truth for your data.

## Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- Lists and List Methods

## Instructions
1. Use the provided Pipfile [link](#) to install all dependencies required for this project.
2. Build out all the methods listed in the deliverables. The methods are listed in a suggested order, but you can tackle them in the order you find most convenient.
3. Create your own test sample instances to try/test your code in the console before submitting.
4. Prioritize writing error-free code over completing all deliverables. Focus on methods that work rather than writing more methods that don't.
5. Test your code in the console as you write.
6. Messy code that works is better than clean code that doesn't. Prioritize getting things working first, then refactor if time allows.
7. When encountering duplicated logic, extract it into shared helper methods.

## Before You Submit
- Save and run your code to verify that it works as expected.
- If some methods are not working, leave comments describing your progress.

**NB**: Sample Pipfile is provided for reference.

### Deliverables

#### Initializers, Readers, and Writers

##### Customer
- `Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington).
- `Customer given_name()`
  - Returns the customer's given name.
  - Should be able to change after the customer is created.
- `Customer family_name()`
  - Returns the customer's family name.
  - Should be able to change after the customer is created.
- `Customer full_name()`
  - Returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - Returns **all** customer instances.

##### Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string.
- `Restaurant name()`
  - Returns the restaurant's name.
  - Should not be able to change after the restaurant is created.

##### Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number).
- `Review rating()`
  - Returns the rating for a restaurant.
- `Review all()`
  - Returns all reviews.

#### Object Relationship Methods

##### Review
- `Review customer()`
  - Returns the customer object for that review.
  - Once a review is created, should not be able to change the customer.
- `Review restaurant()`
  - Returns the restaurant object for that given review.
  - Once a review is created, should not be able to change the restaurant.

##### Restaurant
- `Restaurant reviews()`
  - Returns a list of all reviews for that restaurant.
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.

##### Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed.
