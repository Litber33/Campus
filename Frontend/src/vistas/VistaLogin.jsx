import { useState } from "react";
import { login } from "../servicios/api";
import { useNavigate } from "react-router-dom";

export default function VistaLogin() {
  const [correo, setCorreo] = useState("");
  const [contraseña, setContraseña] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const manejarLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await login(correo, contraseña);
      const { rol } = res.data;

      // Redirigir según el rol
      if (rol === "estudiante") navigate("/estudiante");
      else if (rol === "profesor") navigate("/profesor");
      else if (rol === "padre") navigate("/padre");
      else if (rol === "administrador") navigate("/admin");
    } catch (err) {
      setError("Credenciales incorrectas");
    }
  };

  return (
    <div className="login">
      <h2>Inicio de Sesión</h2>
      <form onSubmit={manejarLogin}>
        <input
          type="email"
          placeholder="Correo"
          value={correo}
          onChange={(e) => setCorreo(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={contraseña}
          onChange={(e) => setContraseña(e.target.value)}
          required
        />
        <button type="submit">Ingresar</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
}
