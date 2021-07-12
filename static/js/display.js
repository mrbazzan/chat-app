
let value = document.getElementById('room_details').textContent;

$(document).ready(function(){

    setInterval(function(){
        $.ajax({
            type: 'GET',
            url : `/getMessages/${value}`,
            success: function(response){
                console.log(response);
                $("#display").empty();
                for (let key in response.messages)
                {
                    let temp="<div class='container darker'><b>"+response.messages[key].user+"</b><p>"+response.messages[key].user_message+"</p><span class='time-left'>"+response.messages[key].date+"</span></div>";
                    $("#display").append(temp);
                }
            },
            error: function(response){
                alert(`/getMessages/${room_details_id}`)
                alert('An error occured')
            }
        });
    },1000);
    })
