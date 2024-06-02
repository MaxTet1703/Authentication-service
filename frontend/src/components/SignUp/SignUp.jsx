import 'bootstrap/dist/css/bootstrap.min.css'
import './signup.css'
import { useState, useRef } from 'react'
import axios from 'axios'
import $ from 'jquery'

function SignUp({ setMessage }) {
    const imageref = useRef(null);
    const [data, setData] = useState({
        image: null
    })

    function handleImageCLick(){
        imageref.current.click()
    }
    function handleImageChange(event){
        const file = event.target.files[0]
        setData(prev => {
            return {
                ...prev,
                image: file
            }
        })
    }
    const handleOnSubmit = (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        data.append("image", data.image)
        axios.post("http://127.0.0.1:8000/api/register/", data,
            {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            })
        .then((response) => {
            console.log(response.data);
            setMessage(() => response.data.success)
            $("div.message").removeClass("hide");
        })
        .catch((response) => {
            setMessage(() => response.response.data.error);
            $("div.message").removeClass("hide");
        })
    } 
    return (
        <>         
            <form onSubmit={handleOnSubmit} id="signup" className="d-flex flex-column" action="">
                {data.image ?
                    <img onClick={handleImageCLick} src={URL.createObjectURL(data.image)} className="profile-image" />: 
                    <img onClick={handleImageCLick} src="default.png" className="profile-image " />
                }
                <input type="email" name="email" placeholder='Введите вашу почту' />
                <input type="text" name="first_name" placeholder='Ваше имя' />
                <input type="text" name="last_name" placeholder='Ваша фамилия'/>
                <input ref={imageref} onChange={handleImageChange} type="file" accept=".png .jpeg .jpg" name="image" style={{display: "none"}} />
                <input type="text" name="password1" placeholder='Придумайте пароль' />
                <input type="text" name="password2" placeholder='Введите придуманный пароль' />
                <button type='sumbit'>Зарегистрироваться</button>
            </form>
        </>
    )
}

export default SignUp