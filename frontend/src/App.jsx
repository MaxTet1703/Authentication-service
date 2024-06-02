import './App.css'
import { Routes, Route, BrowserRouter} from 'react-router-dom'
import EnterPage from './components/EnterPage/EnterPage.jsx'
import UserInfo from './components/UserInfo/UserInfo.jsx'
import { createContext } from 'react'
import { useState } from 'react'

export const UserContext = createContext()

function App() {

  const [user, setUser] = useState({
    signed_in: false,
    email: '',
    first_name: '',
    last_name: '',
    image: null
  })

  return (
    <>
      <UserContext.Provider value={[user, setUser]}>
        <BrowserRouter>
            <Routes>
              <Route exact path="/" element={user.signed_in ? <UserInfo/>: <EnterPage />}/>
            </Routes>
        </BrowserRouter>
      </UserContext.Provider>
    </>
  )
}

export default App
