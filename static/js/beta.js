// on sumbit, Post to python and received to the modal window


$(document).ready(function() {
        $("#tradeForm").on('submit', function(event){
        $(".tradeResponse").html("Give me a second. Running analysis.");
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/trade',
            data: {
                trade: $("#tradeText").val(),
                cash: $("#cash").html(),
                total: $("#total").html()
            },
            success: function (result) {
                text = result.resultpopup;
                yara = result.yararesponse;
                portfolio = result.portfoliotable;
                stock = result.stock;
                price = result.price;
                amount = result.amount;
                shares = result.shares;
                cash = result.cash;
                total = result.total;
                dollarchange = result.dollarchange;
                percentchange = result.percentchange;
                sell = result.sell;
                ticker = portfolio[0][0];
                port_price = portfolio[0][1];
                initial_inve_amount = portfolio[0][5];
                cash_port = portfolio[2][0];
                total = portfolio[1][0];
                console.log(portfolio[0]);
                console.log(portfolio[1]);
                console.log(cash_port);
                if (ticker == 'AAPL' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#AAPLstock").html(ticker.bold());
                    $("#AAPLprice").html(price.bold());
                    $("#AAPLdollarchange").html('$622.40'.bold());
                    $("#AAPLpercentchange").html('25.46%'.bold());
                    $("#AAPLshares").html(portfolio[0][4].bold());
                    $("#AAPLpurchase").html('$122.23'.bold());
                    $("#AAPLamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'NKE' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#NKEstock").html(ticker.bold());
                    $("#NKEprice").html(port_price.bold());
                    $("#NKEdollarchange").html('$2,783.10'.bold());
                    $("#NKEpercentchange").html('12.57%'.bold());
                    $("#NKEshares").html(portfolio[0][4].bold());
                    $("#NKEpurchase").html('$92.77'.bold());
                    $("#NKEamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'MSFT' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#MSFTstock").html(ticker.bold());
                    $("#MSFTprice").html(port_price.bold());
                    $("#MSFTdollarchange").html('$1,219.80'.bold());
                    $("#MSFTpercentchange").html('21.30%'.bold());
                    $("#MSFTshares").html(portfolio[0][4].bold());
                    $("#MSFTpurchase").html('$60.99'.bold());
                    $("#MSFTamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'WMT' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#WMTstock").html(ticker.bold());
                    $("#WMTprice").html(port_price.bold());
                    $("#WMTdollarchange").html('$1,718.28'.bold());
                    $("#WMTpercentchange").html('23.95%'.bold());
                    $("#WMTshares").html(portfolio[0][4].bold());
                    $("#WMTpurchase").html('$63.64'.bold());
                    $("#WMTamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else{
                    $("#tradeResponse").html(yara);
                    $("#stock").html(stock.bold());
                    $("#price").html(price.bold());
                    $("#amount").html(amount.bold());
                    $("#shares").html(shares.bold());
                    $("#cash").html(cash.bold());
                    $("#total").html(total.bold());
                    $("#purchase").html(price.bold());
                    $("#dollarchange").html(dollarchange.bold());
                    $("#percentchange").html(percentchange.bold());
                }
                console.log(portfolio);
                if (text != "") {
                    //$('.tradeButton').trigger("click");
                    $('.trade-modal-opener').modal({
                        content: text,
                        confirm: {
                            text: 'Ok',
                            link: ''
                        },
                    });
                }
            }
        });
    });
});
$(document).ready(function() {
    $("#tradeMicForm").on('submit', function(event){
        event.preventDefault();
        $("#tradeText").val("Speak into the microphone!");
        $(".tradeResponse").html("Give me a second after your speak. Running analysis.");
        $.ajax({
            type: 'POST',
            url: '/trade',
            data: {
                trade: $("#tradeText").val(),
                cash: $("#cash").html(),
                total: $("#total").html()
            },
            success: function(result) {
                text = result.resultpopup;
                yara = result.yararesponse;
                portfolio = result.portfoliotable;
                stock = result.stock;
                price = result.price;
                amount = result.amount;
                shares = result.shares;
                cash = result.cash;
                total = result.total;
                dollarchange = result.dollarchange;
                percentchange = result.percentchange;
                sell = result.sell;
                ticker = portfolio[0][0];
                port_price = portfolio[0][1];
                initial_inve_amount = portfolio[0][5];
                cash_port = portfolio[2][0];
                total = portfolio[1][0];
                console.log(portfolio[0]);
                console.log(portfolio[1]);
                console.log(cash_port);
                if (ticker == 'AAPL' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#AAPLstock").html(ticker.bold());
                    $("#AAPLprice").html(price.bold());
                    $("#AAPLdollarchange").html('$622.40'.bold());
                    $("#AAPLpercentchange").html('25.46%'.bold());
                    $("#AAPLshares").html(portfolio[0][4].bold());
                    $("#AAPLpurchase").html('$122.23'.bold());
                    $("#AAPLamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'NKE' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#NKEstock").html(ticker.bold());
                    $("#NKEprice").html(port_price.bold());
                    $("#NKEdollarchange").html('$2,783.10'.bold());
                    $("#NKEpercentchange").html('12.57%'.bold());
                    $("#NKEshares").html(portfolio[0][4].bold());
                    $("#NKEpurchase").html('$92.77'.bold());
                    $("#NKEamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'MSFT' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#MSFTstock").html(ticker.bold());
                    $("#MSFTprice").html(port_price.bold());
                    $("#MSFTdollarchange").html('$1,219.80'.bold());
                    $("#MSFTpercentchange").html('21.30%'.bold());
                    $("#MSFTshares").html(portfolio[0][4].bold());
                    $("#MSFTpurchase").html('$60.99'.bold());
                    $("#MSFTamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else if (ticker == 'WMT' && sell == 'yes') {
                    $("#tradeResponse").html(yara);
                    $("#WMTstock").html(ticker.bold());
                    $("#WMTprice").html(port_price.bold());
                    $("#WMTdollarchange").html('$1,718.28'.bold());
                    $("#WMTpercentchange").html('23.95%'.bold());
                    $("#WMTshares").html(portfolio[0][4].bold());
                    $("#WMTpurchase").html('$63.64'.bold());
                    $("#WMTamount").html(initial_inve_amount.bold());
                    $("#cash").html(cash_port.bold());
                    $("#total").html(total.bold());
                } else{
                    $("#tradeResponse").html(yara);
                    $("#stock").html(stock.bold());
                    $("#price").html(price.bold());
                    $("#amount").html(amount.bold());
                    $("#shares").html(shares.bold());
                    $("#cash").html(cash.bold());
                    $("#total").html(total.bold());
                    $("#purchase").html(price.bold());
                    $("#dollarchange").html(dollarchange.bold());
                    $("#percentchange").html(percentchange.bold());
                }
                console.log(portfolio);
                if (text != "") {
                    $('.trade-modal-opener').trigger("click");
                    $('.trade-modal-opener').modal({
                        content: text,
                        confirm: {
                            text: 'Ok',
                            link: ''
                        }
                    });
                }
            }
        });
    });
});



$(document).ready(function() {
    $("#managementForm").on('submit', function(event){
        event.preventDefault();
        $(".managementResponse").html("Give me a second. Running analysis.");
        $.ajax({
            type: 'POST',
            url: '/management',
            data: {
                management: $("#managementText").val()
            },
            success: function(result) {
                console.log();
                //text = result.resultpopup;
                yara = result.yararesponse;
                //portfolio = result.portfoliotable;
                $(".managementResponse").html(yara);
                }
            });
        });
    });


$(document).ready(function() {
    $("#managementMicForm").on('submit', function(event){
        event.preventDefault();
        $("#managementText").val("Speak into the microphone!");
        $(".managementResponse").html("Give me a second after your speak. Running analysis.");
        $.ajax({
            type: 'POST',
            url: '/management',
            data: {
                management: $("#managementText").val()
            },
            success: function(result) {
                console.log();
                //text = result.resultpopup;
                yara = result.yararesponse;
                //portfolio = result.portfoliotable;
                $(".managementResponse").html(yara);
                }
            });
        });
    });

    // The modal pop up window


    console.log("ready!");
    $.fn.modal = function(opts){
        opts = $.extend({
            // colour: '#0c8',
            class: 'trade-modal',
            title: 'Trade Confirmation',
            content: '',
            extra: '',
            closeCallback: function(){}
        }, opts);

        var modal = this;

        this.openModal = function(){
            var underlay = $('<div />', {
                class: opts.class + '-underlay'
            });

            var overlay = $('<div />', {
                class: opts.class
            }).append(
                $('<h2 />', {
                    class: 'title'
                }).text(opts.title).append(
                    $('<div />', {
                        class: 'closer waves-effect'
                    })
                )
            ).append(
                $('<div />', {
                    class: 'content'
                }).append(opts.content).append(
                    $('<div />', {
                        class: 'extra'
                    }).append(opts.extra)
                )
            );

            $('body').append(underlay);
            $('body').append(overlay);
            $('body').addClass(opts.class + '-active');

            if(opts.confirm){
                overlay.addClass('with-confirm');
                overlay.append(
                    $('<div />', {
                        class: 'confirm-wrapper'
                    }).append(
                        $('<a />', {
                            href: opts.confirm.link,
                            class: 'confirm waves-effect'
                        }).text(opts.confirm.text)
                    )
                );
                overlay.find(' .confirm').on('click', function(){
                    modal.removeModal(opts.closeCallback);
                    return false;
                });
            }

            setTimeout(function(){
                $('.' + opts.class + '-underlay').css({
                    'opacity': '1'
                });
                $('.' + opts.class).addClass('active');
                $('.' + opts.class + '-underlay').on('click', function(){
                    modal.removeModal(opts.closeCallback);
                });
                $('.' + opts.class + ' .closer').on('click', function(){
                    modal.removeModal(opts.closeCallback);
                });
            }, 50);
        }

        this.removeModal = function(callback){
            $('.' + opts.class + '-underlay').css({
                'opacity': '0'
            });
            $('.' + opts.class).removeClass('active');
            setTimeout(function(){
                $('.' + opts.class + '-underlay').remove();
                $('.' + opts.class).remove();
                $('body').removeClass(opts.class + '-active');
            },350);
            callback();
        }

        modal.on('click', function(){
            modal.openModal();
            return false;
        });

        return this;
    }


