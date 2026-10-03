import React, { useRef, useState } from "react";
import './SearchField.css'

interface ChatMessage{
  user_message:string,
  response: string
}

const SearchField: React.FC = () => {
  
    const inputRef = useRef<HTMLInputElement>(null);
    const [isWelcome, setIsWelcome] = useState(false);
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [isLoading, setIsLoading] = useState(false);

    const sendMessage = async  () => {  
        console.log("Sending message:", inputRef.current?.value);
        const query = inputRef.current?.value || "";  
        if (!query.trim()) return; 

        console.log("Sending message:", query);

        try {
        
            setIsLoading(true);

            const response = await fetch("http://127.0.0.1:8000/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        user_id: 'userId',
                        user_message: query,
                    }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

          
            const data = await response.json();

            console.log("Response receivedddddd:", data);

            setMessages((prev) => [
                ...prev,
                {
                    user_message: query,
                    response: data.response[0].text
                }
            ]);

            setIsLoading(false);
            setIsWelcome(true);

        } catch (error) {
            console.error("Error sending message:", error);
            setIsLoading(false);
        }
    };
  return (
    <div className="search-field">
        
      {isWelcome && <div className="results-field">        
        {messages.map((message, index) => (
        <React.Fragment key={index}>
            <div className="query-message">
            {message.user_message}
            </div>

            <div className="result-messag">
                 <div className="result-message">
                    {message.response}
                </div>
            </div>
        </React.Fragment>
        ))}

        {isLoading && (
            <div className="result-messag">
                <div className="result-message">
                    One moment! I'm working on it...
                </div>
            </div>
        )}
       </div>}
      
        <div className="search-box">
            <input
                className="search-input"
                type="text"
                placeholder="Try dropping the word chicken"
                ref={inputRef}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                    sendMessage();
                    }
                }}
            />
            <button className="search-button" onClick={sendMessage}>🔍</button>
        </div>
      
      
    </div>
  );
};

export default SearchField;

