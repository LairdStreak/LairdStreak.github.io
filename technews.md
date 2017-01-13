---
title: Some Tech News
layout: page
---
<script src="{{ site.url }}/assets/jquery-3.1.1.min.js"></script>
<script>
$(function(){

  //debugger;
  //alert('here')
  // Assign handlers immediately after making the request,
// and remember the jqxhr object for this request
var jqxhr = $.getJSON("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty", function(data) {
  console.log( "success" );
})
  .fail(function() {
    console.log( "error" );
  })
  .always(function() {
    console.log( "complete" );
  });
 
// Perform other work here ...
 
// Set another completion function for the request above
jqxhr.done(function(data) {

  var subset = data.slice(0,20);
  //console.log( data );
  $.each(subset,function(index,item){
    //console.log(item);
    pullData(item)
  })
});
})


function pullData(item){
  var uri = "https://hacker-news.firebaseio.com/v0/item/" + item + ".json"; 
  var jqfetch = $.getJSON(uri, function(data){  }).done(function(data){
    //console.log(data.url)
    $("#newstable").append('<tr><td><a href=' + data.url + ' target=_blank>' + data.title + '</a></td></tr>');
  })
}
</script>
<div style="background-color: #cccccc">news.ycombinator Current top 20.</div>
<table id="newstable">
</table> 