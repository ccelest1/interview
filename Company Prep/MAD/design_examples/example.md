# Mastering Newsfeed System Design: Insider Strategies for Seamless Information Flow
- Newsfeed containing images, video, list of feed posts

## Functional Reqs
<Creator>
Creators can post story with images, videos, text

<User:Consumers>
- Users able to view list of posts matching user's tastes
- User able to follow/sub content creator
- User able to view latest posts when possible
- User able to interact (comment, like, etc)

<System>
- News feed gen'ed with posts from people who user followed/user might be interested in
- Post may have text, image, video
- Rearrange news feed when new posts come into news feed

## Non-Functional Reqs
1. New feed updates to happen in real time (1-2 sec latency)
2. Appending new post = > 5 sec to show in news feed request
3. Posts consistency
4. Seamless viewing through caching

## API Signatures (successful resp = 200, else 404)
1. POST /create/post, createPost(userId, files, metaData) => (returns) postId
2. GET /feed, getPosts(userId, page=1) => post<List>
    - Pagination can be 'offset based', 'cursor based' -> signature changes on what method is desired for getting next data @ list end
3. PUT /patch/user executeFollow(userid, follow user id) => response code, follow user id
4. GET /posts?variant=Its getStories(userId, page=1)
5. POST /create/comment, createComment(userId, postID, comment: String) => commentId

### High Level Design
![HL](./images/high_level.png)
- User - > API Gateway/LB (default)
- Add three different services corresponding to various endpoints described above
1. User Service
    * Includes User Cache (connected to service), User DB (SQL) connected to User Service
2. News Feed Service
    * Connected to News Feed DB (SQL) that is connected to Posts DB (SQL)
3. Upload Posts Service
`   * Pre-id (hash) generation service connected to Service, also connected to Posts DB that is paired to S3

### Low Level Design
![LL](./images/low_level.png)
* Includes multiple users as is realistic
* CDN points to the users (deal with load of distributed system)
* Before LB is connected to News Feed Service, Post Service, we have a Queue System (QS) preceding them that is connected to LB
    - QS -> News Feed Service (read heavy) + feed cache (redis) -> graph ql, newsfeed db (hadoop, spark)
    - QS -> Upload Posts Service (write heavy) -> Posts DB [connected to S3 and R1 - several data replications] + Pre-id (hash) gen service

* For User Service:
    * LB -> User Service, where the db is now connected to a S3 (Profile Object Storage)
    * User Cache (Redis)
