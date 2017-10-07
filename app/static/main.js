$(document).ready(function() {
	$("#submit").click(function() {
      var text = $("#input").val();
	  $.ajax({url: 'http://localhost:5000/test', 
	    type : 'POST',
	    data: {
	    	key: text
	    },
	     success: function(res){
	       console.log("success!", res.key);
	      	
	       $("#test").text(res.key[0]);
	     }
	      
		})
	})
})