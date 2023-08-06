var lat = document.getElementById("").innerHTML
var lon = document.getElementById("").innerHTML
fetch("https://api.openweathermap.org/data/3.0/onecall?lat=16.2359&lon=80.0496&exclude=current&appid=d5cc48f0306399b91909f485463d9bac").then((data)=>{
    console.log(data);
})
