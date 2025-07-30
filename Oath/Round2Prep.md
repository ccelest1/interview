# Prep for Oath Round 2
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
        - [Dashboards, Permissions](#review-dp-tech)
        - [Hands On](#hands-on)
    - [Project Ownership and Collaboration](#project-ownership-and-collaboration)
        - [STAR](#star)
        - [PMA](#product-and-mission-alignment)

    - [Behavioral Questions](#behavioral-questions)

    - [Warmup](#warmup)

    - [TPM](#talking-points-and-materials)



## Technical Review Targeted Practice
### Review Frameworks
#### Review Typescript
[TS Crash Course](https://medium.com/@jannden/typescript-crash-course-79675b69d803)

##### Summary
* TS = Open source language built on JS
    - Main benefit of TS = ability to use static types
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
#### Review SQL
__[Learn SQL Concepts](https://www.youtube.com/watch?v=3s0lFtUrhSQ&t=74s)__
- SQL (structured query language): retrieve, insert, update and delete data from db

#### Review Serverless
### Review DP Tech
### Hands On

## Project Ownership and Collaboration
### STAR
### Product and Mission Alignment

## Behavioral Questions

## Warmup

## Talking Points and Materials
