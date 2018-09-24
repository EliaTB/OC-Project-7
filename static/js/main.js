$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();
		$.getJSON(
			'/_get_json',				//url 

			{question: userInput},  	//data

			function (data) {			//func
				$("#gmapresult").text(data.message1);
				$("#wikireuslt").text(data.message2);
			}
		);
	});		
});



// $(function() {
// 	$('#submit').on('click', function() {
// 		$("#gmapresult").text("test");
// 		$("#wikireuslt").text("second test");

// 	});
// });
