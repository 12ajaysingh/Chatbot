function Message({text,sender}){
    return(
        <div>
            <strong>{sender}:</strong>
            <p>{text}</p>
        </div>
    );
}

export default Message;