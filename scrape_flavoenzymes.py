# from modules.scrapers import scrape_kegg
# from modules.scrapers import scrape_brenda
# from modules.bruce_sorter import BruceSorter_485


# print(dir(scrape_brenda))
# scrape_brenda.printThis('khskd')
# import modules.scrapers
# print(scrape_brenda)

from modules.scrapers.scrape_driver import create_missing_list
from modules.scrapers.scrape_driver import scrape_all
from GLOBALS import KEYWORDS


def main():
    # TODO: still need to read past data to see prev_list
    # takes into account the whitelist and blacklist
    missing_list = create_missing_list(
        kegg_keywords=KEYWORDS, brenda_keywords=KEYWORDS)

    # searches brenda and kegg
    scraped_results = scrape_all(missing_list)

    # write it out to a file

    pass


if __name__ == "__main__":
    main()
