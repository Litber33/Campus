import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './vistas/VistaLogin'
import Inicio from './vistas/VistaInicio'
import VistaEstudiante from './vistas/VistaEstudiante'
import VistaProfesor from './vistas/VistaProfesor'
import VistaPadre from './vistas/VistaPadre'
import VistaAdministrador from './vistas/VistaAdministrador'
import Navbar from './componentes/Navbar'
import { AuthProvider } from './auth/AuthContext'
import ProtectedRoute from './auth/ProtectedRoute'

export default function App(){
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Inicio />} />
          <Route path="/login" element={<Login />} />

          <Route element={<ProtectedRoute roles={['estudiante']} />}>
            <Route path="/estudiante" element={<VistaEstudiante />} />
          </Route>

          <Route element={<ProtectedRoute roles={['profesor']} />}>
            <Route path="/profesor" element={<VistaProfesor />} />
          </Route>

          <Route element={<ProtectedRoute roles={['padre']} />}>
            <Route path="/padre" element={<VistaPadre />} />
          </Route>

          <Route element={<ProtectedRoute roles={['administrador']} />}>
            <Route path="/admin" element={<VistaAdministrador />} />
          </Route>

        </Routes>
      </Router>
    </AuthProvider>
  )
}
