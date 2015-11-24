
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("../static/img/backgrounds/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    /*
        Form validation
    */
    $('.form input[type="text"], .form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="email"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
    
    
});
