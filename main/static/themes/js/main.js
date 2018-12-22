
	$(document).ready(function() { 

        $("#center").center();
      
        var splash_screen = $.cookie('splash'); 

        if (splash_screen == 1){
            $("#overlay").hide();
        }
          
        $("#overlay").click(function(){
            $.cookie('splash', '1');
            $("#overlay").fadeOut(1500);
        });

        $('#promotions-wrapper').cycle({ 
            timeout: 5000, 
            speed: 1000,
            pager:  '#promotions-pagination-inner'
        });

        $('#mobile-toggle').click(function(event){
            event.preventDefault();
            $('body').toggleClass('shownav');
        });

	});

