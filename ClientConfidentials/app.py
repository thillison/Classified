from pathlib import Path
import csv
import sys
import fire
import questionary

# Request & Save Client Portfolio Holdings Tickers
def run():

    # set csv file path
    csvpath = Path("ClientConfidentials/Resources/client_tickers.csv")

    # Portfolio Tickers 
    portfolio_tickers = [] 
    csvheader = ["Ticker Symbols"]

    # Prompt Client for Ticker Input
    value = 'yes'
    while value == 'yes':
        client_ticker = questionary.text("Would you please enter the Ticker Symbol of your Portfolio Holding?").ask()
        client_ticker = str(client_ticker)
        share_amount = questionary.text("What is the number of shares you hold in this stock?").ask()
        share_amount = str(share_amount)
        portfolio_tickers.append([client_ticker,share_amount])

            # Write Client Tickers csv file Output
        with open(csvpath, 'w', encoding = 'UTF-8',newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(csvheader)

        # Iterate tickers for csv file output   
            for ticker in portfolio_tickers:
                csvwriter.writerow([ticker[0],ticker[1]])

        # Prompt User to Continue or Not
        value = questionary.text("Would you like to enter another Ticker from your Portfolio? Type: yes or no").ask()
                    
    # Confirmation .csv file was saved
    print("client_tickers.csv Saved!") 


# Fire Main
if __name__ == "__main__":
    fire.Fire(run)