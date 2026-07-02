import { useEffect, useRef } from "react";
import Message from "./Message";

const SUGGESTIONS = [
  "Verbal reasoning tests",
  "Leadership assessments",
  "Numerical ability tests",
];

function Chatbox({ messages, loading, onSuggestion }) {
  const bottomRef = useRef(null);
  const showSuggestions = messages.length === 0 && !loading;

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="chat-box">
      {showSuggestions && (
        <div className="chat-box__empty">
          <div className="chat-box__empty-icon" aria-hidden="true">
            💬
          </div>
          <div className="chat-box__empty-title">How can I help?</div>
          <div className="chat-box__empty-desc">
            Describe the skills or role you're hiring for and I'll suggest the
            right SHL assessments.
          </div>
          <div className="chat-box__chips">
            {SUGGESTIONS.map((suggestion) => (
              <button
                key={suggestion}
                type="button"
                className="chip"
                onClick={() => onSuggestion(suggestion)}
              >
                {suggestion}
              </button>
            ))}
          </div>
        </div>
      )}

      {messages.map((message, index) => (
        <Message
          key={index}
          sender={message.sender}
          text={message.text}
          recommendations={message.recommendations}
          style={{ animationDelay: `${index * 0.04}s` }}
        />
      ))}

      {loading && (
        <Message sender="AI" text="" isTyping style={{ animationDelay: "0s" }} />
      )}

      <div ref={bottomRef} />
    </div>
  );
}

export default Chatbox;
