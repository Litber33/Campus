import React, { useState, useContext } from 'react'
import { AuthContext } from '../auth/AuthContext'

export default function Login(){
  const [correo, setCorreo] = useState('')
  const [contrasena, setContrasena] = useState('')
  const [error, setError] = useState('')
  const { login } = useContext(AuthContext)

  const submit = async (e) => {
    e.preventDefault()
    try {
      await login(correo, contrasena)
    } catch (err) {
      console.error(err)
      setError('Credenciales inválidas')
    }
  }

  return (
    <div className="login-card">
      <h2>Iniciar sesión</h2>
      <form onSubmit={submit}>
        <input value={correo} onChange={e=>setCorreo(e.target.value)} placeholder="Correo" required />
        <input type="password" value={contrasena} onChange={e=>setContrasena(e.target.value)} placeholder="Contraseña" required />
        <button type="submit">Ingresar</button>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  )
}
