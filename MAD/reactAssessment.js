import { useState } from "react";


function textInput() {
    const [text_input, setTextInput] = useState('')
    const handleChange = (e) => {
        setTextInput(e.target.value)
    }

    return (
        <div>
            <label htmlFor="myInput"> Enter text </label>
            <input
                type="text"
                id="myInput"
                value={text_input}
                onChange={handleChange}
            />
            <p>
                {text_input}
            </p>
        </div>
    )
}

export default textInput
