# Prep
- Sections:
    - [Technical Review, Targeted Practice](#technical-review-targeted-practice)
        - [Review Frameworks](#review-frameworks)
            - [Review Typescript](#review-typescript)
            - [Review React](#review-react)
            - [Review NextJS](#review-next)
            - [Review Adv Python](#review-python)
            - [Review GraphQL](#review-graphql)
            - [Review SQL](#review-sql)
            - [Review Serverless Architecture](#review-serverless)
              - [Review AWS](#review-aws)
        - [Dashboards, Permissions](#review-dp-tech)
        - [Hands On](#hands-on)

## Technical Review Targeted Practice
### Review Frameworks

## Closures, Prototype inheritance, Recursion and coding challenges.
- Closures

- Prototype Inheritance
- Recursion

#### Review Typescript
> Experience with Typescript

  - Typescript
    * TS:

      * Nxtgen
        - [ Social platform for engineers to showcase own projects/developments ]
          * Performed prototyping using TS (Static Types, Compile time errors)
            * Unique case of using TS was for declaration of loading, fail, success states as it related to loading user posts -> provide a granular understanding to FE for in progress data load + !

      * T3 - Twitter:
        - Next.js, Typescript, tRPC, Tailwind CSS, Prisma, Planetscale, Vercel
        * tRPC: type safe RPC framework for API development
          - RPC = Remote Call Procedure -> call functions/procedures on different server in same way as local function (serverless)
        * Tailwind: Utility first css framework for rapid UI development
        * Prisma: Next-generation ORM (Object-Relational Mapper) for DBs
        * Planetscale: Serverless mysql db platform
        * Vercel: Cloud platform for deploying, hosting web apps -> auto deployments, serverless, global CDN
            - Worked on a pet project recreating twitter using TRPC (Creating contexts for understanding user identity, getting user data), createPostWizard, getPostsByUserID (public procedure for obtaining posts for entire user feed), profilePage(s) via slugs ([slug].tsx via @{author})

[TS Crash Course](https://medium.com/@jannden/typescript-crash-course-79675b69d803)

##### Summary
* TS = Open source language built on JS
    - Main benefit of TS = ability to use __static types__
##### Dynamic and statically typed languages
* JS = dynamic typed language allowing for hard-to-spot bugs if type isn't manually inferred
* Statically typed languages like TS
    - Require explicit assignment of types to variables, function params, return values, etc.
        - Prevent bugs and undesirable program behavior later

##### Typescript Use
- Run with `npm install typescript --save-dev`
    * TS as a JS super set needs to be complied down to regular JS for code to actually be executed by TSC (TS Compiler)
    * Can use `tsconfig.json` in order to configure TS machination in environment, JS compilation
        - ```json
            tsc --watch index.ts
          ```
    * Start w/ `index.ts` -> .ts(regular js file), .tsx (react - jsx syntax)
    ```ts
    let price: number = 123
    ```

##### Basic Types
- Most basic types
    * number, string, boolean, any (take any type)
    ```ts
    let price: number = 12
    let product: string = 'daily'
    let isInStock: boolean = true
    let buyers:any = "wiz"
    // can also do
    buyers = true
    ```
    - Instead of `any` can use union of various types
        * `let sellers: numbers | string = 'ten sellers'`

##### Type Assertions
- We have a variable that can hold `any` type -> but want to create another var with more specific type -> assign to value of first one
    * ```ts
       let headcount: any = 1999
       let s1 = headcount as number;
       let s2 = <number> headcount
      ```

##### TS Arrays
- Arrays hold various values in sequence
    * 2 methods
        1. Use square brackets
        2, Generic array type `Array<elementType>`
        ```ts
        let games: string[] = ['wiz','biz']
        let games: Array<string> = ['wiz','biz']
        ```
##### Tuples
- Can specify various types for each element
    - ```ts
        let tuple1: [number, string, boolean] = [1,'str', true]
        let tupleArray: [number, string][] = [ [5, "Expelliarmus"], [7, "Lumos"] ];
      ```
##### Functions
- Specify types of params, return values
```ts
// fix input and output types required, expected
function castAdvSpell(
    spellId: number|string,
    target: string
): string{
    return 'success'
}
// function doesn't return anything
function noReturn(): void {
    // doesn't return value
}
```
##### Generic Functions
- Make code far more dynamic and allow for creation of reusable components
```ts
function mostCommonScore<ScoreType>(
    allScores: ScoreType[]
): ScoreType{
    return allScores.sort((a,b)=>
        allScores.filter(v=> v===a).length
        - allScores.filter(v=> v===b).length
    ).pop();
}
console.log(
  mostCommonScore<number>([50, 75, 75, 100])
); // -> 75
console.log(
  mostCommonScore<string>(["Average", "Good", "Good", "Excellent"])
); // -> Good
```
##### Enum
- Allow for declaration of a set named constants w/ numeric or string values
```ts
// These will get automatically assigned numerical values
enum bookCategories {
  History, // -> 0
  Beasts, // -> 1
  Spells, // -> 2
}

// We can also assign our own numeric values
// If we omit a numeric value, automatically it will be the next in the sequence
enum spellStrengths {
  Defensive = 5, // -> 5
  Offensive, // -> 6
  Fun = 10, // -> 10
}

// String values are not a problem either and we can mix them in with numerical values
enum spellNames {
  Defensive = "EXPELLIARMUS", // -> EXPELLIARMUS
  Offensive = "OBLIVIATE", // -> OBLIVIATE
  Fun = "ALOHOMORA", // -> ALOHOMORA
  SpellCount = 3, // -> 3
  AnotherCount, // -> 4
}
```

##### Interfaces
```ts
// interface definition
interface Student{
    id: number,
    name: string,
    magic(spell: string): void
    age?: number; //optional
    readonly house: string //can only be assigned once on instantiation
}

const harry: Student = {
    id: 1,
    name: 'Harry',
    magic: (spell) => console.log(spell),
    house: 'gryff'
}

// can also do type
type student_type = {
    id: number;
    name: string;
    magic(spell:string):void;
    age?:number;
    readonly house: string
}

const harry: student_type = {
    id: 1,
    name: 'Harry',
    magic: (spell) => console.log(spell),
    house: 'gryff'
}

/*

Use interfaces:
When defining object shape that I expect to extend or repeatedly declare

Use type aliases:
When needing to express more complex types (unions, intersections, tuples)

Simple product shapes: Preference is towards interface due to readability, future extensibility

 * /
```
##### Class
- Use interfaces -> assign type to class with `implements`
```ts
interface Student{
    id: number,
    name: string,
    magic(spell: string): void
    age?: number, //optional
    readonly house: string //can only be assigned once on instantiation
}
```
```ts
class Student implements Student{
    id:number
    name: string

    constructor(id: number, name: string){
        this.id = id
        this.name - name
    }
    magic(spell: string): string{
        return `${this.name} cast ${spell}`;
    }
}

 const potter = new Student(1, 'Harry')
// reuse enum type
console.log(potter.magic(
    spellNames.Fun
))
```

Desire: want to further extend our created class -> next gen of students inherits parent's properties
    - demo `private`, `protected` keywords
```ts
class YoungerStudent extends Student{
    private parents: string[]; // only accessible in class
    protected relatives: string[] // class, sub-class accessible

    constructor(
        id:number,
        name:string,
        parents:string[],
        relatives:string[]
    ){
        this.parents = parents
        this.relatives = relatives
    }
    meetTheParents():void{ //returns nothing, outputs property in class
        console.log(this.parents)
    }
}

const potter2 = new YoungerStudent(
    1, James, ["Harry", "Ginny"], ["Lilly", "Molly"]
)

potter2.meetTheParents()
```
##### TS in React
```tsx
import * as React from "react";
import { render } from "react-dom";

export interface CustomPropsType{
    title:string;
    message?:string;
}

function App(
    props: CustomPropsType
){
    return(
           <>
      <h1>{props.title}</h1>
      <p>{props.message ? props.message : "No message available."}</p>
    </>
    )
}

render(<App title="Welcome" />, document.getElementById("root"));
```

[TS in React](https://profy.dev/article/react-typescript)
##### First Sections
```ts
// types
string, boolean, number
// arrays -> can be built from primitives/other type
number[], string[], User[]
//objects and types, enums
enum UserRole {
  CEO = "ceo",
  CTO = "cto",
  SUBORDINATE = "inferior-person",
}

type User = {
    firstName: string;
    age: number;
    isNice: boolean;
    role: UserRole; //use enum for specificity
    skills; string[];
    friends?: User[];
}
const user = {
  firstName: "Pat",
  age: 23,
  isNice: false,
  role: UserRole.CTO,
    skills: ["CSS", "HTML", "jQuery"],
    friends: undefined
}
```

##### Functions
```ts
// can either write types inline, type extraction and also specify return type
function fireUser({ firstName, age, isNice }: {
  firstName: string;
  age: number;
  isNice: boolean;
}): User {
  ...
}
type User = {
  firstName: string;
  age: number;
  role: UserRole;
}

function fireUser({ firstName, age, role }: User): User {
  ...
}

// exercise
// Challenge: type the function parameters
type product = {
  name: string;
  price: number;
  images: string[];
}

function updateProduct({name, price, images}: product):void{
  // update logic here ...
  console.log({ name, price, images });
}

updateProduct("Shampoo", 2.99, ["image-1.png", "image-2.png"]);

```

##### React w/ TS
```tsx
// example of passing props in order to enable messages specific to user  determined by role as specified by the enum

enum UserRole {
  CEO = "ceo",
  CTO = "cto",
  SUBORDINATE = "inferior-person",
}

type UserProfileProps = {
  firstName: string;
  role: UserRole;
}

function UserProfile({ firstName, role }: UserProfileProps) {
    if (role === UserRole.CTO) {
    return <div>Hey Pat, you're AWESOME!!</div>
  }
  return <div>Hi {firstName}, you suck!</div>
}

// exercise

// Challenge: Fix the error in the App component
// Challenge: type the function parameters


export function App() {
  return (
    <div>
      <Product />
    </div>
  );
}

function Product() {
  const { product, error } = useGetProduct();

  if (error) {
    return <>{error.message}</>;
  }

// allows for product to not error undefined
  if(!product){
    return(
      <div> No product </div>
    )
  }
  return (
    <div>
      <div>
        {product.name} ${product.price}
      </div>
      // add key for mapping
      {product.images.map((src, idx) => (
        <img key={idx} src={src} />
      ))}
    </div>
  );
}

// no need to read this, simply check
// the types in the Product component
// create type
type product_type = {
  name: string;
  price: number;
  images: string[];
}
function useGetProduct():
// set product_type for product
  | { product: product_type; error: undefined }
  | { product: undefined; error: Error } {
  if (Math.random() > 0.5) {
    return { product: undefined, error: new Error("Something went wrong") };
  }
  return {
    error: undefined,
    product: {
      name: "Shampoo",
      price: 2.99,
      images: ["image-1.png", "image-2.png"],
    },
  };
}
```
###### Callback
```tsx
type UserProfileProps = {
  id: string;
  firstName: string;
  role: UserRole;
  fireUser: (id: string) => void;
};

function UserProfile({ id, firstName, role, fireUser }: UserProfileProps) {
  if (role === UserRole.CTO) {
    return <div>Hey Pat, you're AWESOME!!</div>;
  }
  return (
    <>
      <div>Hi {firstName}, you suck!</div>
      <button onClick={() => fireUser(id)}>Fire this loser!</button>
    </>
  );
}

//exercise
// Challenge: type the props so that the component
// can be rendered as follows
//
// <Product
//   id="product-1"
//   name="Shampoo"
//   price={2.99}
//   images={["image-1.png", "image-2.png"]}
//   addToBasket={(id) => console.log(id)}
// />

type product = {
  id:string;
  name:string;
  price:number;
  images:string[];
}
interface product_props{
  Product: product;
  addToBasket(id:string):void;
}
export function Product({ Product, addToBasket }: product_props) {
  return (
    <div>
      <div>
        {Product.name} ${Product.price}
      </div>
      {Product.images.map((src) => (
        <img src={src} />
      ))}
      <button onClick={() => addToBasket(id)}></button>
    </div>
  );
}

// Default Props

type ProductProps = {
  name: string;
  price: number;
  // images is made optional
  images?: string[];
};

// supply empty array as default input
export function Product({ name, price, images = [] }: ProductProps) {
  return (
    <div>
      <div>
        {name} ${price}
      </div>
      {images.map((src) => (
        <img src={src} />
      ))}
    </div>
  );
}

```

###### useState Hook
```tsx
type ProductProps = {
  name: string;
  price: number;
};

export function Product({ name, price }: ProductProps) {
    // added string[] type
  const [images, setImages] = useState<string[]>([]);

  const addImage = () => {
    setImages(images.concat(`image-${images.length + 1}.png`));
  };
  ...

// custom Hooks
type ProductProps = {
  name: string;
  price: number;
  images: string[];
};

// added string[] for initialImages
function useImages(initialImages: string[]) {
  const [images, setImages] = useState(initialImages);

  const addImage = () => {
    setImages(images.concat(`image-${images.length + 1}.png`));
  };
  // add Image for second return value
  return { images, addImage };
}
```
###### TS React Events
```tsx
// Challenge: Type the event param in the onChangeName
// handler and set the name correctly

import { useState } from "react";

export function CreateProductForm() {
  const [name, setName] = useState("");

 // set the event type correctly with inference via the onchange
 // `React.ChangeEvent<HTMLInputElement>`
 // then setName to value via `event.target.value`
  const onChangeName = (event:React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value);
  };

  return (
    <form>
      <input onChange={onChangeName} placeholder="Name" value={name} />
    </form>
  );
}
```

###### Child Type or Component Type
```tsx
// React.ReactNode provides great flexibility, pass anything as child except object
type Layoutprops = {
    children: React.ReactNode;
};
function Layout({ children }): Layoutprops_{
    return <div> {children} </div>
}

// only allows markup
type LayoutProps = {
  children: React.ReactElement; // same as JSX.Element
};
```

###### Using Generics - 3rd party libs
```tsx
// axios -> returning requets
import axios from "axios"

async function fetchUser() {
  const response = await axios.get<User>("https://example.com/api/user");
  return response.data;
}

// react-query
import { useQuery } from "@tanstack/react-query";

function UserProfile() {
  // generic types for data and error
  const { data, error } = useQuery<User, Error>(["user"], () => fetchUser());

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  ...
}

// styled-comps
import styled from "styled-components";

// generic type for props
const MenuItem = styled.li<{ isActive: boolean }>`
  background: ${(props) => (props.isActive ? "red" : "gray")};
`;

function Menu() {
  return (
    <ul>
      <MenuItem isActive>Menu Item 1</MenuItem>
    </ul>
  );
}
```

###### Separating Types
```tsx
type User = {
  firstName: string;
  role: UserRole;
}

type UserProfileProps = {
  user: User;
    fireUser: (user: User) => void;
}

function UserProfile({ user, onClick }: UserProfileProps) {
  return (
    <>
      <div>Hi {user.firstName}, you suck!</div>
      <button onClick={() => fireUser(user)}>
        Fire this loser!
      </button>
    </>
  );
}
```



#### Review React
> Experience with React

- React
    * React: JS:
      - USGS (DOI): Worked on frontend user portals while at the USGS, which required vanilla JS, CSS, HTML
      - MedEase: Primarily a React based project where I used React as a state management platform + conditional rendering with advanced React Hooks in combination with other FE tools (chakraui, framer motion for transitions)

[React Main Core Concepts](​​https://payalpaul2436.medium.com/10-main-core-concept-you-need-to-know-about-react-303e986e1763)
##### Why Learn React JS
* React presents great solutions to FE issues -> fast, scalable, powerful, robust developer community [ rapid growth ]
    - Library, not a framework -> required to make decisions by self

    JSX Expressions
    ```jsx
    const myClasses = (
    <a href=”https://payal.com”>
    <h1>sign up</h1>
    </a>
    );


    ```
- JSX expression req to have 1 outermost element -> `<a>` tag = outermost
SX = js syntax extension -> used to create DOM elements, rendered in React DOM
JS file with JSX has to be compiled before reaching web browser

##### React Virtual DOM
- Performs significantly better than real DOM -> every time state of app changes, virtual dom is updated
    * How is virtual dom faster?
        - Virtual DOM represented by tree is created, each element = tree node
        - If any of the elements change, a new virtual DOM tree is created -> this tree is compared/diffed with previous virtual DOM tree
        - Once diffed, virtual DOM calculates best method to make real DOM changes -> min ops on real DOM, min cost of updating



##### Virtual DOM Use
- In React, UI pieces are components with each having their own state
    * Follows observable pattern, listen for state change -> update virtual dom -> diffing -> diff resolution
- React only updates the objects that have changed in real DOM
    * You tell React what state UI has to be in -> make sure updates occur [ do not need to know as a dev how attribute manipulation, even handling, or manual DOM updates occur bts ] - Abstracted away

##### JSX Props
- JS expressions as props
```jsx
<MyComponent foo={1 + 2 + 3 + 4} />
```
* Props.foo = 10

- if statements, for loops -> not expressions in JS [ placed in surrounding code ]
```jsx
function NumberDescription(props){
let description;
if(props.number % 2 == 0) {
description = <strong>even</strong>;
} else {
description = <i>odd</i>;
}
return <div>{props.number} is an {description} number</div>;
```

##### ReactJS - Components
- Combine comps to make app easier to maintain -> update and change comps w/o impacting rest of page
    * Stateless
        - First component = App -> owner of Header and Content
        - Header and Content are created separately and adding it inside JSX tree in App component
        - Only app comp is required to be exported
            ```jsx
            import React from 'react';
            class App extends React.Component {
            render() {
                return (
                    <div>
                        <Header/>
                        <Content/>
                    </div>
                );
            }
            }
            class Header extends React.Component {
            render() {
                return (
                    <div>
                        <h1>Header</h1>
                    </div>
                );
            }
            }
            class Content extends React.Component {
            render() {
                return (
                    <div>
                        <h2>Content</h2>
                        <p>The content text!!!</p>
                    </div>
                );
            }
            }
            export default App;
            ```


##### Props and PropTypes in React
- Understanding Props [properties]
    * Allow for data sharing across various comps that require them
    * Makes use of one-directional data flow (parent to child comps)
    * W/ a callback function, possible to pass props from child to parent comp
        - Data can be in various forms [ints, strs, …]
            ```jsx
            <PostList posts={postsList} />
            ```

##### React State
- __Class Components__

```jsx
const InputBox = React.createClass({
// set default component state -> empty text value [ use component method getInitialState() returning state object for component ]
getInitialState () {
return {
text: ''
}
},
// changeText() set to onChange event -> updating React state requires setState() method
changeText (event) {
this.setState({text: event.target.value})
},
render () {
return (
<div>
<input type='text' onChange={this.changeText}
placeholder='text' value={this.state.text} />
<span>{this.state.text}</span>
</div>
)
}
})
```

##### React Hooks
- Allows for use of state, other React fts w/o writing a class -> functions that hook into React state and lifecycle fts from function components

- Backwards compatible

* When to Use
    - If function comp is written and state is a desired addition -> convert it to a class
* Hook Rules
    - Ensure that all stateful logic in comp is visible to the source code
        - Only at Top Level
            * Always used at top level, ensure hooks are called in same order through each component render
        - Only called from React functions
            * this.handleClick, this.state


#### Review Next
#### Review Python
#### Review GraphQl
* GQL - Query language for APIs and server-side runtime for query execution using type system defined in data
  * Uses strongly typed schema -> contract between client and server
  * Exposes single endpoint, allow clients to get data need from one request (avoid over and under fetching)

- Query Structure
```go
query GetProduct{
  product(id:'abc123'){
    name
    price
    inStock
    category{
      name
      parent
    }
  }
}
// able to pass arguments and requested nested data
// support vars, aliases, fragments for flex, readable requests
```

- mutations: Create, update, delete data -> changes server data
  * start with keyword `mutation`
  ```go
  mutation AddProduct{
    addProduct(name:'soap',price;2){
      id
      name
      price
    }
  }
  // can update, insert, delete records w/ mutations -> optionally w/ vars for dynamic inputs
  ```

- Resolvers: backend functions tell Graphql to fetch, computer data for field/mutation
  - each field in query/mutation has corresponding resolver function
  - connect schema to actually data sources (dbs, apis) and handle logic for what is to be returned to client
  ```js
  const resolvers = {
    Query: {
      product[parent, args, context, info]{
        return products.find(
          p => p.id === args.id
        )
      },
      Mutation:{
        addProduct(parent, args, context, info){
          return db.createProduct(args)
        }
      }
    }
  }
  ```

#### Review SQL
> How to judge if a SQL query is well written and performant

1. Is the query clear and maintainable?
    - Does it use explicit JOINS, clear aliases, avoid unnecessary complexity?
    - Avoided SELECT *
2. Use EXPLAIN or EXPLAIN ANALYZE in Postgres (pgAdmin)
    - Inspect the execution plan (look for full table scans, sequential scans where an index can be used, costly operations)
    - Check whether indexes are used, if joins are efficient
3. Track actual performance - execution time, rows returned vs expected, locking/walts with built in monitoring tools (padmin, built in postgres logs)
    - In AWS, RDS can be used to monitor query latency and resource consumption at DB + application level to understand bottlenecks impacting be pipeline
4. In regards to scalability -> does execution time grow in a linear fashion or does it spike due to inefficient ops?
    - Look for opportunities to rewrite subqueries, add missing indexes, refactor CTEs/views for speed
5. In regards to resource usage -> Observe CPU, memory, disk i/o usage for query
    - Ensure resource-intensive queries are optimized, appropriately batched

[Is Query good enough for production?](https://www.brentozar.com/archive/2020/08/how-do-i-know-if-my-query-is-good-enough-for-production/)

Things to think about:
  - How many times am I going to run it? Is it a one-off task or is it going to be ran several times/second on the front page?
  - What time of day/week will it be live? Are we under peak loads or is off-peak?
  - Does this server perform small transactional work or is it a reporting server?
  - Is my query going to hold locks while running?

Once these questions are answered:
    * Duration in terms of time, parallelism: how many cores are going to be involved and how long?
    * Reads: how much data is being read
    * Memory grant: Impacts other running queries

When evaluating a specific query:
- Am I in the correct ballpark as it pertains to time
    * If writing a transactional query [ accesses a small amount of data ]
      - Needs to finish in second or two
    * If writing a report
      - Need to finish in 10 to 30 seconds
- CPU time > elapsed time
    * If true, query went parallel across several CPU cores meaning there will need to be tuning

Query Logical Reads
  - Using `StatisticsParser.com` -> paste in returned row of messages/table -> focus on ‘logical reads’ col (number of 8kb pages query reads) regardless of pages being memory/storage fetched
    - Pages read by query = slower performance
  - If 6 digit reads are seen, need to perform query, index tuning

Look at Query Plan

> Importance of SQL Views
[Views Importance](https://www.reddit.com/r/SQL/comments/10mof83/can_somebody_explain_the_importance_of_views/)
- Importance of Views
    - View = query pretending to be a table
      * Pros:
        - Abstraction
          - Required to join data from several different tables to get all data required for specific type of report -> create view that pulls all data together, query if all data was stored nicely together already
        - Security
          - Only give access to view and not underlying tables -> user only able to query what was specifically selected for in the view
        - Efficiency
          - More efficiency from a development perspective, consistent to have a single view used by all
      * Cons:
        - Partially hinders the SQL optimizer


__[Learn SQL Concepts](https://www.youtube.com/watch?v=3s0lFtUrhSQ&t=74s)__
- SQL (structured query language): retrieve, insert, update and delete data from db
    * DMS - database management system (postgresql)
    - RDS - org data into rows, columns

- Can perform CRUD
    * `SELECT column1, column2 FROM table_name WHERE condition;`
    * `INSERT INTO table_name(col1, col2) VALUES(value1, value2)`
    * `UPDATE table_name SET column1=value1 WHERE condition;`
    * `DELETE FROM table_name WHERE condition`
- JOINS - combine rows from 2 or more tables based on related col
```sql
SELECT col1, col2
FROM table1
<INNER JOIN/LEFT JOIN/RIGHT JOIN/FULL JOIN> table2
on table1.col_name = table2.col_name
<-- last line is the common column for joining (like id)-->
```
- Data Types
    - varchar, integer, date, boolean
- Constraints
    - rules defined to maintain data integrity
        * Primary Key - ensure column value unique
        * Foreign key - maintain referential integrity between 2 tables
        * not null - col must have value
        * unique - unique values in col
- Aggregate functions
    - sum, avg, count, min, max

- Group by: Group data based on specific cols
```sql
SELECT col1, SUM(col2)
FROM table_name
GROUP BY col1;
<-- col1 = column to group by, sum(col2) - aggregate function sum calculating all total values in col2 for each group>'
```
- Order by: sort result set in asc, desc order
```sql
SELECT col, COUNT(col) AS count_alias
FROM table_name
GROUP BY column_name
ORDER BY count_alias [ASC|DESC]
```

- Subquery [inner, nested]: query embedded in another query
    * used to retrieve data used as filter/condition in main query
```sql
SELECT employee_name
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = "HR"
)
```

- Views: virtual tables created by queries, used like regular tables
```sql
CREATE VIEW view_name as
    SELECT col1, col2,...
    from table_name
    where condition;

<-- then to invoke view >

SELECT * from view_name;

<--- second example >
CREATE view post_info as
    SELECT title, username
    FROM posts INNER JOIN users
    ON posts.user_id = users.user_id

SELECT * from post_info
```
- Normalization: org data in db to minimize redundancy, improve data integrity

#### Review Serverless

##### Review AWS

##### Experience With
- S3: Simple Storage Service
  * Object storage service allowing for a variety of use cases [ data lakes, websites, mobile apps, images, backups, analytics ]
  * Provides management features to optimize, organize, configure access to data
    * https://docs.aws.amazon.com/s3/?icmpid=docs_homepage_featuredsvcs

- SQS: Simple Queue Service
  * Secure, durable, available hosted queue allowing for integration, decoupling of distributed software systems and components -> Offers DLQs (dead letter queues) -> aws sdk language supported
    * https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html

- AWS EC2
- AWS Lambda
- AWS RDS
- AWS VPC
- AWS Cloudwatch + Cloudinsights [ Error Logs ]
- Route 53
-

##### No Experience With
- SNS: Simple Notification Service
  * Web service coordinates and manages the delivery/sending of messages to subscribers of endpoints, clients
  * Pub/sub
    *  pubs communicate async with subs (web servers, sqs queues, lambda functions) by producing, sending messages to a topic -> logical access point and communication channel via a supported protocol
      - SQS, HTTP/S, AWS Lambda, email
    * https://docs.aws.amazon.com/sns/?icmpid=docs_homepage_appintegration

### Review DP Tech
[Implement RBAC in Python](https://www.osohq.com/learn/rbac-python)

* RBAC
  - Provides a structured way to define who is performing specific actions -> organizes permissions into roles, determining access
    * Roles-based rules, filtering data based on user roles

  - [Implementation](https://www.osohq.com/docs/app-integration/client-apis/python)
* When building app with user permissions - RBAC (Role Based Access Control) provides a structured method to define who can perform specified actions -> org permissions into roles determining access across various app parts
    - Roles = simplify auth logic for engineers, users
        * Group permissions
            - Permission: Action user takes on a resource -> user in org has permission to read repos

* Implementing RBAC -> use built in logic:
    - Use python classes - `Role` class, `User` to manage roles, permissions
        * Key benefits:
            - Group permissions into roles {simple logic}
            - Enforce the principle of least privilege -> restrict access based on roles
            - Support large user bases {structure access across various levels}
            - Integrate alongside other models for fine-grained access control
            - Meet GDPR, HIPAA compliance standards

* Express RBAC in Python
```python
# if user has role required to perform desired action
user = Value('User', User.get_current_user())
repo = Value('Repository', repo_name)
oso.authorize(user, 'read', repo)

# oso policy
actor User {}

resource Organization {
 roles = ["owner"];
}

resource Repository {
 permissions = ["read", "push"];
 roles = ["contributor", "maintainer"];
 relations = { parent: Organization };

 # An actor has the "read" permission if they have the "contributor" role.
 "read" if "contributor";
 # An actor has the "push" permission if they have the "maintainer" role.
 "push" if "maintainer";

 # An actor has the "contributor" role if they have the "maintainer" role.
 "contributor" if "maintainer";

 # An actor has the "maintainer" role if they have the "owner" role on the
 # "parent" Organization.
 "maintainer" if "owner" on "parent";
}

# filter data based on user's role
user = Value("User", User.get_current_user())
repos = oso.list(user, "read", "Repository")
```

- [AuthO](https://developer.auth0.com/resources/code-samples/api/flask/basic-role-based-access-control)

  * Allows for creating permissions, roles, users
    - Decorators to enforce API security policies
  * RBAC: enbaled by token based auth powered by JWTs -> Validate access tokens (JWT) using decorators
    - Request resources = req various access levels


### Hands On
