import '../styles/Sidebar.css';
import SidebarSection from './SidebarSection';

function Sidebar() {
    const childrenList = [
        {
            title: 'Recettes',
            icon: 'brunch_dining',
            childrenList: [
                { title: 'Liste', to: '/list/recipes' },
                { title: 'Ajouter', to: '/add/recipes' },
            ]
        },
        {
            title: 'Ingrédients',
            icon: "grocery",
            childrenList: [
                { title: 'Liste', to: '/list/ingredients' },
                { title: 'Ajouter', to: '/add/ingredients' },
            ]
        },
        {
            title: 'Production',
            icon: "skillet",
            childrenList: [
                { title: 'Liste', to: '/list/productions' },
                { title: 'Ajouter', to: '/add/productions' },
            ],
        }
    ];
    return (
        <div className="sidebar">
            {childrenList.map((child, index) => (
                <SidebarSection key={index} title={child.title} icon={child.icon} childrenList={child.childrenList} />
            ))}
        </div>
    );
}

export default Sidebar;