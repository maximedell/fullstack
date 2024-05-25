import Nav from './Nav'
import logo from '../assets/logo.png'
import '../styles/Banner.css'
import { Link } from 'react-router-dom';

function Banner() {
    return <div className='header'>
        <Link to='/' className='home-link'>
            <img src={logo} alt="MK" className='mk-logo' />
        </Link>
        <Nav />
    </div>
}

export default Banner