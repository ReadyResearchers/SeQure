![SeQure](img/sequre_logo.png)
# SeQure

+ This is a WordPress form plugin vulnerability scanner that works with WordPress web applications that scans the web for cross-site scripting (XSS) vulnerabilities. It is to prevent and assist programmers with making sure they have sanitized and also updated plugins for stronger security for their web application.

## Overview

Over the years, many web applications are becoming more and more susceptible to being exploited by various vulnerabilities. This is done by programmers not properly sanitizing and checking the plugin code for security purposes and only focusing on functionality of their website. There are many WordPress form plugins that have various updates. However, users are still able to access older, vulnerable versions of most plugins.
*This tool specifically focuses on cross-site scripting.*

## How To Run in Terminal

The program begins by promtpting the user to input a URL that they would like to test. The user can then paste their URL inside of the terminal.

![Beginning Prompt](img/bg_prompt.png)

Once the user pastes their URL inside of the prompt, then the source code for SeQure begins to run. SeQure uses an automated testing software called selenium. Selenium opens up a testing browser, so the user can visibly see the code working. While the browser is up and running, the code will parse through the HTML tags looking for specific tags to find input fields. As selenium is opening, the user will be able to see the URL they entered and see certain scripts being entered into the input fields that the code finds. 

If the script is able to send to the owner's email, then the input fields are not sanitized correctly. If this is the case, then the Wordpress user needs to update their plugin to a more recent version of that specific plugin. On the other hand, if the input fields were properly sanitized then that means that the input fields will not allow the script to be sent to the owner making that version of a plugin safe to use.


## For WordPress Plugin Users!


