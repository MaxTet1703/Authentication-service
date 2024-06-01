import './App.css'
import { Routes, Route, BrowserRouter} from 'react-router-dom'
import Login from './components/SignUp/SignUp.jsx'
import EnterPage from './components/EnterPage/EnterPage.jsx'

function App() {

  return (
    <>
      <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<EnterPage />}/>
          </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
