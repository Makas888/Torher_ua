$(window).load(function(){
     $( "#slider-range" ).slider({
                range: true,
                min: 0,
                max: 50000,
                values: [ 0, 50000 ],
                slide: function( event, ui ) {  $( "#amount" ).val( ui.values[ 0 ] );
                                                $( "#amount1" ).val( ui.values[ 1 ] );
                                                $( "#amount3" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                }
     });
    $( "#amount" ).val( $( "#slider-range" ).slider( "values", 0 ) );
    $( "#amount1" ).val( $( "#slider-range" ).slider( "values", 1 ) );
    $( "#amount3" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) + " - $" + $( "#slider-range" ).slider( "values", 1 ) );
    });