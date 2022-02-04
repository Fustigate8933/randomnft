import React from "react"
import { BrowserRouter, Route, Routes } from "react-router-dom"
import Home from "./Home"
import Images from "./Images"

export default function App(){
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/images/" element={<Images />} />
            </Routes>
        </BrowserRouter>
    )
}
