const handleSend = async () => {
    if (!input.trim() || loading) return;
    
    const userMsg = { text: input, sender: "user" };
    setMessages(prev => [...prev, userMsg]);
    const currentInput = input;
    setInput("");
    setLoading(true);

    // 1. DEFINE THE URL EXPLICITLY
    const API_URL = "https://ai-chat-master-pro.onrender.com/chat"; // <--- MUST HAVE /chat
    
    // 2. LOG IT TO CONSOLE (To prove it's correct)
    console.log("Attempting to send to:", API_URL);

    try {
      // 3. USE THE VARIABLE
      const res = await axios.post(API_URL, { message: currentInput });
      setMessages(prev => [...prev, { text: res.data.response, sender: "ai" }]);
    } catch (err) {
      console.error("Full Error Details:", err); // See the real error
      setMessages(prev => [...prev, { text: "Connection failed.", sender: "ai", isError: true }]);
    } finally {
      setLoading(false);
    }
  };