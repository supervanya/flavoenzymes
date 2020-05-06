# from modules.scrapers import scrape_kegg
# from modules.scrapers import scrape_brenda
# from modules.bruce_sorter import BruceSorter_485


# print(dir(scrape_brenda))
# scrape_brenda.printThis('khskd')
# import modules.scrapers
# print(scrape_brenda)

from GLOBALS import KEYWORDS

from modules.scrapers.scrape_driver import create_missing_list
from modules.scrapers.scrape_driver import scrape_all
from modules.scrapers.scrape_driver import write_out


def main():
    # takes into account the whitelist and blacklist
    missing_list = create_missing_list(kegg_keywords=KEYWORDS, brenda_keywords=KEYWORDS)

    # scrapes brenda and kegg
    scraped_results = scrape_all(missing_list)

    # write it out to a file
    if len(scraped_results) > 0:
        write_out(scraped_results)


if __name__ == "__main__":
    main()
