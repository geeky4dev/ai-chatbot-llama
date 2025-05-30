import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const backendUrl = import.meta.env.VITE_BACKEND_URL || "";

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);
    try {
      const response = await fetch(`${backendUrl}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();

      if (data.reply) {
        setReply(data.reply);
      } else if (data.error) {
        setReply("Server error: " + data.error);
      } else {
        setReply("Unexpected response.");
      }
      setMessage("");
    } catch (error) {
      setReply("Error connecting to the server.");
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI Chatbot - Groq Llama</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your question"
        disabled={loading}
      />
      <button onClick={sendMessage} disabled={loading || !message.trim()}>
        {loading ? "Sending..." : "Send"}
      </button>
      <p>
        <strong>Reply:</strong> {reply}
      </p>
    </div>
  );
}

export default App;


