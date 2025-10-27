import React, { useContext } from 'react'
import { Navigate, Outlet } from 'react-router-dom'
import { AuthContext } from './AuthContext'

export default function ProtectedRoute({ roles = [] }){
  const { user } = useContext(AuthContext)

  if (!user) return <Navigate to="/login" replace />
  if (roles.length && !roles.includes(user.rol)) return <Navigate to="/login" replace />
  return <Outlet />
}
