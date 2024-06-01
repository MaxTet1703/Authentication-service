import './EnterPage.css'
import 'bootstrap/dist/css/bootstrap.css'
import $ from 'jquery'
import SignUp from '../SignUp/SignUp.jsx'
import SignIn from '../SignIn/SignIn.jsx'


function EnterPage() {
    const removeOffset = () => {
        $(".slider").removeClass("offset");
        $(".form-slider").removeClass("move");
    }
    const addOffset = () => {
        $(".slider").addClass("offset");
        $(".form-slider").addClass("move");
    }
    return (
        <>
            <div className="enter-container d-flex flex-column">
                <div className="nav-btn">
                    <button className="login" onClick={removeOffset}>Вход</button>
                    <button className="sign-up" onClick={addOffset}>Регистрация</button>
                    <div className="slider"></div>
                </div>
                <div className="wrapper d-flex">
                    <div className="form-slider d-flex">
                            <SignIn />
                            <SignUp />
                    </div>
                </div>
                
            </div>
        </>
    )
}
export default EnterPage