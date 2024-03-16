import React from 'react'

const LoginForm = () => {
  return (
    <form className='form' >
      <label>Enter Your Username.</label>
      <input placeholder='UserName'  type='text'  />
      <label>Enter Your Password</label>
      <input placeholder='Enter Your Password.' type='password' ></input>
      <button>Login</button>
    </form>
  )
}

export default LoginForm
