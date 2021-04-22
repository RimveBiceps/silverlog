// animate fa fa-heart on click
$(document).on('click', '.like', function () {
	this.children[0].style.color = "#66c144";
	this.getElementsByTagName('I')[0].classList.toggle('fa-spin');
});
// Ajax post method on click for adding company to favorites
$(document).ready(function(){
    $(".like").click(function(){		
        var acr = $("#id_company_title").val();
        var data = {
            'company_symbol': acr
            };

        $.ajax(
			{
				type: 'POST',
                url: '../favorite/',
                data: data,
                success: function(json) {
					alert(json); // your actions after save, you can just pop-up some ui element that added to wishlist
				}
			})
    });
});
