$(document).ready(function(){   
    $(".tradeButton").click(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "",
            data: {
                trade: $(".tradeText").val()
            },
            success: function(result) {
                $(".tradeResponse").html(result);
            }
        });
    });
    $(".tradeInputMic").click(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "",
            data: {
                trade: $(".tradeText").val()
            },
            success: function(result) {
                $(".tradeResponse").html(result);
            }
        });
    });
});