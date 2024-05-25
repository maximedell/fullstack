import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import "../styles/Add.css"

function Add() {
    const { type } = useParams()
    const [fields, setFields] = useState([])

    useEffect(() => {
        axios.get(`http://localhost:8000/api/${type}/empty/`)
            .then(response => {
                // Supposons que la réponse contient un objet avec les informations de chaque champ
                setFields(response.data)
            })
    }, [type])

    const renderField = (field, info) => {
        console.log(info.type)
        switch (info.type) {
            case 'CharField':
                return <input type="text" name={field} />
            case 'DateField':
                return <input type="date" name={field} />
            case 'IntegerField':
                return <input type="number" name={field} />
            case 'BooleanField':
                return <input type="checkbox" name={field} />
            case 'FloatField':
                return <input type="number" name={field} step="0.01" />
            case 'FileField':
                return <input type="file" name={field} />
            case 'ForeignKey':
                return (
                    <select name={field}>
                        {info.choices.map(choice => (
                            <option key={choice.value} value={choice.value}>{choice.display_name}</option>
                        ))}
                    </select>
                )
            case 'ChoiceField':
                return (
                    <select name={field}>
                        {info.choices.map(choice => (
                            <option key={choice} value={choice}>{choice}</option>
                        ))}
                    </select>
                )
            // Ajoutez d'autres cas ici pour d'autres types de champs
            default:
                return <input type="text" name={field} />
        }
    }

    return (
        <div className='form'>
            <h1>Ajouter {type}</h1>
            <form>
                {Object.entries(fields).map(([field, info]) => (
                    <div key={field}>
                        <label>{info.verbose_name}</label> {/* Utilisez verbose_name ici */}
                        {renderField(field, info)}
                    </div>
                ))}
                <button type="submit" className='btn_sub'>Ajouter</button>
            </form>
        </div>
    )
}

export default Add