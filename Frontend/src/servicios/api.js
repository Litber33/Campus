import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' },
})

// interceptor para agregar token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export default api

// helpers
export const loginApi = async (correo, contrasena) => {
  // usar OAuth2 token endpoint
  const params = new URLSearchParams()
  params.append('username', correo)
  params.append('password', contrasena)
  // token endpoint: /auth/token
  const res = await axios.post(`${API_URL}/auth/token`, params, {
    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
  })
  return res.data
}

export const listarEstudiantes = () => api.get('/estudiantes/')
export const crearEstudiante = (data) => api.post('/estudiantes/', data)
export const listarProfesores = () => api.get('/profesores/')
export const listarPadres = () => api.get('/padres/')
export const listarUsuariosAdmin = () => api.get('/admin/usuarios')
