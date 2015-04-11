
/*Creates tabpanel according to tabpanel_data*/
function create_tabs(tabpanel_data, tabs_pos) {

    keys = Object.keys(tabpanel_data); // tabs names
    if (keys == 0) {
        return;
    }
    var tab_intern = "<ul class='nav nav-tabs' role='tablist'></ul><div class='tab-content'></div>";
    if (tabs_pos == 'bottom') {
        tab_intern = "<div class='tab-content'></div><ul class='nav nav-tabs' role='tablist'></ul>";
    }

    var newtabs = "<div id='tab-container' class='tabs-" + tabs_pos +
                  "' role='tabpanel'>"+tab_intern+"</div>" ;

    var main_container = "#content";
    $(newtabs).insertBefore('#content-main'); // Position for new tabpanel


    // Get all fieldsets and inlines
    var fsets = $(main_container).find("fieldset").not("._inline-group fieldset");
    var inlines = $(main_container).find("div._inline-group"); 

    for (var i = 0; i <  keys.length; i++) { 

        // Add anchor (tab header)    
        $("#tab-container ul").append("<li role='presentation'><a role='tab' \
                                       data-toggle='tab' aria-controls='#tabs-"+ i +
                                       "' href='#tabs-" + i + "'>"+keys[i]+"</a></li>");
        // Add tab content
        $("#tab-container div.tab-content").append("<div role='tabpanel' class='tab-pane fade' id='tabs-"+  i +"'></div>");
        
        // Add tab contents (relocate django html: fieldsets, and inline)
        var entries = tabpanel_data[keys[i]];
        for (var j=0; j < entries.length; j++){
            var e = entries[j];
            var pos = e[0];

            if (e[1] == 'f') {
                // Fieldset
                $(fsets[pos]).appendTo("#tabs-" + i); 
            }
            else {
                // Inline
                $(inlines[pos]).appendTo("#tabs-" + i); 
            }
        }
    }

    $('#tab-container a:first').tab('show');

  }
