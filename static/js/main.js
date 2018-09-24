$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();
		$.getJSON(			
			//url
			'/_get_json',				
			//data
			{question: userInput},  	
			//func
			function (data) {			

				if (typeof data.failure_msg !== 'undefined') {	
					$("#gmapresult").text(data.failure_msg)
				}

				else {
				$("#gmapresult").text(data.message1);
				$("#wikireuslt").text(data.message2);
				}
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
