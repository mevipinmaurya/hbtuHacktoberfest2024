import React, { useState } from 'react';
import '../styles/Navbar.css';
import { useFocusMode } from './FocusModeContext';

const Navbar = ({ links }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(prev => !prev);
  };

  const handleLinkClick = () => {
    setIsOpen(false);
  };

  // ...existing code...
  // Use global focus mode context
  const { focusMode, setFocusMode } = useFocusMode();
  const handleFocusToggle = () => {
    setFocusMode(prev => !prev);
  };

  return (
    <nav className="navbar">
      <div className="navbar-inner">
        <div className="navbar-brand">
          <span className="logo">MySite</span>
          <button
            className="hamburger"
            onClick={toggleMenu}
            aria-label="Toggle navigation menu"
            aria-expanded={isOpen}
          >
            <span className="hamburger-line" />
            <span className="hamburger-line" />
            <span className="hamburger-line" />
          </button>
          {/* Focus mode toggle button */}
          <button
            className={`focus-toggle${focusMode ? ' active' : ''}`}
            onClick={handleFocusToggle}
            aria-pressed={focusMode}
            aria-label={focusMode ? 'Disable focus mode' : 'Enable focus mode'}
            tabIndex={0}
            onKeyDown={e => {
              if (e.key === 'Enter' || e.key === ' ') {
                handleFocusToggle();
              }
            }}
          >
            {focusMode ? 'Exit Focus Mode' : 'Focus Mode'}
          </button>
        </div>

        <ul className={`navbar-links ${isOpen ? 'open' : ''}`}> 
          {links.map((link, index) => (
            <li key={index} className="navbar-item">
              <a href={link.href} onClick={handleLinkClick}>
                {link.label}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
