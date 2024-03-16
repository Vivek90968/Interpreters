import React from 'react'
import "../../../styles/authForm.scss"

const RegisterForm = () => {
  return (
        <form className='form' >
          <label>Name</label>
          <input placeholder='Name'  type='email'  />
          <label>Email</label>
          <input placeholder='Enter Your email.' type='email' ></input>
          <label>Password</label>
          <input placeholder='Enter Your Password.' type='password' ></input>
          <label>Confirm Password</label>
          <input placeholder='Confirm Your Password.' type='password' ></input>
          <button>Register</button>
        </form>
  )
}

export default RegisterForm
