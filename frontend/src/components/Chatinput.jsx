import { useState } from "react"



function Chatinput({addMessage}){
    const[message, setMessage] = useState("")
    return(
        <div>
            <input
            type="text"
            placeholder="Enter your message...."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
        />

        <button
        onClick={() => {
            if(message.trim() ==="")
                return;
            addMessage(message)
            setMessage("")

        }}>send</button>
        </div>
    )
}

export default Chatinput