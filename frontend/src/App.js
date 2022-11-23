import React, {useState, useEffect} from 'react'
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from './index.js';


function App() {
  var errorMessage = <hN></hN>
  const init = {
    keyword:'',
    interval:'',
    startDate:'',
    endDate:'',
    numBooks:'',
    extraWords:'',
    analysisType:'',
    language:''

  

  };

  const [values, setValues] = useState(init);
  
  const handleChange = (e) => {   
    console.log("v")             
    setValues({
      ...values,                                // spreading the unchanged values
      [e.target.name]: e.target.value,          // changing the state of *changed value*
    });
  };

  const sendData = (e) => {
    e.preventDefault()
    const requestOptions = {
      
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
   
      body: JSON.stringify(values)
  };
  fetch('http://127.0.0.1:5000/result', requestOptions).
  then((response) => 
    response.json()).then((result) => 
{
      console.log(result['response'])
      if (result['response']!=='Redirecting to the loading page...'){
        document.getElementById("errorMessage").innerHTML ="Please input all of the required fields."
       
    }
    else{
      console.log('e')
    }
  })
    
    //console.log(result['response']))
};
  
//   
//})
   
  





  //React.render(element);

  
return (
  <form action="/">
      
      
      
    <h1 > (Required) Enter keyword(s) (Separate by spaces)</h1>
<input type="text" name="keyword" id="content" onChange={handleChange}
        ></input>
<form action="/" >
    <h1  > (Required) Enter interval</h1>
<input type="text" name="interval" id="content" onChange={handleChange}
        ></input>
</form>
<form action="/">
    <h1 > (Required) Enter start date</h1>
<input type="text" name="startDate" id="content" onChange={handleChange}
        ></input>
</form>
<form action="/" >
    <h1 > (Required) Enter end date</h1>
<input type="text" name="endDate" id="content" onChange={handleChange}
      ></input>
</form>
<form action="/">
    <h1> (Required) Enter # of books</h1>
<input type="text" name="numBooks" id="content" onChange={handleChange}></input>
</form>
<form action="/" >
    <h1> (Optional) Enter extra keywords </h1>
<input type="text" name="extraWords" id="content" onChange={handleChange}></input>
</form>
<form action="/" >
    <h1> (Optional) Enter analysis type (m-magazines, n-newspapers, b-books)</h1>
<input type="text" name="analysisType" id="content" onChange={handleChange}></input>
</form>
<form action="/" >
    <h1> (Optional) Enter language </h1>
<input type="text" name="language" id="content" onChange={handleChange}></input>
</form>

<input type="Submit" value = "send form" name="analysisType" id="content" onClick={sendData}></input>
<h1 id='errorMessage' style={{color:'red'}}> </h1>
<h1>Submitted Values</h1>
      <div>
    {
      Object.keys(values).map((key, index) =>  
        <p key={index}>{key}:{values[key]}</p> 
      )
    }
  </div>
</form>)
}

// Makes our app component visible in other modules.
export default App;
