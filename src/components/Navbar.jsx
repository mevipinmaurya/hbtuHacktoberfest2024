import React, { useState } from 'react';
import '../styles/Navbar.css';

const Navbar = ({ links }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(prev => !prev);
  };

  const handleLinkClick = () => {
    setIsOpen(false);
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
