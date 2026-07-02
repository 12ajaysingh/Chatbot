import { useState } from "react";

function SendIcon() {
  return (
    <svg
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2.2"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M22 2L11 13" />
      <path d="M22 2L15 22L11 13L2 9L22 2Z" />
    </svg>
  );
}

function Chatinput({ addMessage, loading }) {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (message.trim() === "" || loading) return;
    addMessage(message);
    setMessage("");
  };

  return (
    <div className="chat-input-container">
      <div className="chat-input-wrapper">
        <input
          className="chat-input"
          type="text"
          placeholder="Ask about any SHL assessment..."
          value={message}
          disabled={loading}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSend();
          }}
        />

        <button
          className={`send-btn ${loading ? "send-btn--loading" : ""}`}
          onClick={handleSend}
          disabled={loading || message.trim() === ""}
          aria-label="Send message"
        >
          <SendIcon />
        </button>
      </div>

      <p className="chat-input-hint">Press Enter to send · Powered by SHL AI</p>
    </div>
  );
}

export default Chatinput;
