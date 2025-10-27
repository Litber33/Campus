import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h1>Campus Virtual</h1>
      <ul>
        <li><Link to="/">Inicio</Link></li>
        <li><Link to="/login">Iniciar Sesión</Link></li>
      </ul>
    </nav>
  );
}