$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();
		if (userInput == "") {
			addGranpyMsg("Vous n'avez rien mis dans la barre de recherche!");
			$("#map").css({display:"none"});
		}
		else {
			addUserMsg(userInput);
			$(".loader").css({display:"block"})	
					
			$.getJSON(			
				//url
				'/_get_json',				
				//data
				{question: userInput},  	
				//func
				function (data) {							

					if (data.error) {
						addGranpyMsg(data.message1);
						$("#map").css({display:"none"});
					}
					else {
						addGranpyMsg(data.message1)
						addGranpyMsg(data.message2, data.url)

						var lat = (data.lat);
						var lng = (data.lng);

	                	initMap(lat, lng);
	                	$("#map").css({display:"block"});				
					}
					$(".loader").css({display:"none"});
				}
			);
		}
	});		
});
				

function initMap(lat, lng) {

	var pos = {lat: parseFloat(lat), lng: parseFloat(lng)};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: pos
    });

    var marker = new google.maps.Marker({
        position: pos,
        map: map
    });
}

function addGranpyMsg(message, url=null){
	var grandpyElt = document.createElement("strong");
	grandpyElt.appendChild(document.createTextNode('Grandpy: '));

	var messageElt = document.createElement("p");
	messageElt.appendChild(grandpyElt);
	messageElt.appendChild(document.createTextNode(message));
	

    div = document.createElement('div');
    div.classList.add("msg");
    div.appendChild(messageElt);

	if (url !== null) {
		var urlElt = document.createElement("a");
		urlElt.href = url;
		urlElt.appendChild(document.createTextNode("En savoir plus"));

		messageElt.appendChild(urlElt)
	}

    document.getElementById("grandpyanswer").append(div);
}

function addUserMsg(message) {
	var userElt = document.createElement("strong");
	userElt.appendChild(document.createTextNode('User: '));

	var messageElt = document.createElement("p");
	messageElt.appendChild(userElt);
	messageElt.appendChild(document.createTextNode(message));

	div = document.createElement('div');
    div.classList.add("msg", "darker");
    div.appendChild(messageElt);

    document.getElementById("grandpyanswer").append(div);
}