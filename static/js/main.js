$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();

		if (userInput == "") {
			$("#gmapresult").text("Grandpy: Vous n'avez rien mis dans la barre de recherche!");
			$("#map").css({display:"none"});
			$("#wikireuslt").css({display:"none"});
		}
		else {
			$.getJSON(			
				//url
				'/_get_json',				
				//data
				{question: userInput},  	
				//func
				function (data) {							

					if (data.error) {
						addGPyMess(data.message1)

					}
					else {
						addMesg(data.message1)
						addMesg(data.message2, data.url)

						var lat = (data.lat);
						var lng = (data.lng);

	                	initMap(lat, lng);
	                	$("#map").css({display:"block"});				
					}
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

function addMesg(message, url=null){
	var grandpyElt = document.createElement("strong");
	grandpyElt.appendChild(document.createTextNode('Grandpy: '));

	var messageElt = document.createElement("p");
	messageElt.appendChild(grandpyElt);
	messageElt.appendChild(document.createTextNode(message));
	

    div = document.createElement('div');
    div.classList.add("box");
    div.appendChild(messageElt);

	if (url !== null) {
		var urlElt = document.createElement("a");
		urlElt.href = url;
		urlElt.appendChild(document.createTextNode("En savoir plus"));

		messageElt.appendChild(urlElt)
	}

    $("#grandpyanswer").append(div);
}