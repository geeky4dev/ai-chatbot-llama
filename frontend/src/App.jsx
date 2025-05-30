import { useState } from 'react'

function App() {
  const [message, setMessage] = useState("")
  const [reply, setReply] = useState("")

  const sendMessage = async () => {
    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }) // use message instead of userInput
      })

      const data = await response.json()
      if (data.reply) {
        setReply(data.reply)
      } else if (data.error) {
        setReply("Server error: " + data.error)
      } else {
        setReply("Unexpected response.")
      }
    } catch (error) {
      setReply("Error connecting to the server.")
      console.error("Error:", error)
    }
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI Chatbot - Groq Llama</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your question"
      />
      <button onClick={sendMessage}>Send</button>
      <p><strong>Reply:</strong> {reply}</p>
    </div>
  )
}

export default App


