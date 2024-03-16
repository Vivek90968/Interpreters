import LoginForm from '@/components/userDefined/client/LoginForm'
import React from 'react'
import "../../styles/authForm.scss"

const page = () => {
  return (
    <div className='authFormContainer' >
      <LoginForm />
    </div>
  )
}

export default page
