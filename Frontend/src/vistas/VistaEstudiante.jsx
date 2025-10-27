import { useEffect, useState } from "react";
import { listarEstudiantes } from "../servicios/api";

export default function VistaEstudiante() {
  const [estudiantes, setEstudiantes] = useState([]);

  useEffect(() => {
    listarEstudiantes().then((res) => setEstudiantes(res.data));
  }, []);

  return (
    <div className="vista">
      <h2>Panel del Estudiante</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th><th>Correo</th><th>Programa</th><th>Semestre</th>
          </tr>
        </thead>
        <tbody>
          {estudiantes.map((e) => (
            <tr key={e.id}>
              <td>{e.nombre}</td>
              <td>{e.correo}</td>
              <td>{e.programa}</td>
              <td>{e.semestre}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
