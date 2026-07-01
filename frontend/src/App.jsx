import Header from "./components/Header"
import Chatbox from "./components/Chatbox"
import Chatinput from "./components/Chatinput";
import { useState } from "react";
import { getAIResponce } from "./service/aiService";

function  App(){
  const [message, setMessage] = useState([
    {
      sender:"AI",
      text:"Hello! I'm your shl assistant"
    }
  ]);



  const addMessage=(text) => {
    const userMessage = {
      sender:"You",
      text: text,
    }

    const reply = getAIResponce(text);
    setMessage(prev => [...message,userMessage]);
    setTimeout(() => {
      const aiMessage = {
          sender:"AI",
          text:reply
      }
      setMessage(prev => [...prev,aiMessage])
    },1000)
  }

  return(
    <>
    <Header/>
    <Chatbox messages={message}/>
    <Chatinput addMessage={addMessage}/>
    </>
  );
}

export default App;