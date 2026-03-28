*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.myntra.com/

*** Test Cases ***
Handling myntra
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=(//a[text()='Women'])[1]
    Mouse Over    xpath=(//a[text()='Women'])[1]

    Click Element    xpath=(//a[text()='Lehenga Cholis'])[1]
    Sleep  2s

    Scroll Element Into View    xpath=//input[@value='Blue']/following-sibling::div
    Click Element    xpath=//input[@value='Blue']/following-sibling::div
    Sleep  2s
    ${name}=  Get Text  (//h3)[1]
    Log To Console  ${name}

    Sleep  2s
    Close Browser
