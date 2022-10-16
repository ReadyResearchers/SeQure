# SeQure

+ This is a WordPress form plugin scanner that works with WordPress web applications that scans the web for specific vulnerabilities. It is to prevent and assist programmers with making sure they have sanitized and also updated plugins for stronger security for their web application.

## Overview

Over the years, many web applications are becoming more and more susceptible to being exploited by various vulnerabilities. This is done by programmers not properly sanitizing and checking the plugin code for security purposes and only focusing on funcitonality of their website. There are many WordPress form plugins that have various updates. However, users are still able to access older, vulnerable versions of most plugins.
Users who utilize this tool will allow them to see on how many of these test scripts pass. Within this tool, there will also be either a markdown file (.md) or text file (.txt) holding all of the information that was run within the code: how many scripts passed. If scripts do pass, then the plugin itself is vulnerable and needs to be removed or the plugin needs to be updated immediately. *This tool specifically focuses on cross-site scripting.*

## How To Run

The program begins by promtpting the user to input a URL that they would like to test. The user can then paste their URL inside of the terminal.

![Beginning Prompt](img/bg_prompt.png)

Once the user pastes their URL inside of the prompt, then the source code for SeQure begins to run. Next, it detect any open forms and tests the scripts on the URL's input form. If the script is able to pass, then it returns an output of what script was passed and returns a value of `True` meaning that the URL input form is vulnerable. However, if the tool detects a form but none of the scripts pass then it will return a value of `False`.
![Example URL](img/ex_prompt.png)
