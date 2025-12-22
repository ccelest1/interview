# [UI Coding Interviews](https://www.greatfrontend.com/front-end-interview-playbook/user-interface)
- Best practices, important concepts


## Types
- Range from smart UI components to complex client-facing products including small apps and games
    - Widgets, Comps, Layouts
        * Components
            - [Accordion](https://www.greatfrontend.com/questions/user-interface/accordion)
            - [Tabs](https://www.greatfrontend.com/questions/user-interface/tabs)
            - [Star Rating Widget](https://www.greatfrontend.com/questions/user-interface/star-rating)
            - [Tweet](https://www.greatfrontend.com/questions/user-interface/tweet)
            - Image Carousel
        * Widgets
            - [Digital Clock](https://www.greatfrontend.com/questions/user-interface/digital-clock)
            - [Analog Clock](https://www.greatfrontend.com/questions/user-interface/analog-clock)
        * Page Sections
            - [Signup Form](https://www.greatfrontend.com/questions/user-interface/signup-form)
            - [Holy Grail](https://www.greatfrontend.com/questions/user-interface/holy-grail)
    - Apps/Games
        - Longer time period -> 1/2 hr to 1hr to complete questions, esp in games
            * Apps:
                * [Todo List](https://www.greatfrontend.com/questions/user-interface/todo-list)
                * [Stopwatch](https://www.greatfrontend.com/questions/user-interface/todo-list)
                * [Temperature Converter](https://www.greatfrontend.com/questions/user-interface/temperature-converter)
            * Games
                * [Tic-tac-toe](https://www.greatfrontend.com/questions/user-interface/tic-tac-toe)
                * [Whack-a-mole](https://www.greatfrontend.com/questions/user-interface/whack-a-mole)


## Performing in UI Coding Interviews
1. Find out what is given
    - Coding Platform + Familiarize self with coding environment
        * Local vs Online IDEA
        * Supported editor shortcuts
        * Vanilla JS v Frameworks/Libraries
        * Execute code? Preview UI?
        * Latest support JS syntax and language fts
        * Can you install dependencies beforehand?
2. Introduction
    - <1 minute introduction
3. Clarify
    - Can newest JS syntax be used?
    - Id browser support
4. Complexity Management
    - Break down problem into stages/milestones -> communicate with interviewer
        * Focus of UI interviews: component states, APIs
5. Coding
    - Code solution and explain while doing so
        * Test code in browser per milestone/ft added
        * Read and parse in separate markdown doc: [Cheatsheet](https://www.greatfrontend.com/front-end-interview-playbook/user-interface-questions-cheatsheet)
6. Review
    - Read through code once, spot errors: typos, variables prior to initialization, incorrect API use
7. Testing
    - Outline basic test cases, edge cases
        - Test code and determine if it passes
    - Failure: Debug -> Fix
8. Tradeoffs
    - Explain:
        * Tradeoffs made
        * Cases not explicitly handled
        * Improve code with more time
9. Follow Ups
    - Prepare for follow ups

## Prepare for UI Coding Interviews
1. Core Concepts
    - Familair with [VCs](#vital-concepts)
    - Familair with [Quiz Section](https://www.greatfrontend.com/front-end-interview-playbook/quiz)
        - (Read and Parse)
2. Practice writing UI
    - Learn both: UIs in JS and UI framework of choice (React)
        * Vanilla:
            - Learn DOM Manipulation APIs
                * Creating DOM elements
                * Adding classes/attributes
                * Add child elements
        * Ui Framework:
            - Learn React
3. CSS
    - Vanilla CSS:
        * CSS Variables
    - Naming Convention:
        - [Block Element Modifier](https://getbem.com/naming/)

4. Deep Dives
    - [UI CheatSheet - same as above](https://www.greatfrontend.com/front-end-interview-playbook/user-interface-questions-cheatsheet)
        - (Read and Parse)
    - [UI Comp API Design Principles](https://www.greatfrontend.com/front-end-interview-playbook/user-interface-components-api-design-principles)
        - (Read and Parse)

5. Increase Practice
    * [GFE 75](https://www.greatfrontend.com/interviews/gfe75)
    * [Study Plans](https://www.greatfrontend.com/interviews/study-plans)
    * Practice [UI Questions](https://www.greatfrontend.com/questions/formats/ui-coding)
        * Even time with UI Comps and Building Apps/Games

## Vital Concepts
- DS
    * Arrays, Maps, Stacks (?), Trees (?), Sets
- SWE
    * SOLID (?), Design Patterns, Model-View-Controller (?)
- HTML
    * Semantic HTML(?), Forma validation(?), Form submission (?)
- CSS
    * Box model (?), Selectors, Specificity, Positioning (?), Units, Flexbox, Grid (?), CSS Custom Properties (vars)
- JS
    * Closures (?), Callbacks (?), Promise (?), Async/Await (meh), Handling variadic arguments (?)
- DOM
    * DOM Traversal (?), DOM Creation (meh), DOM Manipulation (meh), Accesing element/node properties (close), Event delegation (meh)
- Runtime APIs [ Heavy Review ]
    * setTimeout() (meh), setInterval() (?), Networking - fetch() (?)
- Accessibility
    * ARIA roles (?), states and properites (?), Keyboard interactions (meh)

## Eval Axes
- More emphasis on domain expertise, FE topics
    * Problem Solving
        - Systematic and logical approach to understanding and addressing a problem
        - Break down problem into smaller subproblems with evaluating different approaches + tradeoffs
    * Software Engineering Foundation
        - Familiar with DS, algos, runtime complexity, design pattern use, clean abstraction use
    * Domain Expertise
        - Understanding of
            * Browser (DOM, DOM APIs)
            * HTML/CSS
            * Javascript
            * User Experience
            * Accessibility
            * i18n (?)
            * Performance
            * Networks
    * Communication
        - Ask questions to clarify details, explain approach and considerations
    * Verification
        - Id several scenarios to test code against + edge cases

## Practice Qs
- [To go through](https://www.greatfrontend.com/questions/formats/ui-coding)
    - Required to test UI coded, so best to create test cases for each question

## Quiz Section
- Short close-ended questions testing domain understanding
- Examples
    * What is the CSS Box model?
    * What is the CSS selector specificity?
    * Differences between variables created using `let`, `var`, `const`
    * Use of `this` in JS
- Based off resume (can be asked questions about listed frameworks)
    * What problems does X tech solve?
    * Biggest advs, disadvs of X tech?
    * How does X tech work under the hood?
    * How does X tech compare to Y tech>

- Relevant Rounds
    * Recruiter: Review lightly concepts, frameworks, potential implementation solutions that are common
    * Online: Multiple choice
    * Coding:L Quiz questions asked prior, dive deeper into concepts mentioned
    * System Design: Further questions asked
    * Hiring Manager: Resume review

- Tips
    * Understand solutions to common questions and get real world experience with use in projects

- Practice
    * [JS Quiz](https://www.greatfrontend.com/questions/javascript-interview-questions/quiz)
    * [HTML Quiz](https://www.greatfrontend.com/questions/html-interview-questions/quiz)
    * [CSS Quiz](https://www.greatfrontend.com/questions/css-interview-questions/quiz)
