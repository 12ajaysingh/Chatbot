function Message({ sender, text, recommendations, isTyping, style }) {
  const isUser = sender === "You";

  return (
    <div
      className={`message-row ${isUser ? "user" : "ai"}`}
      style={style}
    >
      <div
        className={`message-avatar ${isUser ? "message-avatar--user" : "message-avatar--ai"}`}
        aria-hidden="true"
      >
        {isUser ? "👤" : "✦"}
      </div>

      <div className="message-content">
        <span className="message-sender">{sender}</span>

        <div className={`message-bubble ${isUser ? "user-bubble" : "ai-bubble"}`}>
          {isTyping ? (
            <div className="typing-indicator" aria-label="AI is typing">
              <span className="typing-dot" />
              <span className="typing-dot" />
              <span className="typing-dot" />
            </div>
          ) : (
            text
          )}

          {recommendations && recommendations.length > 0 && (
            <div className="recommendation-list">
              {recommendations.map((item, index) => (
                <div className="recommendation-card" key={index}>
                  <h4>{item.name}</h4>
                  <p>{item.test_type}</p>
                  <a href={item.url} target="_blank" rel="noreferrer">
                    View Assessment
                  </a>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Message;
