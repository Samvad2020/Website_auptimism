$(document).ready(function(){

    // Add new element
    $(".add2").click(function(){

        // Finding total number of elements added
        var total_element = $(".element2").length;
                    
        // last <div> with element class id
        var lastid = $(".element2:last").attr("id");
        var split_id = lastid.split("_");
        var nextindex = Number(split_id[1]) + 1;

        var max = 10;
        // Check total number elements
        if(total_element < max ){
            // Adding new div container after last occurance of element class
            $(".element2:last").after("<div class='element2' id='div2_"+ nextindex +"'></div>");
                        
            // Adding element to <div>
            $("#div2_" + nextindex).append("<input type='text' size=50 placeholder='Enter Instructions' name='inst_"+ nextindex +"' id='txt2_"+ nextindex +"' >&nbsp;<span id='remove2_" + nextindex + "' class='remove2'>X</span>");
                    
        }
                    
    });

    // Remove element
    $('.container').on('click','.remove2',function(){
                
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        // Remove <div> with id
        $("#div2_" + deleteindex).remove();
    });                
});