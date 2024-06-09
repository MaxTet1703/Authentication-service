import 'bootstrap/dist/css/bootstrap.min.css'
import './userinfo.css'
import axios from 'axios'
import $ from 'jquery'
import { Oval } from 'react-loader-spinner'

import { useContext, useEffect } from 'react'
import { UserContext } from '../../App'


function UserInfo(){
    const [user, setUser] = useContext(UserContext)

    const logoutHandling = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/api/logout/", {
            "refresh": localStorage.getItem("refreshToken"),
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("accessToken")}`,
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json; charset=utf-8"
            }
        })
        .then(() => {
            setUser(() => {
                return(
                    {
                        signed_in: false,
                        email: '',
                        first_name: '',
                        last_name: '',
                        image: null
                    }
                )
            })
        })
    }

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/user/info/", {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("accessToken")}`,
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json; charset=utf-8"
            }
        })
        .then((response) => {
            console.log(response.data)
            setUser((prev) => {
                return (
                    {
                        ...prev,
                        email: response.data.email,
                        first_name: response.data.first_name,
                        last_name: response.data.last_name,
                        image: response.data.image
                    }
                )
            })
            $(".loading").addClass("d-none");
            $(".user-info").removeClass("d-none");
        })
        .catch((response) => {
            console.log(response.response)
        }) 
    }, [])
    return(
        <>
            <div className="user-info-container d-flex">
                <div className="loading d-flex justify-content-center align-items-center">
                <Oval
                    visible={true}
                    height="80"
                    width="80"
                    color="#4fa94d"
                    ariaLabel="oval-loading"
                    wrapperStyle={{}}
                    wrapperClass=""/>
                </div>
                <div className="user-info d-flex justify-content-center align-items-center flex-column d-none">
                    <img className="user-image" src={user.image} alt="" />
                    <p className="full-name">{user.first_name} {user.last_name}</p>
                    <p className="email">{user.email}</p>
                    <button className='logout' onClick={logoutHandling}>Выйти</button>
                </div>
            </div>
            
        </>
    )
}

export default UserInfo