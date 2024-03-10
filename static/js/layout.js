// !function(){"use strict";var t,a,e;sessionStorage.getItem("defaultAttribute")&&(t=document.documentElement.attributes,a={},Object.entries(t).forEach(function(t){var e;t[1]&&t[1].nodeName&&"undefined"!=t[1].nodeName&&(e=t[1].nodeName,a[e]=t[1].nodeValue)}),sessionStorage.getItem("defaultAttribute")!==JSON.stringify(a)?(sessionStorage.clear(),window.location.reload()):((e={})["data-layout"]=sessionStorage.getItem("data-layout"),e["data-sidebar-size"]=sessionStorage.getItem("data-sidebar-size"),e["data-layout-mode"]=sessionStorage.getItem("data-layout-mode"),e["data-layout-width"]=sessionStorage.getItem("data-layout-width"),e["data-sidebar"]=sessionStorage.getItem("data-sidebar"),e["data-sidebar-image"]=sessionStorage.getItem("data-sidebar-image"),e["data-layout-direction"]=sessionStorage.getItem("data-layout-direction"),e["data-layout-position"]=sessionStorage.getItem("data-layout-position"),e["data-layout-style"]=sessionStorage.getItem("data-layout-style"),e["data-topbar"]=sessionStorage.getItem("data-topbar"),Object.keys(e).forEach(function(t){e[t]&&e[t]&&document.documentElement.setAttribute(t,e[t])})))}();



// (function() {
//     "use strict";
    
//     var attributes, storedAttributes, defaultAttributes;

//     // Retrieve stored default attributes from sessionStorage
//     storedAttributes = sessionStorage.getItem("defaultAttribute");

//     // If default attributes are stored
//     if (storedAttributes) {
//         // Get the attributes of the document element
//         attributes = document.documentElement.attributes;

//         // Initialize an object to store attribute name-value pairs
//         defaultAttributes = {};

//         // Iterate through each attribute
//         Object.entries(attributes).forEach(function(item) {
//             var attrName, attrValue;

//             // If the attribute has a name and it's not undefined
//             if (item[1] && item[1].nodeName && item[1].nodeName !== "undefined") {
//                 // Get attribute name and value
//                 attrName = item[1].nodeName;
//                 attrValue = item[1].nodeValue;

//                 // Store attribute name-value pair
//                 defaultAttributes[attrName] = attrValue;
//             }
//         });

//         // If stored default attributes don't match current attributes
//         if (storedAttributes !== JSON.stringify(defaultAttributes)) {
//             // Clear sessionStorage
//             sessionStorage.clear();
//             // Reload the page
//             window.location.reload();
//         } else {
//             // Initialize an object to store data attributes
//             var dataAttributes = {};

//             // Retrieve data attributes from sessionStorage
//             dataAttributes["data-layout"] = sessionStorage.getItem("data-layout");
//             dataAttributes["data-sidebar-size"] = sessionStorage.getItem("data-sidebar-size");
//             dataAttributes["data-layout-mode"] = sessionStorage.getItem("data-layout-mode");
//             dataAttributes["data-layout-width"] = sessionStorage.getItem("data-layout-width");
//             dataAttributes["data-sidebar"] = sessionStorage.getItem("data-sidebar");
//             dataAttributes["data-sidebar-image"] = sessionStorage.getItem("data-sidebar-image");
//             dataAttributes["data-layout-direction"] = sessionStorage.getItem("data-layout-direction");
//             dataAttributes["data-layout-position"] = sessionStorage.getItem("data-layout-position");
//             dataAttributes["data-layout-style"] = sessionStorage.getItem("data-layout-style");
//             dataAttributes["data-topbar"] = sessionStorage.getItem("data-topbar");

//             // Iterate through each data attribute
//             Object.keys(dataAttributes).forEach(function(attr) {
//                 // If data attribute has a value, set it on the document element
//                 if (dataAttributes[attr]) {
//                     document.documentElement.setAttribute(attr, dataAttributes[attr]);
//                 }
//             });
//         }
//     }
// })();


(function() {
    "use strict";

    // Retrieve stored values from session storage
    var storedValues = JSON.parse(sessionStorage.getItem("layoutPreferences"));

    // If there are stored values, apply them to the document element
    if (storedValues) {
        Object.keys(storedValues).forEach(function(attribute) {
            var storedValue = storedValues[attribute];
            var currentValue = document.documentElement.getAttribute(attribute);

            // Check if the current attribute value matches the stored value
            if (currentValue !== storedValue) {
                // If there's a mismatch, update the attribute and store the new value
                document.documentElement.setAttribute(attribute, storedValue);
            }
        });
    }
})();
