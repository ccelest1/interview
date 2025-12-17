/*
You are working for a large retailer. We would like to determine what was the product which sold the most, and how many times it was sold.

Write a function that takes in a collection of product name strings representing purchases and returns the name of the product with the most purchases, and the total number of sales for that product. If multiple products sold the same amount, return the first to appear in the purchases list. Product names are case insensitive.

Example:
purchases1 = ["Television", "Laptop", "MacBook", "MacBook", "Nintendo Switch"]
findMostSold(purchases1) -> MacBook, 2

purchases2 = ["Blue Shirt", "Red Shirt", "blue pants", "blue shirt", "Red Shirt", "Red Shirt", "blue shirt", "Blue Shirt"]
purchases3 = ["Plushy", "Teddy Bear", "Doll", "Plushy", "Teddy Bear"]
purchases4 = ["Plushy", "Teddy Bear", "Doll", "Doll", "Plushy", "Teddy Bear"]
purchases5 = ["Teddy BeAr", "Plushy", "Doll", "Plushy", "Teddy Bear"]

All Test Cases:
findMostSold(purchases1) -> MacBook, 2
findMostSold(purchases2) -> Blue Shirt, 4
findMostSold(purchases3) -> Plushy, 2
findMostSold(purchases4) -> Plushy, 2
findMostSold(purchases5) -> Teddy Bear, 2

Complexity analysis variables:
P = Number of purchases
(Note: Individual purchase strings have constant length)
*/

/*
input -> list[str], str -> product purchased
output -> type string -> product with most purchases, #number of sales
function purpose ->
["Television", "Laptop", "MacBook", "MacBook", "Nintendo Switch"]
[L, M, M, N, T]
i
["Plushy", "Teddy Bear", "Doll", "Doll", "Plushy", "Teddy Bear"]
{
  P:2,
  T:2,
  D:2
}
return the first key-value pair if we encounter ties ->
(0) store the max_count = 0, max_purchase = null; ()
 (1) it should itearte
 through the list of strings
 (2)
 */
function findMostSold(purchases) {
    let map = {}

    purchases.forEach((element) => {
        let normalized = element.toLowerCase()
        map[normalized] = (map[normalized]||0) + 1
    })
    // happy path: we have only 1 max key
    // sad path: we have multiple keys with ties
    let max_value = Math.max(...Object.values(map))
    let max_arr = []
    Object.keys(map).forEach((key) => {
        // iterate through the keys in this dictionary, store a count of keys that match the max_value and if we only have a count = 1, then we can just return that kay else we have to just return the first instance that we encounter

        if (map[key] === max_value) {
            max_arr.push(key)
        }
    })
    return `${max_arr[0]} ${max_value}`
}

const purchases1 = ["Television", "Laptop", "MacBook", "MacBook", "Nintendo Switch"];
const purchases2 = ["Blue Shirt", "Red Shirt", "blue pants", "blue shirt", "Red Shirt", "Red Shirt", "blue shirt", "Blue Shirt"];
const purchases3 = ["Plushy", "Teddy Bear", "Doll", "Plushy", "Teddy Bear"];
const purchases4 = ["Plushy", "Teddy Bear", "Doll", "Doll", "Plushy", "Teddy Bear"];
const purchases5 = ["Teddy BeAr", "Plushy", "Doll", "Plushy", "Teddy Bear"];


let test_cases = []
test_cases.push(
    purchases1,
    purchases2,
    purchases3,
    purchases4,
    purchases5
)
test_cases.forEach(test_case => console.log(findMostSold(test_case)))
