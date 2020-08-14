$( document ).ready(function() {
    var pathname = window.location.pathname;
    var nav_items =  $(".sidebar-sticky .nav-link");
    for(var i=0;i<nav_items.length;++i){
        $(nav_items).removeClass("active");
    }
    if(pathname.startsWith("/invoice/")){
        pathname = pathname.substring(9);
        if(pathname.indexOf("invoice")>=0){
            $(nav_items[1]).addClass("active");
        }else{
            $(nav_items[0]).addClass("active");
        }
    }

    $("#createCustomer").click(function(){
        window.location.href = "/invoice/customer/new";
    });

    $("#createInvoice").click(function(){
        window.location.href = "/invoice/create-invoice";
    });

});