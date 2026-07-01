import Message from "./Message"

function Chatbox({messages}){
    return(
        <div className="chat-box">
            {messages?.map((message,index) => (
                <Message
                key={index}
                sender={message.sender}
                text={message.text}
                />
            ))}
        </div>
    )
}

export default Chatbox