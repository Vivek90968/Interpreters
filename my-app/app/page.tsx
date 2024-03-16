import  "../styles/index.css";
import image from "../public/Group 9.svg"
import Image from "next/image";
export default function Home() {
  return (
    <div className="mainContainer" >
      <h1>Project <span className="text-['#B92BFF]" > Onion</span>: Tor Crawler Dashboard</h1>
      <Image src={image} alt="Tor Onion" />
    </div>
  )

}
   
