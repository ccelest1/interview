import React, { useState } from 'react';

function TodoForm({ onSubmit }) {

    const [input, setInput] = useState('');

    const handleChange = (e) => {
        setInput(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const val = input.trim();
        if (!val) {
            console.log('Error: empty input...');
            return;
        }
        onSubmit(val);
        setInput(''); // clear form
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" className="itemInput" onChange={handleChange} value={input} />
            <button className="addItemButton">Add Item</button>
        </form>
    );
}

export default TodoForm;
