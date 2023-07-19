odoo.define("wb_portal.NewStudentForm", function(require){
'use strict';
console.log("Hi this is for the testing purpose log write down.");
var publicWidget = require("web.public.widget");

publicWidget.registry.NewStudentForm = publicWidget.Widget.extend({
    selector:"#new_student_creation",
    events:{
        'submit': "_onSubmitButton",
    },

    _onSubmitButton: function(evt){
        var studentName = this.$("input[name='name']").val();
        var $schoolName = this.$("select[name='school']");
        var school_name = ($schoolName.val() || '0');
        if(!studentName){
            $("#student_client_side_validation_message").html("Please enter student name.");
            $("#student_client_side_validation_message").show();
            evt.preventDefault();
        }
        if(!school_name || school_name == '0'){
            $("#student_client_side_validation_message").html("Please select school.");
            $("#student_client_side_validation_message").show();
            evt.preventDefault();
        }
        if(!school_name.match(/^[0-9]+$/)){
            $("#student_client_side_validation_message").html("Please select proper school option.");
            $("#student_client_side_validation_message").show();
            evt.preventDefault();
        }
        //        console.log("Hello This submit button clicked!");
//        alert("Hi");
    },
});
});