This repo contains all the scraping, cleaning, processing code to extract and transform data into clean raw corpus format for doing continued pre-training of LLMs.
Even though model now are trained in a generalized way , that it captures nuances like this. I am doing this to learn about the CPT dataset creation process, how it affects the models accuracy and generalization and more.

## Scraped Websites and Purpose behind them
| Scarped Websites | Purpose for scarping |
|------------------|----------------------|
|tamil2lyrics      |after doing CPT on this data, the model would have knowledge about all in tamil song lyrics. then if SFT is done on a Q&A pairs variant of this data, then model could complete the song the user prompts. or even sing in case it has audio capability.|
