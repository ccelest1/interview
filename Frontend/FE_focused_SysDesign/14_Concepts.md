# [ 14 Front End System Design Concepts Explained in 10 Minutes ](https://www.youtube.com/watch?v=YO7R0rYWDl8)


## State Management
- Reduce number of requests by caching data on client side
    * Traditional: Client performs several repetitive calls that can be saved using state management layer like React, Axios
* New paradigm using a caching strategy
    - Interceptor in between client and server, attach jwt token
    - Every server response gets intercepted to have data stored in cache
    - Delete options can modify info stored in cache
* Keep data up to date using expiry policy

## API Caching w/ Expiration
- `useQuery` from `react-query` to make api calls, consume data nd render on application
    * allows for user of `staleTime` in order to expire information for renewal of currently stored data

## GraphQL = Mitigate Over Fetching
- Specify properties using graphql that are as needed and none that we don't
- Apollo client supports caching techniques as well

## Rate Limiting and Debouncing
- Reduce number of calls from client to server -> RL = debouncing/throttling
- Debounce i.e in searching of search Terms -> wait certain period after user stops typing to execute search

## Cursor v Offset Pagination
- Offset pagination: page size, number of elements -> use sql for offset required
- Cursor -> next 10 items using sequential timestamp/id that corresponds to given items
