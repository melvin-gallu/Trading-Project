import { useState } from "react";
import useApi from "./FastapiRest";

const Home = () => {

    const item = {'name':'Melvin', 'description':'my name', 'price':10, 'tax':3.5}
    const {data, loading, error} = useApi('POST','/items',item)

    if (loading) return <p>Loading...</p>
    if (error) {
        console.log(error)
        return (
            <div>
                <p>Error: <b>{error.message}</b></p>
                <p>Status: {error.response.statusText}</p>
            </div>
        )
    }

    if (!data) return <p>Nothing</p>

    const dataDisplay = JSON.stringify(data)

    return (
        <div className="home">
            <h2>Home Page</h2>
            <p>{dataDisplay}</p>
        </div>
    )
}

export default Home;