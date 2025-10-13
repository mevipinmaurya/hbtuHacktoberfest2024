import { useState, useEffect } from "react";

export default function FunFact() {
  const [fact, setFact] = useState("");

  const fetchFact = async () => {
    try {
      const res = await fetch("https://uselessfacts.jsph.pl/random.json?language=en");
      const data = await res.json();
      setFact(data.text);
    } catch (err) {
      setFact("Couldn’t load a fun fact 😅");
    }
  };

  useEffect(() => {
    fetchFact();
  }, []);

  return (
    <div style={{
      background: "#f9f9f9",
      padding: "1rem",
      borderRadius: "12px",
      textAlign: "center",
      margin: "2rem auto",
      maxWidth: "400px",
      boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
    }}>
      <h3>🤓 Fun Fact</h3>
      <p>{fact}</p>
      <button
        onClick={fetchFact}
        style={{
          marginTop: "10px",
          background: "#007bff",
          color: "white",
          border: "none",
          borderRadius: "6px",
          padding: "8px 12px",
          cursor: "pointer"
        }}
      >
        New Fact 🔄
      </button>
    </div>
  );
}

