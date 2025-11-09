# [ How to Design a Typeahead Component ](https://www.youtube.com/watch?v=Sky0Ln0hrZs)

## Clarification
- Scale of application -> millions or only some hundreds
- Supported devices (mobile, desktop)
- Where is data stored
    * Remote (api to fetch or local)
- Do I need personalization of search result?
- Do we need to return data in paginated result?
    * Top `x` items
- Do we need to handle, errors, status?
    * skeleton for loading data
- If offline system?
- Is it just text for each search element or do we need icons?
- Keyboard Navigation?

## Component Structure
- Require list of results, button, search input box
    * Simple at first then expand when narrowing down details
- When loading show indicator
- Error message that shows exclamation symbol
- onClick event
- ask about desired keyboard nav and accessibility

## Details
- Dealing with list
    * for items in list, we need an id for each item, label demonstrate results, url that is optimal string
    * image with certain results
- Trending section
    * Has own list with recents, personalized results
- Fixed list
    * Group that is a string, items in group
- PageInfo (object)
    * pagenumber, pageSite, hasNext (bool)

## API Design
- Restful: `/api/search?query`allowing for get request -> url encoded query
    * receive back response containing status, message
- Graphql
    * searchQuery that involves str `keyword`
    * involves pageSize, pageNumber
    * edges -> nodes containing id, text, image
    * pageinfo -> cursor, hasNext
- Pros, Cons
    * Flexibility
    * Extending the API (websockets - rt notis for backend)

## Optimization Strategies
- Performance
    * Cache
        - frontend
        - gateway
        - backend
            * algorithm + expiry
    * Network (race condition)
        - cancel req
        - relay
    * Debounce/throttling
- Security
- Accessibility
    - testing access.
- Offline
- Error handling
- Internalization
