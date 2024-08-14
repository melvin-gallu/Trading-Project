import { useState, useEffect } from "react";
import useApi from "./FastapiRest";

const Home = () => {

    const item = {'name':'melvin', 'description':'my', 'price':1, 'tax':3.5}
    const user = {'username':'mg', 'full_name':'melvin gallu'}

    const requestedData = {user:user, item:item, importance:3};

    const {data, loading, error, triggerFetch} = useApi('POST','/items',requestedData)
    
    // Use useEffect to trigger the fetch when the component mounts
    useEffect(() => {
        triggerFetch();
    }, []); // Empty dependency array means this runs only on mount

    if (loading) return <p>Loading...</p>
    if (error) {
        console.log(error)

        const errorData = JSON.stringify(error.response.data)
        return (
            <div>
                <p>Error: <b>{error.message}</b></p>
                <p>Details: {errorData}</p>
            </div>
        )
    }

    const dataDisplay = JSON.stringify(data)

    console.log(data)

    return (
        <div className="home">
            <h2>Home Page</h2>
            <p>{dataDisplay}</p>
        </div>
    )
}

export default Home;