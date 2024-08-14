import React from "react";
import Home from "./Home";
import Form from "./Form";
import Navbar from "./Navbar";

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Navbar />
                <div className="content">
                <Routes>
                    <Route path='/' element={<Home />}></Route>
                    <Route path='/form' element={<Form />}></Route>
                </Routes>
                </div>
            </div>
        </BrowserRouter>
    );
}

export default App;