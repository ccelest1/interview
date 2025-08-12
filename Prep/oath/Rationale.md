# Main Prep
1. Overview diagram: FE ↔ API (REST & GraphQL) ↔ DB
2. Table schemas: Users, Campaigns, Donations, Roles/RBAC (with explanations)
3. API contracts: Example REST endpoints + sample JSON; example GraphQL queries/mutations
4. Workflow descriptions: Step-by-step for key user stories (admin/organizer actions)
5. Discussion: What would you optimize, monitor, or secure? How would you automate or scale?

## Misc Topics
- Rest API: GraphQL v FastAPI
    * FastAPI (REST):
        * Pros
            - __Simplicity and Speed__: Scaffold REST endpoints w/ auto validation, interactive docs
                - Performative v traditional REST use cases
            - __Great for CRUD__: Simple, well defined endpoints -> fast build, easy security
            - __Easier Caching__: Efficiently leverage HTTP Caching Mechanisms
            - __Explicitness__: REST enforces clear patterns of GET/POST/DELETE -> API design, doc is clear
        * Cons
            - Can lead to excess network calls for complex/nested data -> less flexibility for clients in response shape

    * Graph QL
        * Pros
            - __Flexible Queries__: Request precise data needed -> no over/under fetching as with Rest
            - __Efficient Complex Relationships__: Mitigate need for several requests for nested/related data
            - __Self-Documenting Schema__: Schema defines available queries + types
            - __Great for FEs__: Useful for when UIs need to present complex, dynamic view with customized data needs
        * Cons
            - Increase complexity for implementation and secure initially, tricker caching and pagination, overkill for simpler CRUD APis

    * Demo Interview [ if asked about graphql vs restapi, use of both ]:
        - If Donation Platform mostly involves CRUD (create, read, update, delete) + well defined resources -> FastAPI produces simpler and quicker dev for microproject
        - For greater fe user flexibility, integrate GraphQL for key queries

        - __What to say in Interview__:
            * I would implement REST and GraphQL endpoints atop an SQL DB.
                - REST is great for simple admin CRUD flows
                - GraphQL is great for flexible, aggregate dashboard queries
                    * shows that design systems where correct protocols are silo'ed to a specific platform area

    * Tradeoffs:
        - Simple python REST: Rapid dev w/ understood patterns, easy caching, monitoring, great for CRUD heavy admin portals
            - Examples:
                - CRUD campaigns (Clear, explicit, easy to secure)
                - CRUD user management (auth, role updates)
                - Basic auth/session management (fits rest pattern)

        - Graphql Bonus: Flexible data loading (platform growth), great for dashboards w/ custom aggregate views
            * Examples:
                - Nested related data i.e campaigns involving returned owner info ( efficient nested data fetching )
                - Paginate campaign and donor queries containing amounts, names ( mitigate multiple network reqs )
                - Aggregate stats, dashboard metrics: totalRaise, campaignCount, activeCampaigns ( complex queries handled in one call)

        - Docker v Kubernetes:
            * Docker Compose - ideal for dev/small projects
            * Kubernetes - migration path for scale/ops
            * DB: SQL (postgres) -> well suited to RBAC + relational models, robust
            * Data Ingestion: Key to automation, validation, monitoring, error recovery
