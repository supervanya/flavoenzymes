# from modules.scrapers import scrape_kegg
# from modules.scrapers import scrape_brenda
# from modules.bruce_sorter import BruceSorter_485


# print(dir(scrape_brenda))
# scrape_brenda.printThis('khskd')
# import modules.scrapers
# print(scrape_brenda) 

from modules.scrapers.fetch_ecs import ec_list

def main():
    L = ec_list()
    L.print()
    L.search_brenda()
    L.search_kegg()
        # takes inro account the whitelist and blacklist
        # searches brenda
        # searches kegg
        
    # kegg_data = scrapers.scrape_kegg()
    # brenda_data = scrapers.scrape_brenda()
    pass

if __name__ == "__main__":
    main();        