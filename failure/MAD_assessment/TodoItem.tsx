import React from 'react';

function TodoItem({item, onRemove, onComplete, unCompleteItem }) {

  const clickHandler = (checked) => {
    if(checked===false){
      unCompleteItem()
    }else{
      onComplete()
    }
  }

  return (
    <div className="singleTodoItem">
      <div className={item.status === 'Complete' ? 'completed' : ''}>{item.todo}</div>
      <div>
        <label> <input type="checkbox" onClick={e => clickHandler(e.target.checked)} /></label>
        <button className="removeTodoItem" onClick={onRemove}>X</button>
      </div>
    </div>
  );
}

export default TodoItem;
