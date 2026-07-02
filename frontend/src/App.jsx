import Header from "./components/Header";
import Chatbox from "./components/Chatbox";
import Chatinput from "./components/Chatinput";
import { useState } from "react";
import { sendMessage } from "./api/chat";

function App() {
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState([]);

  const addMessage = async (text) => {
    const userMessage = {
      sender: "You",
      text: text,
    };

    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await sendMessage(text);

      const aiMessage = {
        sender: "AI",
        text: response.reply,
        recommendations: response.recommendations,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          sender: "AI",
          text: "Something went wrong. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <div className="floating-orb floating-orb--1" aria-hidden="true" />
      <div className="floating-orb floating-orb--2" aria-hidden="true" />
      <div className="floating-orb floating-orb--3" aria-hidden="true" />

      <div className="particles" aria-hidden="true">
        <span className="particle particle--1" />
        <span className="particle particle--2" />
        <span className="particle particle--3" />
        <span className="particle particle--4" />
        <span className="particle particle--5" />
        <span className="particle particle--6" />
      </div>

      <div className="app">
        <Header />
        <Chatbox messages={messages} loading={loading} onSuggestion={addMessage} />
        <Chatinput addMessage={addMessage} loading={loading} />
      </div>
    </div>
  );
}

export default App;
