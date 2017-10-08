$(document).ready(function() {
	$("#submit").click(function() {
      var text = $("#input").val();
	  $.ajax({
			url: 'http://localhost:3000/punny', 
			type : 'POST',
			contentType: 'application/json',
	    data: JSON.stringify({
	    	key: text
	    }),
	     success: function(res){
	       console.log("success!", res['res']['response'][0]['phrase']);
	      	
	       $("#test").text(res['res']['response'][0]['phrase']);
	     }
	      
		})
	})
})