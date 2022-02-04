import { Button, Typography, Select, FormControl, InputLabel, MenuItem } from "@material-ui/core"
import React, { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Home(){
    const [market, setMarket] = useState("")
    const imgs = []

    function fetchImgs(){
        console.log("Fetching imgs...")
        fetch("/api/list/")
        .then(response => response.json())
        .then(data => {
            data.map((item, index) => {
                imgs.push(item.src)
            })
            console.log(imgs)
        })
    }

    function handlePress(event){
        event.preventDefault()

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
            console.log(data)
            fetchImgs()
            handleNavigate()
        })
    }

    function handleNavigate(){
        let navigate = useNavigate()
        navigate({pathname: "/images/", state: { src: imgs }})
    }

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
