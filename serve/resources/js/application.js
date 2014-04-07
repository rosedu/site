$(document).ready(function() {
	$('input').focus(function() {
		if(this.value==this.defaultValue)
			this.value='';
		$(this).css('color','#323232');
	});

	$('input').blur(function() {
		if($.trim(this.value)=='')
			this.value=(this.defaultValue?this.defaultValue:'');
		$(this).css('color','');
	});
});
