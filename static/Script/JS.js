let backdrop=document.getElementById("backdrop");
let cont7=document.getElementById("container7");
let cont73=document.getElementById("container73");




function Toggle_Backdrop()
{
  backdrop.classList.toggle("visible");
};

function Toggle_LoginForm()
{
  cont7.classList.toggle("visible");
  Toggle_Backdrop();
};

function Toggle_adminForm()
{
  cont73.classList.toggle("visible");
  Toggle_Backdrop();
};


// js file for weather fetching


const temperature = document.querySelector(".temperature p");
const loc = document.querySelector(".location p")


const weather={};
const key = "41b060f3fbabc4c45cf464bc48b2bcc8";

if ('geolocation' in navigator){
    navigator.geolocation.getCurrentPosition(setPosition);
}else{
    alert("Browser doesn't Support Geolocation");
}

function setPosition(position){
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;
    
    getWeather(latitude, longitude);

}


function getWeather(latitude, longitude){
    let api = `http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${key}`;
    console.log(api)
    
    fetch(api)
        .then(function(response){
            console.log(response)
            let data = response.json();
            console.log(data);
            return data;
            
        })
        .then(function(data){
            weather.temperature = Math.floor(data.main.temp-273);
            
            weather.city = data.name;
        })
        .then(function(){
            displayWeather();
        });
}

// DISPLAY WEATHER TO UI
function displayWeather(){
  
    temperature.innerHTML = `${weather.temperature}°C`;
    loc.innerHTML = `${weather.city}`;
}



