import React, { useEffect, useState } from 'react'
import { listarEstudiantes } from '../servicios/api'

export default function VistaEstudiante(){
  const [datos, setDatos] = useState([])
  useEffect(()=>{ listarEstudiantes().then(r=>setDatos(r.data)).catch(()=>{}) },[])
  return (
    <div>
      <h2>Panel Estudiante</h2>
      <ul>{datos.map(d => <li key={d.id}>{d.id} - {d.programa || 'Sin programa'}</li>)}</ul>
    </div>
  )
}
