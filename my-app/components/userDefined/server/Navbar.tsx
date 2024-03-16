'use client'

import Image from 'next/image'
import React, { useState } from 'react'
import logo  from "../../../public/logo.png"
import Link from 'next/link'
import "@/styles/navbar.scss"
import { FaBars, FaXmark } from "react-icons/fa6";

const Navbar = () => {
  const [navActive , setNavActive]  = useState(false);
  return (
    <nav>
      <div className='logo' >
        <Image src={logo} alt='Project Onion'  />
      </div>
      <div className='mobSwitch text-4xl' onClick={()=>{setNavActive(!navActive)}}  >
        {
          navActive ?<FaXmark /> : <FaBars />
        }
      </div>
      <div className={navActive ? "navOptions navComes" : "navOptions"} >
        <ul>
          <li><Link href={'login'} >Login</Link></li>
          <li><Link href={'register'} >Register</Link></li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar
