from django.core.management.base import BaseCommand
import facts.crawler as crawler


class Command(BaseCommand):
    help = "My shiny new management command."

    #
    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        # crawler.get_all_artists()
        # crawler.get_all_songs()
        crawler.get_all_facts()
