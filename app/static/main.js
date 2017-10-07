$(document).ready(function() {
	$("#submit").click(function() {
		axios.post('/', {
			name: $("#input").val()
		})
		.then(function(response) {
			console.log(response);
		})
		.catch(function(error) {
			console.log(error);
		});
	})
})