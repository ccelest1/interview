# Game Strategy - General FE/API/BE for Oath Donation Platform with Admin + RBAC

## Step 1: Requirement Clarification
- Questions to ask
    - To clarify problem scope prior to design:
        * Are  we going to primarily focus on be and/or fe?
        * Regarding Entities
            - Is correct to assume that campaigns are a collection of donations? If campaigns are just donations, should they consist of any other attributes? (info, text, images, videos)
            * (narrow down entities)
        * What are the user types are given to individuals on the platform 'admins, organizers, donors, or others?' ? Are those defined by an admin?
                * Following:
                    - For Admins,
                        * Are admins expected to create, edit, and delete campaign pages?
                        - Related question: Should admins be able to edit donation pages, individual donations, or just campaign/page info?
                        - Will admins include the permission set/actions of others users?
                    - Organizers
                        * Should organizers only manage their campaigns?
                            * Should donors and organizers on the platform be able to follow campaigns? Should donors and organizers be able to follow?
                    - Donors
                         * Do donors need to register or can they give anonymously?
                         * Are donors allowed to view or donate directly from pages?

        * From what I can understand, campaigns and donations will be separate entities, is that a correct assumption:
        * Campaigns + Donations:
            * Which users will be able to view campaigns?
            * How exactly will this dashboard be structured?
                - What attributes of campaigns will be made publicly and wont?
                - What users will be able to view dashboards (donations, campaigns)?
            * (My Understanding of Above) All will have dashboard specific screens/role with their correct permissions?
            * Search Functionality (campaigns, donors, organizers)?
            * Do we need to display trending/recommended campaigns?
            * Will there be notifications for regular users for new campaigns/donated to campaign events/news?
            * Will there be notifications for organizers about recent/biggest donations?
            * Should campaigns support several organizers?

- (From Sys Design Edit)
    * Abbreviated Questions
        * Are we going to primarily focus on be and/or fe?

        * Regarding Entities
            - Is correct to assume that campaigns are a collection of donations? If campaigns are just donations, should they consist of any other attributes? (info, text, images, videos)

        * What should users expect in terms of roles? What should a user expect in terms of permissions for said roles? (who should be able to CRUD and to what extent regarding donations and campaigns)
            * Should the expectation be that users are presented with varying screens/functionalities as it relates to their roles? -> i.e. authentication, authorization processes involved in login
            * Can users have multiple roles?

        * Should users be able to search for campaigns and donations?
        * Are recurring donations/campaign analytics required?
        * What are the compliance/security reqs?

        * Should i just focus on core features or are there any additional add-ons that I should prioritize?

        * Should i assume that our user base/user activity is quite large and that the eventual system is going to be in some way distributed?

        (Specific to August Interview)
        - Should I anticipate that other systems involved in this feature will be built out already? Or should I just give an estimate of the entire system including my feature addition?

* Functional Requirements (what a system does)
    * Outline
        - Roles, Permissions
        - Campaign, Donation Activity
            * Dashboard
        - Searching (? - may be out of scope)

    FRs
    * In scope
        - Users should be assigned their proper roles for correct feature functionality
            * Users should have dashboards reflect their role
        - Users should be able to view campaigns in list view
        - Users should be able to perform searches for donations, campaigns, maybe even users
    * Out of scope
        -* Users can donate anon
        -> Correct users should be able to view overall donation/their specific donation activity
        - Notifications about donation, campaign activity
        - Trending/Recommendations

Nonfunctional Reqs (how well a functional reqs are to be provided)
* In scope
    - The system should prioritize __availability for searching and viewing campaigns, consistency for donations__ (legal, financial compliance) -> donations exactly once, recorded once with correct amount, timestamp, user
    - system should be scalable and handle high throughput for popular campaigns
    - System is of course very read heavy (read>write)
    - system should provide secure donor transactions (purchase path security)
    - RBAC system -> dictate user roles and permissions

* Out of scope
    - system should ensure GDPR compliance
    - system should have regular backups
    - System should have low latency search


## Step 2: Database Design/Core Entities
- Core Entities
    * User (id, name, contact_field, donations[] (fk on donations))
        - Roles (Enums) and accompanying permissions table
    * Campaigns (id, name, owner[] (fk - connected to user), donations[] (fk on donations table to campaign))
    * Donation (id, amount, donor (fk), campaign (fk))

    - can just be a app config/table to enforce auth
    * Roles (id, fk to user_id, name)
        * Permissions(id, fk to roles, token - contains payload for correct actions.description - yes to this action)


## Step 3; API DESIGN
- Campaigns [ Campaign Service ]
    - listCampaigns() aggregate of individual campaigns-> GET /api/campaigns -> 200
        * Campaign[]
    ```
    {
        "content":[
            "campaign_id":
        ]
    }
    ```

    - getCampaign(id, name, date_created, donations[] (fk on donations table to campaign [many to one]), organizer (fk on campaign table to organizer) ) -> GET /events/search?keyword={keyword}&start={start_date}&end={end_date}&pageSize={page_size}&page={page_number} -> Campaign[]

        * for dashboard
    - putCampaign() -> PUT /api/campaigns/{id} -> 200, 404 if not found, 401 if not authorized
        * for new donations (trigger), editing campaigns

