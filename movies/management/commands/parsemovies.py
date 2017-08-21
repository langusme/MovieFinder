from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
import datetime
import schedule
from time import sleep
from movies.models import Movie

class Command(BaseCommand):
    help = "Scrapes eBroadcast for today's movies"

    def handle(self, *args, **options):
        print("demo demo demo")

        print("Getting Datetime Information")
        now = datetime.datetime.now()
        dateSTR = datetime.date(day=now.day, month=now.month, year=now.year).strftime('%A %d %B %Y')
        print("It is ", dateSTR)
        print("Getting Movies")
        url = 'http://www.ebroadcast.com.au/tv/movies'
        page = requests.get(url)
        htmlTxt = page.text

        times, names, channels = [], [], []

        print("Parsing Movies Into Tables")
        htmlBS = BeautifulSoup(htmlTxt, 'html.parser')
        table = htmlBS.find('table', class_="table table-hover").find('tbody')
        for row in table.findAll('tr'):  # Iterates through each row in the table body
            # print(row.prettify())
            cells = row.findAll('td')
            times.append(cells[0].find('h5').text)
            names.append(cells[1].find('h5').text)
            if (cells[2].h5 == None):
                channels.append(cells[3].h5)
            else:
                channels.append(cells[2].h5)

        # Make it so that it just adds to same file, and add tha ir date in A column

        # b = names.__len__() + a
        # col = [x for x in range(a, b)]
        print("Adding Movies to Database")
        for x in range(names.__len__()):
            print("a")
            movie = Movie(movie_name=names[x], channel=channels[x].text, air_date=now.date(), air_time=datetime.datetime.strptime(times[x], '%I:%M %p'))
            movie.save()
            # num = col[x] + 2
            # ws['A' + str(num)] = dateSTR
            # ws['B' + str(num)] = times[x]
            # ws['C' + str(num)] = names[x]
            # ws['D' + str(num)] = channels[x].text

        # a += names.__len__()
        # ws['E1'] = a
        # print("Saving Spreadsheet")
        # wb.save('Movie.xlsx')
        print("\n\nScript has finished for", dateSTR + ". You can now open and view the spreadsheet.")
        print(
            "\n\nThis script will automatically run at 10:00am tomorrow if you leave this window open.\nOtherwise just run it again tomorrow, and it will add tomorrow's movies to the current spreadsheet.")
        print("\nMade by Liam Angus")