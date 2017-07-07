function mt(name,domain,subject,body){
  var addBody = '?';
  if(subject != ""){
	addBody += 'subject='+subject;
	addBody += '&';
  }
  if(body != "") addBody += 'body='+body;
  location.href = "mailto:"+name+"@"+domain+addBody;
}
$(document).ready(function(){
  var cache = {},
  lastXhr;
  var cache2 = {},
  lastXhr2;
  $("#quickStadt").autocomplete({
	minLength: 2,
	source: function( request, response ) {
	  var term = request.term;
	  if ( term in cache ) {
		response( cache[ term ] );
		return;
	  }
	  request.act = 'getStadt';

	  lastXhr = $.getJSON( "/tpl/QuickSearch.php", request, function( data, status, xhr ) {
		cache[ term ] = data;
		if ( xhr === lastXhr ) {
		  response( data );
		}
	  });
	}
  });
  $('.multiSelValue').hide();
  $('.multiSelect,.multisel,.addremove').show();
  $("#quickStelle").autocomplete({
	minLength: 2,
	source: function( request, response ) {
	  var term = request.term;
	  if ( term in cache2 ) {
		response( cache2[ term ] );
		return;
	  }
	  request.act = 'getStelle';

	  lastXhr2 = $.getJSON( "/tpl/QuickSearch.php", request, function( data, status, xhr ) {
		cache2[ term ] = data;
		if ( xhr === lastXhr2 ) {
		  response( data );
		}
	  });
	}
  });
  if($('#print').length > 0){
	$('#print').html('<a href="javascript:window.print()">Drucken</a>');
  }
	
  $('form').find('.multisel').change(function(){
	var name = $(this).attr('name').substring(0,$(this).attr('name').length-3),
	match = $('[name=\''+name+'\']').val().match(','+$(this).val()+',');
	if(match)
	  $('[name=\''+name+'but\']').val('-');
	else
	  $('[name=\''+name+'but\']').val('+');

  });
  $('form').find('.addremove').click(function(){
	var name = $(this).attr('name').substring(0,$(this).attr('name').length-3),
	eltxt = $('[name=\''+name+'txt\']'),
	el = $('[name=\''+name+'\']'),
	sel1 = $('[name=\''+name+'sel\']').val(),
	sel2 = $('[name=\''+name+'sel\'] :selected').text(),
	add;

	if($(this).val() == '-'){
	  el.val(el.val().replace(','+sel1+',', ''));
	  if(el.val().substr(-1) != ',') el.val(el.val()+',');
	  if(el.val().substr(0,1) != ',') el.val(','+el.val());
	  el.val(el.val().replace(',,', ''));

	  eltxt.val(eltxt.val().replace(sel2, ''));
	  eltxt.val(eltxt.val().replace(',,', ''));
	  if(eltxt.val().substr(0,1) == ',') eltxt.val(eltxt.val().substring(1));
	  if(eltxt.val().substr(-1) == ',') eltxt.val(eltxt.val().substring(0,eltxt.val().length-1));
	}else{
	  add = '';
	  if(el.val() == '')el.val(',');
	  if(eltxt.val() != '')add = ',';
	  el.val(el.val()+sel1+',');
	  eltxt.val(eltxt.val()+add+sel2);
	}
	$(this).parent().find('.multisel').trigger('change');
  });
});

function printpr()
{
  var OLECMDID = 7;
  /* OLECMDID values:
  * 6 – print
  * 7 – print preview
  * 1 – open window
  * 4 – Save As
  */

  var PROMPT = 1; // 2 DONTPROMPTUSER
  var WebBrowser = '<OBJECT ID="WebBrowser1"WIDTH=0 HEIGHT=0 CLASSID="CLSID:8856F961-340A-11D0-A96B-00C04FD705A2"></OBJECT>';
  document.body.insertAdjacentHTML('beforeEnd', WebBrowser);

  WebBrowser1.ExecWB(OLECMDID, PROMPT);
  WebBrowser1.outerHTML = "";
}
