# PeaFree!
[PeaFree!](https://www.peafree.info) is a Django application which allows users to search for foods that meet new FDA recommendations for dog foods (no peas, potatoes, legumes, or pulses as main ingredients).

The data used by the application is supplied by my [Multithreaded-Chewy-Scraper](https://github.com/MikeAleksa/Multithreaded-Chewy-Scraper) and stored in a MySQL database. Regular Expressions are used to examine ingredients of foods, to classify whether they contain discouraged ingredients or not. Discouraged ingredients are highlighted to show why a food is considered to go against current FDA recommendations.

The production version of this application can be found at [PeaFree.info](https://www.peafree.info), and is deployed using AWS Elastic Beanstalk and AWS RDS.
