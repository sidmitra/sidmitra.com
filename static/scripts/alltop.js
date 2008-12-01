document.addEvent('click', function(e){
	if ($('ack-box')) $('ack-box').removeClass('show-urls');
	if ($('cat-box')) $('cat-box').removeClass('show-urls');
});

window.addEvent('domready', function(){
	$$('ul#cat-box li.categories a').each(function(el){
		el.addEvent('click', function(e){
			new Event(e).stop();
			$('cat-box').toggleClass('show-urls');
		});
	});

	$$('ul#ack-box li.categories a').each(function(el){
		el.addEvent('click', function(e){
			new Event(e).stop();
			$('ack-box').toggleClass('show-urls');
		});
	});
});