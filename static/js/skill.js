$(document).ready(function(){

    // Add new element
    $(".add3").click(function(){

        // Finding total number of elements added
        var total_element = $(".element3").length;
                    
        // last <div> with element class id
        var lastid = $(".element3:last").attr("id");
        var split_id = lastid.split("_");
        var nextindex = Number(split_id[1]) + 1;

        var max = 10;
        // Check total number elements
        if(total_element < max ){
            // Adding new div container after last occurance of element class
            $(".element3:last").after("<div class='element3' id='div3_"+ nextindex +"'></div>");
                        
            // Adding element to <div>
            $("#div3_" + nextindex).append("<input type='text' size=50 placeholder='Enter skill' id='txt3_"+ nextindex +"' >&nbsp;<span id='remove3_" + nextindex + "' class='remove3'>X</span>");
                    
        }
                    
    });

    // Remove element
    $('.container').on('click','.remove3',function(){
                
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        // Remove <div> with id
        $("#div3_" + deleteindex).remove();
    });                
});