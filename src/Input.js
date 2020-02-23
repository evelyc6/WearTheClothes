import React, {useState} from "react";
import './Input.css';


const Inputs=() =>{
    const [city, setCity] = useState("");
    const [temp, setTemp] = useState("");
    const [top, setTop] = useState("");
    const [bottom, setBottom] = useState("");
    const [outer, setOuter] = useState("");
    const [message, setMessage] = useState("");

    function handleChange(e){
        // console.log(e)
        setCity(e.target.value)
    }
    function handleSubmit(cityName){
        // e.preventDefault();
        // setCity(cityName);
        var url = 'http://localhost:5000/?city='+ city
        console.log(city); //print statements
        fetch(url)
        .then(res=>{
            return res.json();
        })
        .then((myJson)=>{
            console.log(myJson)
            setTemp(myJson["Temperature"])
            console.log(myJson["Temperature"])
            setTop(myJson["clothes"][0])
            setBottom(myJson["clothes"][1])
            setOuter(myJson["clothes"][2])
            setMessage(myJson["clothes"][3])
            document.getElementById('column1').style.opacity = 0.8;
        })
        
    
    }

    function keypressed(event){
        // e.preventDefault();
        // setCity(cityName);
        if (event.key === "Enter")
        {
            handleSubmit();
        }
    
    }


    return(
        <div>
            <div className="SubmitText">
                <input className = "textBox" placeholder="Input a City" onKeyPress={keypressed} type="text" name="city" onChange={(e) => handleChange(e)}></input>
                <button className = "buttonInfo"  onClick={handleSubmit}>Submit</button>
            </div>
            {true && <div id = "column1">
              
               <div className= "topTitle">
                    {temp === ""? "" :city}
                </div>  
                <p>{temp===""?"": "Temperature: "+ temp+ " °F"} </p>
                <p>{top === ""? "": "Top: "+ top}</p>
                <p>{bottom===""? "":"Bottom: " +bottom }</p>
                <p>{outer==="" ? "" :"Outerwear: " + outer}</p>
                <p className = "message">{message === "" ? "" : "Message: " + message}</p>
                
            </div>}
        </div>
    );

}
export default Inputs;