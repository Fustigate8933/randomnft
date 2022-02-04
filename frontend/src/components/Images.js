import React from "react"

export default function Images(props){
    return(
        <div>
            {
                props.imgs.map((item, index) => {
                    <img key={index} src={item} />
                })
            }
            <h1>test</h1>
        </div>
    )
}
