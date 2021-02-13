
function changeStatus(){
    fetch("https://exceed16.cpsk-club.xyz/status?slot=1")
    .then(data => data.json())
    .then(data => console.log(data));
    let slot = 1
    let num = data.result['status']
    if (slot === 0){
        if (num === 1){
            document.getElementById("ava1").innerHTML = "Time";
            document.getElementById("time1").innerHTML = "X";
            document.getElementById("car1").style.background = "red";
            
        }

        else{
            document.getElementById("ava1").innerHTML = "Available";
            document.getElementById("time1").innerHTML = "";
            document.getElementById("car1").style.background = "green";
        }
    }

    else if (slot == 1){
        if (num == 1){
            document.getElementById("ava2").innerHTML = "Time";
            document.getElementById("time2").innerHTML = "X";
            document.getElementById("car2").style.background = "red";
            
        }

        else{
            document.getElementById("ava2").innerHTML = "Available";
            document.getElementById("time2").innerHTML = "";
            document.getElementById("car2").style.background = "green";
        }
    }

    else if (slot == 2){
        if (num == 1){
            document.getElementById("ava3").innerHTML = "Time";
            document.getElementById("time3").innerHTML = "X";
            document.getElementById("car3").style.background = "red";
            
        }

        else{
            document.getElementById("ava3").innerHTML = "Available";
            document.getElementById("time3").innerHTML = "";
            document.getElementById("car3").style.background = "green";
        }
    }

    else if (slot == 3){
        if (num == 1){
            document.getElementById("ava4").innerHTML = "Time";
            document.getElementById("time4").innerHTML = "X";
            document.getElementById("car4").style.background = "red";
            
        }

        else{
            document.getElementById("ava4").innerHTML = "Available";
            document.getElementById("time4").innerHTML = "";
            document.getElementById("car4").style.background = "green";
        }
    }
}

changeStatus();