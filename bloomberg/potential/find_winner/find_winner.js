/*

        There are n friends that are playing a game
        Friends sit in circle numbered from 1 to n in clockwise order
        Moving clockwise from ith friend brings you to (i+1th) friend for 1<= i < n and moving clockwise from nth friend brings you to 1st friend

        Rules:
         1. start at 1st friend
         2. count next k friends in clockwise direction including friend I started @ -> counting wraps around circle and may include fiends more than once
         3. last friend counted leaves circle and loses game
         4. if there is more than 1 friend in circle, go to step 2 starting from friend immediately clockwise or friend who just lost and repeat
         5. else, lsat friend in circle wins game

         Given number of friends `n` and integer `k` return winner of game
         k%n -> remainder of spots
         if given n friends, we know that at max we are limited by n in terms of positions, if we have 5 friends and 4 turns -> 4, if we have 5 friends and 6 turns, return 1
         index = k%n, helper function taking in array of remaining friends and decrementing number of turns
 */

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function (n, k) {
    let friends = []
    for (let i = 1; i < n + 1; i++) {
        friends.push(i)
    }

    const elimination = (arr, elimination_index, k, n) => {
        // if not friends, exit as we need to return a remaining friend
        // base case, if we get to one friend we want to return that index
        // algo - eliminate friend on specified turn
        // return elimination(sliced_arr, n-1)
        if (arr.length === 0) {
            return null
        }
        if (arr.length === 1) {
            return
        }
        // 2 -> (1+0)%5 -> 1
        elimination_index = ((k - 1) + elimination_index) % arr.length;
        arr.splice(elimination_index, 1)
        elimination(arr, elimination_index, k, n)

    }
    elimination(friends, 0, k, n)
    return friends[0]
};

console.log(findTheWinner(
    5, 2
))
console.log(findTheWinner(
    6, 5
))
