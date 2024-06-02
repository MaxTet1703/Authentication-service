import './EnterPage.css'
import 'bootstrap/dist/css/bootstrap.css'
import $ from 'jquery'
import SignUp from '../SignUp/SignUp.jsx'
import SignIn from '../SignIn/SignIn.jsx'
import { IoMdClose } from "react-icons/io";
import { useState } from 'react'


function EnterPage() {
    const [message, setMessage] = useState("");
    const removeOffset = () => {
        $(".slider").removeClass("offset");
        $(".form-slider").removeClass("move");
    }
    const addOffset = () => {
        $(".slider").addClass("offset");
        $(".form-slider").addClass("move");
    }
    const closeMessage = () => {
        $(".message").addClass("hide");
    }
    return (
        <>
            <div className="message hide"><p>{message}</p><span onClick={closeMessage}><IoMdClose /></span></div>
            <div className="enter-container d-flex flex-column">
                <div className="nav-btn">
                    <button className="login" onClick={removeOffset}>Вход</button>
                    <button className="sign-up" onClick={addOffset}>Регистрация</button>
                    <div className="slider"></div>
                </div>
                <div className="wrapper d-flex">
                    <div className="form-slider d-flex">
                            <SignIn setMessage={setMessage}/>
                            <SignUp setMessage={setMessage} />
                    </div>
                </div>
                
            </div>
        </>
    )
}
export default EnterPage