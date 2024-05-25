import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/SidebarSubsection.css';

function SidebarSubsection({ title, to }) {
    return (
        <div className="sidebar-subsection">
            <Link to={to}>
                <span className='material-symbols-outlined'>subdirectory_arrow_right</span>
                {title}
            </Link>
        </div>
    );
}

export default SidebarSubsection;