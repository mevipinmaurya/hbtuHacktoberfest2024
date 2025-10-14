import React, { useEffect, useState } from "react";
import "../styles/greetingTimeWidget.css";

const GreetingTimeWidget = () => {
  const [currentTime, setCurrentTime] = useState(new Date());

  // Update time every minute
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 60000);

    return () => clearInterval(timer);
  }, []);

  // Format time
  const formatTime = (date) => {
    let hours = date.getHours();
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12;
    return `${hours}:${minutes} ${ampm}`;
  };

  // Determine greeting
  const getGreeting = () => {
    const hour = currentTime.getHours();
    if (hour >= 5 && hour < 12) return "Good morning 🌞";
    if (hour >= 12 && hour < 17) return "Good afternoon ☀️";
    if (hour >= 17 && hour < 21) return "Good evening 🌙";
    return "Good night 🌚";
  };

  return (
    <div className="greeting-widget">
      <p className="greeting-text">{getGreeting()}</p>
      <p className="time-text">{formatTime(currentTime)}</p>
    </div>
  );
};

export default GreetingTimeWidget;
