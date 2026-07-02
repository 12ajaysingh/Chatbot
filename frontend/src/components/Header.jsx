function Header() {
  return (
    <header className="header">
      <div className="header__icon" aria-hidden="true">
        ✦
      </div>
      <div className="header__text">
        <div className="header__title">SHL AI Assistant</div>
        <div className="header__subtitle">Smart assessment recommendations</div>
      </div>
      <div className="header__status">
        <span className="header__status-dot" />
        Online
      </div>
    </header>
  );
}

export default Header;
