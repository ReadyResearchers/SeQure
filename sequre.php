<?php
/**
* Plugin Name: SeQure
* Plugin URI: https://github.com/ReadyResearchers/SeQure
* Description: Test.
* Version: 0.1
* Author: Alexis Caldwell
* Author URI: https://lex.chompe.rs/
**/

// Import the necessary classes
use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;


function reflected(){

    $host = 'http://localhost:4444/wd/hub';
    // Set up the desired capabilities for the browser you want to use
    $capabilities = DesiredCapabilities::chrome();

    // Create a new RemoteWebDriver instance with the desired capabilities
    $driver = RemoteWebDriver::create(
        'http://localhost:4444/wd/hub',
        $capabilities
    );

    // Use the RemoteWebDriver instance to navigate to a website
    $driver->get('https://lex.chompe.rs/contact-form-7-v4/');

    // Use the findElement method to locate an element on the page and interact with it
    $searchBox = $driver->findElement(WebDriverBy::name('q'));

    // Use the sendKeys method to enter text into the element
    $searchBox->sendKeys('Selenium with PHP');

    // Use the submit method to submit the form
    $searchBox->submit();

    // Close the browser
    $driver->quit();
}

echo "Welcome to SeQure!";
reflected();

?>