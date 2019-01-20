# stocks-28protons-com
A project where you can use it to pull information on stocks. I will be adding more features over time. I plan to continue to publish the code for this project for the foreseeable future.

Latest version: 2 (https://www.28protons.com/stocks/v2)

Experimental version: (https://www.28protons.com/stocks/experimental)

The experimental version is using the "current" folder in the repository. It will always have the most up to date changes, but may be broken or in progress changes and may not be that useable.

Changelog:
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
