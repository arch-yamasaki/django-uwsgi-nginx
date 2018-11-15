$("form").submit( function(event) {
    event.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.prop("action"),
      method: form.prop("method"),
      data: form.serialize(),
      timeout: 10000,
      dataType: "text",
    })
    .done( function(data) {
        console.log(data);
        $("#id_div_ajax_response").text(data);
    })
  });
