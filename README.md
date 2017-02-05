## Description

This is a simple [scrapy](https://scrapy.org/)-based project which allows grabbing all dead links from a website.

To start using it, it is highly recommended to create a virtual environment in order to not mixing installed packages with system ones.

So, the first to run the `dead_links_spider` clone this repository. Next, do the following:

`cd dead_links_spider`

`mkvirtualenv dead_links_spider -a .`

Now, when the virtual environment has been created, install requirements from `requirements.txt` file.

`pip install -r requirements.txt`

At this moment you're able to list all available spiders. In this case, we have only one:

`scrapy list`

The output you should see:

`dead-links-spider`

If everything has been done correctly, you can start scrapping your website trying to find dead links. To do that you can either run the following scrapy command:

`scrapy crawl dead-links-spider -o results.json`

Or you can also run a bash wrapped:

`run.sh results.json`

All results retrieved by spiders will be collected in results.json file in JSON format.

**Note**: `run.sh` script takes the first input parameter as a name of result file if there weren't specified one it will use default name `results.json`.

To see the broken urls stored in results.json file run the following bash command:

`cat results.json | jq . | grep url`

To set the target URLs and domains take a look `settings.py` configuration file. There you can find 2 constant ALLOWED_DOMANS and START_URLS that determine the spider's behavior.
