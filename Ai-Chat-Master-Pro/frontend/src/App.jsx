import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, Bot, User, Cpu, Loader2, AlertTriangle } from 'lucide-react';

function App() {
  const [messages, setMessages] = useState([
    { text: "System Online. I am Ai-Chat-Master-Pro.", sender: "ai" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const scrollRef = useRef(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || loading) return;
    
    const userMsg = { text: input, sender: "user" };
    setMessages(prev => [...prev, userMsg]);
    const currentInput = input;
    setInput("");
    setLoading(true);

    try {
const res = await axios.post("https://ai-chat-master-pro-1.onrender.com", { message: currentInput });      setMessages(prev => [...prev, { text: res.data.response, sender: "ai" }]);
    } catch (err) {
      setMessages(prev => [...prev, { text: "Connection failed. Is the backend running?", sender: "ai", isError: true }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-black text-gray-100">
      <nav className="p-4 bg-gray-900 border-b border-gray-800 flex items-center gap-2">
        <Cpu className="text-blue-500" />
        <h1 className="font-bold tracking-widest">AI-CHAT-MASTER-PRO</h1>
      </nav>

      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`flex gap-3 max-w-xl ${m.sender === 'user' ? 'flex-row-reverse' : ''}`}>
              <div className={`w-10 h-10 rounded-full flex items-center justify-center border border-gray-700 ${m.isError ? 'bg-red-900' : 'bg-gray-800'}`}>
                {m.sender === 'user' ? <User size={18}/> : <Bot size={18} className="text-blue-400"/>}
              </div>
              <div className={`p-4 rounded-2xl ${m.sender === 'user' ? 'bg-blue-700' : 'bg-gray-800 border border-gray-700'} ${m.text.includes('⚠️') ? 'text-yellow-400 border-yellow-900' : ''}`}>
                {m.text}
              </div>
            </div>
          </div>
        ))}
        {loading && <div className="text-gray-500 animate-pulse text-sm">Processing...</div>}
        <div ref={scrollRef} />
      </div>

      <div className="p-6 bg-gray-900 border-t border-gray-800">
        <div className="max-w-3xl mx-auto flex gap-3">
          <input 
            className="flex-1 bg-black border border-gray-700 rounded-xl px-4 py-3 outline-none focus:border-blue-500"
            placeholder="Enter command..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          />
          <button onClick={handleSend} className="bg-blue-600 p-3 rounded-xl hover:bg-blue-500 transition-all">
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;