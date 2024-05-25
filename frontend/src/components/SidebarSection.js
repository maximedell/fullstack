import React, { useState } from 'react';
import SidebarSubsection from './SidebarSubsection';
import '../styles/SidebarSection.css';

function SidebarSection({ title, icon, childrenList }) {
    const [isOpen, setIsOpen] = useState(false);

    const toggleSubsection = (e) => {
        e.preventDefault();
        setIsOpen(!isOpen);
    };

    return (
        <div className="sidebar-section">
            <button onClick={toggleSubsection} className='sidebar-section-title'>
                {title}
                <span className='material-symbols-outlined'>{icon}</span>
            </button>
            <div className={`sidebar-section-children ${isOpen ? '' : 'hidden'}`}>
                {childrenList.map((child, index) => (
                    <SidebarSubsection key={index} title={child.title} to={child.to} />
                ))}
            </div>
        </div>
    );
}

export default SidebarSection;