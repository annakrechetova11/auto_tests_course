import pytest

from utils.file_utils import FileUtils
from utils.user_utils import UsersData
from utils.login_utils import Login
from utils.ukr_net_utils import UkrNetEmail
from utils.browsers import Browsers


class TestMail:

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.users_data = UsersData()
        self.file_utils = FileUtils()
        self.chrome_browser = Browsers()
        self.chrome_browser.invoke_chrome_browser()
        self.login_page = Login(page=self.chrome_browser.page)
        self.ukr_net_utils = UkrNetEmail(page=self.chrome_browser.page)

    def test_send_text_file_gmail(self):
        string_text = "Hello!"
        self.chrome_browser.navigate_to_page(url=self.ukr_net_utils.ukr_net_url)
        self.login_page.login(password=self.users_data.senders['password'], login=self.users_data.senders['username'])
        self.login_page.login_check(context=self.chrome_browser.context)
        self.file_utils.create_and_read_file(string_text=string_text, file_name="greetings.txt")
        self.ukr_net_utils.fill_the_email_data(email=self.users_data.recipients_list['emails'],
                                               subject_text=string_text)
        self.ukr_net_utils.copy_and_paste_body_text(body_text=string_text)
        self.ukr_net_utils.send_email()
