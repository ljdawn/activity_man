/**
 * Created by Asa on 21/11/15.
 */

$(document).on('change','#id_magazine',function(){
    $.ajax({
        url: '/ajax/mag/activities/'+$(this).val(),
        type: 'GET',
        dataType: "json",
        success: function(data) {
            if (data.code=="ok")
                $("#id_activity").find("option").remove();
                var acts = data.activities;
                for (var i=0; i<=acts.length; i++)
                    {
                        $('<option/>', { value: acts[i][0] }).text(acts[i][1]).appendTo('#id_activity');
                    }
            },
        error: function(e) {
            console.log(e.message);
        }
    });
});
