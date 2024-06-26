import 'bootstrap/dist/css/bootstrap.min.css'
import './signin.css'
import axios from 'axios'
import $ from 'jquery'
import { UserContext } from '../../App'
import { useContext } from 'react'


function SignIn({ setMessage }){

    const [user, setUser] = useContext(UserContext)

    const handleSubmit = (e) => {
        e.preventDefault()
        const data = new FormData(e.target)
        axios.post("http://127.0.0.1:8000/api/login/", data,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        })
        .then(( response ) => {
            localStorage.setItem("accessToken", response.data.access);
            localStorage.setItem("refreshToken", response.data.refresh);
            setUser((prev) => {
                return {
                    ...prev,
                    signed_in: true
                }
            })
        })
        .catch(( response ) => {
            setMessage(response.response.data.error)
            $("div.message").removeClass("hide");
        })
    }
    return (
        <>
            <form onSubmit={handleSubmit} id="signin" className='d-flex flex-column align-self-center'>
                <input type="email" name="email" placeholder="Введите Вашу почту"/>
                <input type="password" name="password" placeholder="Введиет пароль" />
                <button type='sumbit'>Войти</button>
            </form>
        </>
    )
}
export default SignIn