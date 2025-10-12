import React, { useEffect, useState } from 'react';
import '../styles/GreetingClock.css';

const getGreeting = (hours) => {
  if (hours >= 5 && hours < 12) return { text: 'Good morning', emoji: '🌞' };
  if (hours >= 12 && hours < 17) return { text: 'Good afternoon', emoji: '☀️' };
  return { text: 'Good evening', emoji: '🌙' };
};

const formatTime = (date) => {
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
};

export default function GreetingClock({ updateInterval = 1000 }) {
  const [now, setNow] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setNow(new Date()), updateInterval);
    return () => clearInterval(timer);
  }, [updateInterval]);

  const { text, emoji } = getGreeting(now.getHours());

  return (
    <div className="greeting-clock" role="status" aria-live="polite">
      <div className="greeting">{text} <span className="emoji" aria-hidden>{emoji}</span></div>
      <div className="time">{formatTime(now)}</div>
    </div>
  );
}
