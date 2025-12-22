# Prep
- Sections:
    - [Resume Review](#resume-review)
        - [STAR](#star)

    - [Behavioral Questions](#behavioral-questions)

    - [TPM](#talking-points-and-materials)


#### Intro
INTRODUCTION
Hello, My name is Tyler. I am an interdisciplinary Software Developer with experience in Full Stack Agile Development and AI Programming. I value creating quality software through careful planning and design with my focus being centered on stakeholder value and user experience.

In my previous role at the USGS, I primarily worked on migrated legacy services over to modern stacks and providing users with access via portals powered by our backend system and data repositories. I worked on refactoring several of our backend pipelines as well

In regards to my background, I have had a wealth of software, data, and AI related experiences. During my undergraduate, I was a platform analyst for an energy company where I conducted A/B testing on their web and mobile interfaces and modeled a number of data and demand response trends regarding energy demand management. Following my undergraduate, I interned at an AI-focused company called Atlantic Automation and created an optimized data pipeline for financial analytics for their law firm partner ‘Bain and Barkley’. Two of my most recent experiences involved being a Backend Team Manager for an event platform for a coding organization and working on the frontend for a radiology report management platform.


#### Resume Review
> USGS - DOI - Integrated Info Disseminated Division
GOVERNMENT - SOFTWARE ENGINEER

> DEPARTMENT OF INTERIOR (USGS) (AUG 2024 - MAY 2025/PRESENT) [ DRP ]

- Developed and implemented advanced statistical computations—including percentiles, mean, and median—for the production stats service, boosting the data fetching pipeline’s performance by 20%

[ Revise to STAR Format]
  - Implemented query helper for assisting in the statistical calculation of provisional and approved data in our ingest pipeline

    * As our water quality/resource statistics require in field data acquired by researchers and scientists, we have to make a delineation between data that that has been certified as being accurate and those that are to be audited i.e estimated data
    * The above distinction will be demarcated in our dbs via flags in the dictionary/json formatted data
      - Flag: ‘A,e’ in qualifiers key section

  - After that approval process, our determination of what stat to be calculated is then inputted by the user via a Fastapi frontend and then we use match-case python blocks in order to return the correct desired data [ mean, percentiles, median ]  for the provided site number
  - Percentiles in particular was interesting
    - We used a package (that had to be streamlined in its required dependencies) called HYSWAP (Hydrologic Surface Water Analysis Package) that is used in manipulation and visualization of USGS Water Data
    - HYSWAP has both Variable, Fixed, and Variable Moving Window percentiles to be returned (Variables -> computed with flow obs for particular day, fixed -> computer with flow obs in recorded period, Moving Window -> Understand how a particular time period ranks compared to other times of year in history)

 - Perform filtration of data [ approved, estimated ] -> convert these filtered dictionaries into a dataframe -> dataframe is fed into desired percentile methods desired by user -> return percentiles and other desired data (median, mode, etc.)


- Created and deployed comprehensive documentation for the Samples Service MVP and Stats Service, improving clarity and reducing help desk tickets by 80% for a user base of over 2.4 million researchers and developers
  * Worked on FASTAPI frontend user documentation for users to better understand how to gain desired information from queries -> maybe show current live link
    - Migration from legacy

- Refactored and engineered statistical upserts and timeseries SQL logic, optimizing data handling for samples and statistics services, achieving a 15% performance improvement across multiple projects
  - Extrapolate match case (of desired statistics) logic into its own externalized function for reuse in be pipeline
  - Performed combination of `get_upsert_normal_stats` and `get_upsert_interval_stats` (normal being the entire POR and interval being that defined in a specific period)
    - Depending on user desire, they either want to have data for entire history or between desired dates -> tasked with reducing logic in main into if/else, try/except in own encapsulated methods
    - Extrapolate logic combined with sql calls/statements made to db for required

- Engineered a secure, tier-limited DLQ redrive utility in iow-operational-utilities using AWS Lambda, enabling efficient data recovery within AWS SQS
  - Needed a method in order to redrive messages from a Dead Letter Queue to Source Queue (AWS)
    * Implemented code using AWS SDK to construct said method
    * Required a function that takes in params of information targeting DLQ to be redriven for processing or deletion as required

- Implemented production-tier statistics service API and refined SQL queries to support scalable data loads (AWS RDS) and robust analytics
  * Performed stats api bootstrapping - set up ci/cd, built dummy service, package hierarchy, fastapi
  * Deployed to same prod VPC (virtual private cloud)

- Spearheaded a comprehensive optimization initiative using Liquibase database migration models, resulting in a 30% enhancement in backend performance pipeline efficiency across aqts-capture services
  * Performed a de-normalization of location service and samples data in our liquibase tables
  * Allowed for faster db returns matching user queries for the separate entities
  * Provided improvements for our samples bulk loads
    - Liquibase = tool for managin db schema state

> FREELANCE - BACKEND ENGINEER LEAD - NYC CODE AND COFFEE (JUN 2023 - NOV 2023)

Orchestrated the implementation of a sophisticated data pipeline and relational models using sqlite, resulting in streamlined data management and advanced analytics capabilities (Eliminated on-premise processing time)
BP1
Created RESTful API methods using FastAPI for event creation, attendance tracking, account management, user grouping, task lists, user communication, as well as notifications using websockets and message queues
BP1
Successfully aided in implementing security via user authentication and authorization using OAuth to provide protected endpoints and role identity
BP1

Led full-stack efforts on event-experience management project for coding organization (NYC Code and Coffee) in Javascript, Python (Primarily Backend with a team of 5, with design/prototyping using Svelte)
S - Had the opportunity to work on an event-experience management platform for a coding organization in NY known as Code and Coffee -> T - I was tasked with leading the backend efforts for the project and as a result I had to perform reconnaissance for what would best suite the org’s needs -> A - After gathering and confirming ideal technologies to be involved for our implementation (fastapi, sqlite, docker, oauth, message queues, and websockets), I then made sure to understand what individuals would be involved in the backend efforts and delegated tasks among them. -> R - We were able to accomplish serious progress with the backend, having created a prototype complete with desired models, routes, relationships, and a proper security flow. We are able to take on suggestions from the frontend team and often demo’ed our implementation to drive the whole team forward.

For the EEA app, I was put in charge with leading the efforts of the backend system and quickly realized that actualizing the stakeholder’s ideas would involve a somewhat intricate design -> I informed the stakeholder about my idea, but they rebuffed my ideas due to a lack of understanding and ask that I present my findings/concepts in a way that would be easier to understand -> I used Figma in order to conceptualize my be idea with models and relationships outlined -> The stakeholder had a clearer idea and was able to approve/make better suggestions.

### STAR
STAR
S - Situation
T - Task
A -  Action
R - Result

- Prepare a response. For each example, prepare a brief response:
- Describe the situation (2-3 sentences).
- Explain your task (1-2 sentences).
- Describe the action you took (2-3 sentences).
- Share your result (2-3 sentences).
  * Tell me about a time you had to complete a task within a tight deadline.
  * Describe the situation and explain how you handled it.
  * What do you do when a team member doesn't complete their share of the work?
  * Tell me about a time you showed initiative on the job.


Example:
Led full-stack efforts on event-experience management project for coding organization (NYC Code and Coffee) in Javascript, Python (Primarily Backend with a team of 5, with design/prototyping using Svelte)
S - Had the opportunity to work on an event-experience management platform for a coding organization in NY known as Code and Coffee -> T - I was tasked with leading the backend efforts for the project and as a result I had to perform reconnaissance for what would best suite the org’s needs -> A - After gathering and confirming ideal technologies to be involved for our implementation (fastapi, sqlite, docker, oauth, message queues, and websockets), I then made sure to understand what individuals would be involved in the backend efforts and delegated tasks among them. -> R - We were able to accomplish serious progress with the backend, having created a prototype complete with desired models, routes, relationships, and a proper security flow. We are able to take on suggestions from the frontend team and often demo’ed our implementation to drive the whole team forward.

As an intern, I worked at Atlantic Automation (an AI focused company) on a project for one of their partners: Bain and Barkley; While initially I didn’t have an assigned project, I was able to identify a pain point in their process which involved me designing, testing, and deploying python scripts to produce a more optimized pipeline for financial analytics (Python - utilised pandas, matplotlib in addition to component-based visualization)
Given a subset of AA’s work, I was tasked with identifying a potential project to work on and identified that they would benefit greatly from an improvement in their data pipeline process. I was tasked with then implementing said suggestion to provide a demo outlining my suggested improvements. Starting this process meant first understanding my strengths as it related to data preparation and processing. I identified the correct tools and based on what I observed of their current process, I set about performance and visualization improvements. I then presented my findings and a demo to my manager.

(technical collaboration) Uses appropriate configuration management platforms to collaboratively perform code submission and reviews + adapts to team norms
On my recent project being a Medical platform for doctors, I took the initiative to educate the team on collaborative tools
People were unfamiliar with the proper git process, understanding PRs, and using issues in order to track their own individual process -> I took the initiative to then conduct a session where I would educate the team about how it should systemically be carried out. -> Prior to the first meeting, I made a presentation that would aid people in a step by step understanding. When our first meeting took place, I then ran through a demo PR, demo issue, and demo workflow (branch, etc.). -> The team had a better understanding.

(Software Development Communication) Effective documentation, communication of risks, estimates, dependencies, relevant info regarding project/app with team + across org
On one of my and upcoming projects that I am working on is with a startup team and I took the initiative to create both the Frontend Wireframe and BE Mockup.
I was invited to be a part of the team for a startup that was being formed -> As the founders didn’t have prior experience with coding, they asked if anyone would be able to create FE wireframes and a BE mockup in order to start on the actualization of the platform. I decided to take the initiative to create both as a result of my versatile skillset -> In order to create a great FE wireframe, I decided to look at platforms that would have features similar to those desired by the founders and added my own ideas in order to target a streamlined design. For the BE, I utilized notes taken from our first meeting in order to design models and relationships that would make development easy -> I presented my work and the team was pleased.

(Problem solving) Uses sound judgment and creativity to apply technical knowledge, methodologies, and tools in order to recommend and/or develop new solutions
Collaborate w/ others to resolve challenges, create solutions, make progress w/ empathy, situational awareness, tact
During my undergraduate, I was involved in a capstone project with mechanical and electrical engineers and had to figure out how to make impact on the team through my expertise in software.
I was put on a team with other electrical, mechanical engineering students and I had to take the initiative to figure out how to create impact that just didn’t involve serving as a communication liaison, as a general engineering minor student -> I decided that providing impact would entail using whatever software experience I had at the time and naivete in mechanics and electrical engineering. This in aggregate would provide me with powerful insights about what design decisions the team could potentially not be thinking about. If I could present targeted evidence, then my insights would be substantiated. When discussions about a potential GUI were made, I realized an opportunity. -> To provide impactful insights, I began consulting with faculty and team members about our current design framework. I asked questions:  While we can easily study the turbine, can we approximate a holistic overview of the creek and turbine as a system? How do we pinpoint statistically significant pain points and reduce noise? Is there software that would already perform an analytical review of the turbine? -> Due to my driven questioning and investigation, I was able to discover solutions like SimScale and open-source software like WaterTurbine CFD that I tailored to fit the reality of our current machinery. My iteration and fitting based on our current machinery allowed me to come up with data-fueled insights to empower my team.


(Communication)
Explains in-depth or technical concepts using oral, written, and visual mediums, and in ways that different types of audiences can understand. Presents findings, recommendations, and alternatives to help others make a decision or understand the value of organizational IT needs. Communicates relevant project considerations and updates such as risks, estimates, and dependencies
An example of explaining technical concepts was when I had to provide rational to a backend system that I led in terms of development.
For the EEA app, I was put in charge with leading the efforts of the backend system and quickly realized that actualizing the stakeholder’s ideas would involve a somewhat intricate design -> I informed the stakeholder about my idea, but they rebuffed my ideas due to a lack of understanding and ask that I present my findings/concepts in a way that would be easier to understand -> I used Figma in order to conceptualize my be idea with models and relationships outlined -> The stakeholder had a clearer idea and was able to approve/make better suggestions.

## Behavioral Questions
-  Tell me about a time you solved a hard technical problem?

- Tell me about a time you have a conflict with a teammate?

- What's a project you're proud of?

- When did you fail?

- Tell me about an interesting project you worked on

## Talking Points and Materials
