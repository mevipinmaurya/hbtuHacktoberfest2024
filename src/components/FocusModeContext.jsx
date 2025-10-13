import React, { createContext, useContext, useState, useEffect } from 'react';

const FocusModeContext = createContext();

export function useFocusMode() {
  return useContext(FocusModeContext);
}

export function FocusModeProvider({ children }) {
  const [focusMode, setFocusMode] = useState(() => {
    const saved = localStorage.getItem('focusMode');
    return saved === 'true';
  });

  useEffect(() => {
    localStorage.setItem('focusMode', focusMode);
  }, [focusMode]);

  return (
    <FocusModeContext.Provider value={{ focusMode, setFocusMode }}>
      {children}
    </FocusModeContext.Provider>
  );
}
