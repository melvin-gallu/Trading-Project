import { useState, useEffect } from "react";
import useApi from "./FastapiRest.js";

const Home = () => {
    const { data, loading, error } = useApi('GET','/test','check');

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: <b>{error.message}</b></p>;

    const dataString = JSON.stringify(data, null, 2);

    console.log(data)

    return (
        <div className="home">
            <h2>Home Page</h2>
            <br />
            <p>{data.message.test}</p>
            <p>{data.message.test2}</p>
        </div>
    )
}

export default Home;