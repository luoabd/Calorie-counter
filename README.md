# Calorie Counter

This is an implementation of a project idea by [@florinpop17](https://github.com/florinpop17) from his [App Ideas Collection Initiative](https://github.com/florinpop17/app-ideas).

**Tier:** 3-Advanced

Getting and staying healthy requires a combination of mental balance, 
exercise, and nutrition. The goal of the Calorie Counter app is to help the
user address nutritional needs by counting calories for various foods.

This app provides the number of calories based on the result of a user search
for a type of food. The U.S. Department of Agriculture MyPyramid Food Raw Data
will be searched to determine the calorie values.

## User Stories

-   [X] Developer will create a JSON file containing the food items to be
searched. This will be loaded when the app is started.
-   [X] User can see an panel containing a food description input text box, 
a 'Search' button, and a 'Clear' button.
-   [X] User can enter search terms into the food description input text box.
-   [X] User can click on the 'Search' button to search for the matching food.
-   [X] User can see a warning message if no search terms were entered.
-   [X] User can see a warning message if no matches were found.
-   [ ] User can see a list of the matching food items, portion sizes, and
calories in a scrollable results panel that is limited to 25 entries.
-   [X] User can click on the 'Clear' button to clear the search terms and 
results list. 

## Bonus features

-   [ ] User can see the count of the number of matching food items adjacent to
the results list.
-   [ ] User can use a wildcard character in search terms.
-   [ ] User can see more than 25 entries from a search by clicking a Down
icon button to add more matching food items to the search results list.
-   [ ] Developer will implement load the MyPyramid data into a database or a
data structure other than an array for faster searching. 

## Resources

[MyPyramid Food Raw Data](https://catalog.data.gov/dataset/mypyramid-food-raw-data)

