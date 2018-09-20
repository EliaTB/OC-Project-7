$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();
		$.getJSON(
			'/_get_json',				//url                     
			{question: userInput},  	//data

			function (data) {
				$("#gmapresult").text(data.address);
				$("#wikireuslt").text(data.wiki_summary);
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
