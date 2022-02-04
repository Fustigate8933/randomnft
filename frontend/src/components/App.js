import { Button, Typography, Select, FormControl, InputLabel, MenuItem } from "@material-ui/core"
import React, { useState } from "react"
import {BrowserRouter as Router, Route, Routes, useNavigate} from "react-router-dom"
import Images from "./Images"

export default function App(){
    const [market, setMarket] = useState("")
    const [imgs, setImgs] = useState([])

    function handlePress(){
        const payload = {
			method: "post",
			headers: {"Content-Type": "application/json"},
			body: JSON.stringify({
				market: market
			})
		}

        fetch("/api/search/", payload)
        .then(response => response.json())
        .then(data => {
            setImgs(data)
            console.log(data)
            const navigate = useNavigate()
            navigate("/images/")
        })
    }

    function renderHome(){
        return(
            <div>
                <Typography id="dropdown-title">Choose your marketplace!</Typography>
                <FormControl color="secondary" variant="outlined" style={{minWidth: 300}}>
                    <InputLabel>Market</InputLabel>
                    <Select
                        value={market}  
                        label="Market"
                        onChange={event => setMarket(event.target.value)}
                    >
                        <MenuItem value="OpenSea">OpenSea</MenuItem>
                        <MenuItem value="Nifty Gateway">Nifty Gateway</MenuItem>
                        <MenuItem value="Rarible">Rarible</MenuItem>
                    </Select>
                </FormControl>
                <Button id="go-button" onClick={handlePress} variant="outlined" color="primary">Go!</Button>
            </div>    
        )
    }

    return(
        <div>
            <Router>
                <Routes>
                    <Route path="/">{renderHome()}</Route>
                    <Route path="/images/" component={Images} imgs={imgs} />
                </Routes>
            </Router>
        </div>
    )
}
