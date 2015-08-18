// popup.js 
chrome.tabs.executeScript({code: 'console.log("hello")'});
document.addEventListener('DOMContentLoaded', function() {
    var enabledBox = document.getElementById('enabled');
    if(enabledBox.checked)
        {
            console.log('Enabled');
            chrome.tabs.executeScript({code: 'var pL = document.getElementsByTagName("a").length; console.log(pL);'
            });
        }
        else
        {
            console.log('Disabled');
        }
    enabledBox.addEventListener('change', function() {
        enabledBox.checked = !enabledBox.checked;
    }, false);
}, false);
