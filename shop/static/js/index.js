$('#ChangeForm').on('submit',function(event){
event.preventDefault();
var data = $( this ).serialize();
$.post('/change/user/',data,function(response){
$('#user').html(response)
});

});