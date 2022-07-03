from base.base_functions import *
from pages.main_page import MainPage


class TestFlightTicketSearch(BaseClass):
    """Test case

    1. Obilet ana sayfasına girilerek Uçak tabine tıklanır ve Uçak bileti aramasayfasının açıldığı görülür.
    2. Bir gidiş ili ve gidiş tarihi , bir dönüş ili ve dönüş tarihi seçilir.
    3. Seçimler yapıldıktan sonra uçuş ara butonuna tıklanır ve uçuşlarınlistelendiği görülür.
    4. Uçuşlardan herhangi bir gidiş uçuşu seçilir.
    5. Uçuşlardan herhangi bir dönüş uçuşu seçilir.
    6. Ödeme sayfanın başarılı şekilde açıldığını ödeme sayfasındaki gidiş ve dönüş uçusunun seçilen
    gidiş ve dönüş uçuşu olduğu teyit edilir.

    """

    def setUp(self):
        self.methods = BaseClass()
        self.driver = self.methods.get_driver()

    def runTest(self):
        # 1. Obilet ana sayfasına girilerek Uçak tabine tıklanır ve Uçak bileti aramasayfasının açıldığı görülür.
        main_page = MainPage(self.methods)
        flight_search_page = main_page.navigate_to_flight_search()

        # 2. Bir gidiş ili ve gidiş tarihi , bir dönüş ili ve dönüş tarihi seçilir.
        selected_origin = flight_search_page.fill_origin()
        self.assertIn(self.methods.get_from_ini("origin_city"), selected_origin)
        selected_destination = flight_search_page.fill_destination()
        self.assertIn(self.methods.get_from_ini("destination_city"), selected_destination)
        flight_search_page.fill_departure()
        flight_search_page.fill_return()

        # 3. Seçimler yapıldıktan sonra uçuş ara butonuna tıklanır ve uçuşlarınlistelendiği görülür.
        flights_page = flight_search_page.search_flights()

        # 4. Uçuşlardan herhangi bir gidiş uçuşu seçilir.
        flights_page.select_random_departure_flight()
        # 5. Uçuşlardan herhangi bir dönüş uçuşu seçilir.
        cart_page = flights_page.select_random_return_flight()

        # 6. Ödeme sayfanın başarılı şekilde açıldığını ödeme sayfasındaki gidiş ve dönüş uçusunun seçilen
        # gidiş ve dönüş uçuşu olduğu teyit edilir.
        flights_data = cart_page.get_flights_data()
        self.assertIn(flights_page.departure_flight_code, flights_data)
        self.assertIn(flights_page.return_flight_code, flights_data)

    def tearDown(self):
        self.driver.quit()
