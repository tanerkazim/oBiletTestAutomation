from base.base_functions import *
from pages.main_page import MainPage


class TestUserRegistration(BaseClass):
    """Test case:

    1. Ana sayfası açılır ve sayfanın doğru şekilde açıldığı kontrol edilir.
    2. Üye giriş butonuna tıklanır. Üyelik Pop-Up'ının açıldığı görülür. Üye ol butonuna tıklanır.
    3. Mail ve Password alanı girilerek üye ol butonuna tıklanır.
    4. Yeni kullanıcının başarılı şekilde oluşturulduğu kontrol edilir.

    """

    def setUp(self):
        self.methods = BaseClass()
        self.driver = self.methods.get_driver()

    def runTest(self):
        # 1. Ana sayfası açılır ve sayfanın doğru şekilde açıldığı kontrol edilir.
        main_page = MainPage(self.methods)

        # 2. Üye giriş butonuna tıklanır. Üyelik Pop-Up'ının açıldığı görülür. Üye ol butonuna tıklanır.
        login_popup = main_page.navigate_to_login()
        self.assertTrue(login_popup.login_form_presence())
        login_popup.navigate_to_signup()
        self.assertTrue(login_popup.register_form_presence())

        # 3. Mail ve Password alanı girilerek üye ol butonuna tıklanır.
        login_popup.fill_email()
        login_popup.fill_password()
        login_popup.complete_register()
        # 4. Yeni kullanıcının başarılı şekilde oluşturulduğu kontrol edilir.
        self.assertTrue(main_page.user_profile_presence())

    def tearDown(self):
        self.driver.quit()
