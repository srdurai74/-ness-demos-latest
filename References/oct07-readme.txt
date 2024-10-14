References:
https://devhints.io/xpath
https://flukeout.github.io/

Selenium
   - IDE
       - record and playback
   - WebDriver
       - Scripting
   - Grid
       - Cross browser testing


WebDriver architecture

3.x
Scripts -> Selenium client library --> Drivers -->  Browsers
                                JSON Protocol

4.x
W3C protocol is used instead of JSON Protocol

driver.get('https://ebay.com')
    - REST API call
        - GET
        - http://localhost:7055/...
        - {
            "url":"https://ebay.com"
          }

chromedriver.exe

WebElements
    Textfield
    button
    dropdowns
    text
    links
    checkboxes
    radio buttons

Operations that can be performed on the Web Elements
    send keys
    click
    clear
    submit

Web Elements can be identified using:

    tagname
    id - 1st choice
    name - 2nd
    classname - 2nd
    link text
    partial link text
    xpath
    css selectors

<p id="">Sample text</p>

class="
 oxd-button
 oxd-button--medium
 oxd-button--main
 orangehrm-login-button"

Absolute xpath
/html
   /body
      /div[1]
        /div[1]
          /div
            /div[1]
              /div
                /div[2]
                  /div[2]
                   /form
                     /div[3]
                       /button

Relative xpath
    //*[@id="app"]
        /div[1]
            /div
                /div[1]
                    /div
                        /div[2]
                            /div[2]
                                /form
                                    /div[3]
                                        /button