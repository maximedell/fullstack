import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import '../styles/List.css';

function List() {
    const { type } = useParams();
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [search, setSearch] = useState(''); // Ajout d'un state pour la recherche

    useEffect(() => {
        const fetchItems = async () => {
            try {
                setLoading(true);
                const response = await axios.get(`http://localhost:8000/api/${type}/`); // Modifier l'URL en fonction de votre API
                setItems(response.data);
            } catch (error) {
                setError(error);
                console.error('Error fetching data: ', error);
            } finally {
                setLoading(false);
            }
        };

        fetchItems();
    }, [type]);

    // Fonction pour gérer le changement de l'input de recherche
    const handleSearchChange = (event) => {
        setSearch(event.target.value);
    };

    // Filtrer les items en fonction de la recherche
    const filteredItems = items.filter(item =>
        Object.values(item).some(val =>
            String(val).toLowerCase().includes(search.toLowerCase())
        )
    );

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div className='list-div'>
            <h1>{type.charAt(0).toUpperCase() + type.slice(1)} List</h1>
            <input
                type='text'
                placeholder='Search...'
                className='searchbar'
                value={search}
                onChange={handleSearchChange} // Ajout d'un gestionnaire d'événements pour le changement de l'input
            />
            <table className='list'>
                <thead>
                    <tr className='list-header'>
                        {Object.keys(items[0])
                            .slice(0, 5)
                            .map((key) => (
                                <th>{key}</th>
                            ))
                        }
                    </tr>
                </thead>
                <tbody>
                    {filteredItems.map((item) => ( // Utiliser les items filtrés ici
                        <tr key={item.id} className='list-row'>
                            {Object.entries(item)
                                .slice(0, 5)
                                .map(([key, value]) => (
                                    <td className='list-cell'>{value}</td>
                                ))
                            }
                        </tr>
                    ))}
                </tbody>
            </table>
        </div >
    );
}

export default List;