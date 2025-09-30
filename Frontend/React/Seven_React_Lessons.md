# [7 React Lessons I Wish I Knew Earlier](https://www.youtube.com/watch?v=4AXQgOcL1mo&t=77s)

## Req: React State is Immutable
- Replace old data with new data with desired changes
    1. Make copy of old data
    2. Make changes to copy
    3. Replace original with copy
    ```js
    const [users, setUsers] = useState([])

    function addUser(newUser){
        newUsers = users.concat(newUser)
        // setUsers([...users, newUser])
        setUsers(newUsers)
    }

    <AddUser onSubmit={addUser} />
    <Users users={users} />
    ```

## useState() is not for everything
- There are multiple types of app state: Server, URL, Local storage + cookies

    - incorrectly using useEffect()
        ```js
        const [ data, setData ] = useState([])

        useEffect(()=>{
            fetch('/api/data')
                .then(res => res.json())
                .then(data => setData(data))
        }, [])
        ```
    - using ReactQuery for server state
        ```js
        const { data } = useQuery({
            queryKey:['apiData'],
            queryFn:() => fetch('/api/data').then(res=>res.json())
        })
        ```

    - Can use usePathname() vs useState() for obtaining web url
        * [ incorrect ] const [url, setUrl] = useState(window.location.pathname)
        * [ correct ] const pathname = usePathName()

    - Checklist
        * Is this a simple value that can be computed each render?
        * Is there a library that already holds the desired state?
        * Does it need to be rendered?
            - If answer is No, then put data in state

## Derive Values w/o State
- Derived values from other state, prop value can be put directly in jsx
```js
function Data({ date }){

    const formatted = new Date(date).toLocaleDateString()

    return <p> Date: {formatted} </p>
}
```
- Date in this example can derive during render (re-render when props change)

## Compute Values w/o Effects
- If simple computation:
    ```js
    function CalculateSum({ numbers }){

        const sum =  numbers.reduce((a,b)=> a+b, 0)
        return <p> Sum: {sum} </p>

    }
    ```
- If expensive calculation:
    * wrap in useMemo() that re-calcs when deps change
    ```js
    function CalculateSum({ numbers }){
        const sum = useMemo(()=>{
            return numbers.reduce((a,b)=> a+b, 0)
        }, [numbers])
        return <p> Sum: {sum} </p>
    }
    ```

## Keys should be Unique
* In list elements/nodes
```js

const items = [...]
const data = items.map(item=>{
    return {...item, id: crypto.randomUUID()}
})
return(
    <ul>{
        data.map((item)=>{
            <li key={item.id}>{item.name}</li>
        })
    }
    </ul>
)

```

## Don't Leave Out Dependencies
```js
const [count, setCount] = useState(0)

useEffect(()=>{
    const intervalID = setInterval(()=>{
        setCount(count+1)
    }, 1000)
    return () => clearInterval(intervalId)
}, [count]) //always make sure to incorporate dependencies

return <p> {count} seconds </p>
```
or based on comment
```js
const [count, setCount] = useState(0)

useEffect(()=>{
    const intervalID = setInterval(()=>{
        setCount(oldCount => oldCount + 1)
    }, 1000)
    return () => clearInterval(intervalId)
}, []) //always make sure to incorporate dependencies

return <p> {count} seconds </p>

```

## Don't overuse useEffect()
- Only specifies when code should run, instead of why and what it shoudl do
