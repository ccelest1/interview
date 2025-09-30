import React, {useState} from "react";
import TodoItem from "./TodoItem";
import TodoForm from "./TodoForm";

function App() {

  const [items, setItems] = useState([]);

  const addItem = (item) => {
    const newList = [].concat(items, [{
      status: 'In Progress',
      todo: item
    }]);
    setItems(newList);
  };

  const removeItem = (idx) => {
    const newList = [].concat(items);
    newList.splice(idx, 1);
    setItems(newList);
  };

  const completeItem = (idx) => {
    const newList = [].concat(items);
    newList[idx].status = 'Complete';
    setItems(newList);
  };

  const unCompleteItem = (idx) => {
    const newList = [].concat(items);
    newList[idx].status = 'In Progress';
    setItems(newList);
  }

  return (
    <div className="app">
      <div className="todo-list">
        <ul>
        {items.map((item, idx) => {
          return (
            <li key={`li-${idx}`}>
              <TodoItem key={`item-${idx}`}
                item={item}
                onComplete={() => {completeItem(idx)}}
                onRemove={() => {removeItem(idx)}}
                unCompleteItem = {() => {unCompleteItem(idx)}}
              />
            </li>
          );
        })}
        </ul>
        <TodoForm onSubmit={addItem} />
      </div>
    </div>
  );
}

export default App;
