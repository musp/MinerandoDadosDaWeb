/**
 * Created by mauricio on 16/02/16.
 */
$.getJSON( 'http://localhost:5000/todo/api/v1.0/tasks/'+document.getElementsByClassName('table table-bordered')[0], function( json ) {console.log(document.getElementsByClassName('table table-bordered')[0]); });


$.ajax({ type: "PUT", url: 'http://localhost:5000/todo/api/v1.0/tasks/', data: jQuery(document.body.getElementsByTagName('table')[0]).text(), success: true});
$.post( 'http://127.0.0.1:5000/todo/api/v2.0/tasks/', { table:jQuery(document.body.getElementsByTagName('table')[0])} );



document.body.getElementsByTagName('fieldset')[0].outerText+'***'+document.body.getElementsByTagName('fieldset')[1].outerText+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerText+'***'+document.body.getElementsByTagName('fieldset')[4].outerText+'***'+document.body.getElementsByTagName('fieldset')[5].outerText

                                                       document.body.getElementsByTagName('fieldset')[0].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[1].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[4].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[5].outerHTML
$.getJSON('http://127.0.0.1:5000/todo/api/v2.0/tasks/'+document.body.getElementsByTagName('fieldset')[0].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[1].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[4].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[5].outerHTML, function( json ) {console.log(document.getElementsByClassName('table table-bordered')[0]); });