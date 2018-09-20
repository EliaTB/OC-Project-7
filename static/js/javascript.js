$(function() {
	$('#submit').on('click', function() {
		var userInput = $('input[name="question"]').val();
		$.getJSON(
			'/_get_json',				//url                     
			{question: userInput},  	//data

			function () {
				$("#gmapresult").text(address);
				$("#wikireuslt").text(wiki_summary);
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
