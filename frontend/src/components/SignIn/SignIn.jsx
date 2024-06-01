import 'bootstrap/dist/css/bootstrap.min.css'
import './signin.css'


function SignIn(){
    return (
        <>
            <form id="signin" className='d-flex flex-column align-self-center'>
                <input type="email" placeholder="Введите Вашу почту"/>
                <input type="password" placeholder="Введиет пароль" />
                <button type='sumbit'>Войти</button>
            </form>
        </>
    )
}
export default SignIn