- Donations [ Donation Service ] - Payments
    - getDonation(id, user (fk to user table), amount, date_donation_made)
        * for campaigns model, fk (many to one in regards to campaigns)
        * GET /api/donations
    - postDonations(id, user (fk to user table), amount, date_donation_made)
        * POST /api/donations/:campaignId


- Users [ User Service ] - RBAC
    * getUser() - GET /api/get/users
    * getUsers() - GET /api/get/users/{id}

## Step 4: Diagramming (High Level)
[EXD](https://excalidraw.com/#json=bJUFbnjmRgrBIq_YNy1b8,Zg-B22uOsBY_pd1wvWXj2A)

## Step 5: Diagramming (Drill into Diagram Details)
[EXD](https://excalidraw.com/#json=bJUFbnjmRgrBIq_YNy1b8,Zg-B22uOsBY_pd1wvWXj2A)


## Step 6: Wrap Up/Optimizations


# Game Strategy - Specific FE/API/BE for Oath Donation Platform with Admin + RBAC


## Misc
1. Rest Endpoints
    * Post /campaigns, GET /campaigns, PUT /campaigns/{id}, DELETE /campaigns/{id}
    * GET /donations, POST /donations
    * GET /users

2. APIs
- Graphql
```
query GetCampaigns{
    campaign(id:'abc123'){
    title
    goal
    totalRaised
    owner{
      id
      name
      role
    }
    donations{
        id
        amount
        donor[
            id
            name
        ]
    }
  }
}
```


```
  mutation AddCampaign{
    addCampaign(title:'Peace, Progression, Prosperity', goal:1000, owner:..., donations = None){
      id
      title
      goal
      owner
      donations
    }
  }
```

3. Scale Estimates
- DB needs to handle several concurrent writes/reads -> select Postgresql for relational integrity and sql
    * Postgresql: must for ledger/transactions, users (strong ACID guarantees, relational integrity)
    * Nosql:
        - Campaign metadata/Content -> flexible, document-like data with potential structure changes over time (mongodb)
            * Schema flexibility (campaign content can be unstructured/varied), fast retrieval, easy denormalization
        - Activity Feed/Notifications -> real time updates, ephemeral (dynamodb/redis)
        - Analytics/Aggregations - Fast aggregations, column family/wide-row store (Cassandra, DynamoDB)

- Initial deployment: docker compose -> migrate to kubernetes
- RBAC at DB:
    * Store role column; API checks owner_id for update/delete; logs all access attempts.
    * Consider views or row-level security for multi-tenancy if required.
        * Auth stub/Auth0 or next-auth provider that returns jwts, roles, credentials returned from be via user query combined with middleware for role-based auth
        * considering frontend -> useContext (React) for passing role data to all dashboard comps
        * conditional rendering of fts based on role

            * Fetching the JWT Token: Using getToken, we retrieve the JWT token which contains the user's role.
            * Redirecting Based on Role: We check the user’s role and redirect them to different paths based on their role (e.g., DOCTOR, NURSE).

### Diagram High Level
```
[ Next.js Frontend (React/TypeScript) ]
             │      │
     REST (CRUD)    │
     GraphQL (nested queries, analytics) (Identity Provider/Auth0)
             ↓
[ FastAPI Backend (Python) ] (CRUD, RBAC, Middleware)
             │
      SQLAlchemy ORM
             ↓
[ PostgreSQL DB ]
             ↑
[ Data Ingestion Process: Python scripts pulling vendor CSV/API ]
```

### Sharding
User DB: Probably not early on — scale vertically first.
Ledger DB: Yes, when donations grow large — sharding keeps write performance high.
Campaign DB (NoSQL): Yes, sharding is usually built in (e.g., MongoDB, DynamoDB).


## SQL API
```
models
class UserRole(enum):
    ADMIN = 'ADMIN'
    organizer = 'organizer'
    donor = 'donor'

class User(Base):
    __tablename__ = 'users'
    id = Column(integer, primary_key)
    name = Col(str)
    ...
    role = Column(Enum(UserRole)), default = UserRole.donor, nullable = False
    campaigns = relationship('Campaign', back_populates='owner')
    donations = relationship('Donations', back_populates='donor')

class Campaign(Base):
    id ...
    owner_id = Col(integer, foreignKey(users.id))
    owner = relationship('User', back_populates='campaigns')
    donations = relationship('Donation',  back_populates='campaigns')

Class Donation
    id  = Column(integer, primary_key)
    campaign_id = Col(integer, foreignKey(campaign.id))
    campaign = relationship('Campaign', back_populates = 'donations')
    donor_id = Col(integer, foreignKey(user.id))
    donor=relationsip(User, back_populates=;)

 schemas
class UserRole(str, Enum):
    admin = 'admin'
    ...

class userBase(BaseModel):
    name: str
    email: emailStr

routes
def assert_role(user: User, allowed_roles: List[UserRole]):
    if user.role not in allowed_roles:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
```

## ML
-
