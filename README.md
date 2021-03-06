# stocks-28protons-com
A project where you can use it to pull information on stocks. I will be adding more features over time. I plan to continue to publish the code for this project for the foreseeable future.


Latest version: 3.2 (https://stocks.28protons.com/)

Due to the new IEX API, versions older than 3.1 no longer work and I do not plan on modifying the code to make them work at the moment.

Changelog:
Version 3.2
- Moved the website to a different server not on aws or amazon rds since it cost more than my shared webserver.
- Adapted the DBInterface class to utilize mysql using PyMySQL instead of postgres.
- Removed ability to see after hours information because the IEX api doesn't supply it by default any longer.
- Some other minor changes to accomodate the move to the new server.

Version 3.1:
- Updated to use the new IEX api.

Version 3:
- Mobile formatting fixes
- Fixed up css so that the site no longer looks weird on iOS devices.
- Symbol Updater now runs and grabs the valid symbols each day.
- Symbol validator runs whenever the user inputs stock symbols into the input field.
- The validator will check the database of valid symbols and only display ones that are valid instead of asking the api for invalid stocks, which would then unintentionally return no results.

Version 2:
- Updated UI
    - Enjoy a basic light mode UI for the stocks.
    - Each stock only displays its latest price instead of latest price, open, close, 52 week high, 52 week low.
- Added change in price from the previous close. It is displayed next to the latest price in both the number of dollars that changed as well as the percentage. Ex: 20.48 +0.5(+2.5%)
- Added extended hours pricing. This will display below the latest price when it is no longer market hours for the stock.
- Extended hours pricing will also differentiate between pre-market and after hours periods even during days when the exchange is closed.
- Implemented templating system for the front end via php.
- Refactored parts of the backend to be more flexible in accomodating multiple types of stock requests.
- Stock symbols now appear in the order that the user typed them in in the input box.
- Changes in the Dow Jones, S&P 500, and the Nasdaq 100 are now displayed on the page.
