 $(document).ready(function() {

 

  $("select.dynamic-option-create-multiple").select2({
    tags: false,
    multiple: true,
  });

  $("select.dynamic-option-create-createTag").select2({
    tags: true,
    multiple: true,
   
  });

  $("select.dynamic-option-create-separate-by-comma").select2({
    tags: true,
    tokenSeparators: [','],
  });
})
