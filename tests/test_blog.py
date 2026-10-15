import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture(scope="session")
def driver():
    """Test oturumu için tek browser başlat"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # HTML dosyasının tam yolu
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'qa-blog.html'))
    driver.get(f'file:///{file_path}')
    
    yield driver
    
    # Tüm testler bitince browser'ı kapat
    driver.quit()

class TestBlogWebsite:
    
    @allure.feature("Blog Sayfası")
    @allure.story("Sayfa Başlığı Kontrolü")
    @allure.title("Sayfa başlığının doğru olduğunu doğrula")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_title(self, driver):
        """Sayfa başlığının 'Alper Türk - QA Blog' olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        expected_title = "Alper Türk - QA Blog"
        actual_title = driver.title
        
        with allure.step("Sayfa başlığını al"):
            allure.attach(actual_title, name="Actual Title")
        
        assert expected_title in actual_title, f"Expected '{expected_title}' in title, but got '{actual_title}'"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Header Kontrolü")
    @allure.title("Header'da 'Alper Türk - QA Blog' yazısını doğrula")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_header_text(self, driver):
        """Header'da Alper Türk yazısının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        header = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        header_text = header.text
        
        with allure.step("Header metnini al"):
            allure.attach(header_text, name="Header Text")
        
        assert "Alper Türk" in header_text, f"'Alper Türk' not found in header: {header_text}"
        assert "QA Blog" in header_text, f"'QA Blog' not found in header: {header_text}"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Hero Bölümü")
    @allure.title("Hero bölümünde 'Test Otomasyonu' yazısını doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_hero_section(self, driver):
        """Hero bölümünde Test Otomasyonu yazısının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        hero_heading = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".hero h2"))
        )
        hero_text = hero_heading.text
        
        with allure.step("Hero metnini al"):
            allure.attach(hero_text, name="Hero Text")
        
        assert "Test Otomasyonu" in hero_text, f"'Test Otomasyonu' not found in hero: {hero_text}"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Laptop Kontrolü")
    @allure.title("3D laptop elementinin var olduğunu doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_laptop_exists(self, driver):
        """3D laptop elementinin sayfada olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        laptop = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".laptop-3d"))
        )
        
        with allure.step("Laptop elementinin varlığını kontrol et"):
            allure.attach("Laptop elementi bulundu", name="Status")
        
        assert laptop is not None, "Laptop elementi bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Laptop Ekranı")
    @allure.title("Laptop ekranında kod editörünün olduğunu doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_laptop_code_editor(self, driver):
        """Laptop ekranında kod editörünün olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        code_editor = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".code-editor"))
        )
        
        with allure.step("Kod editör elementinin varlığını kontrol et"):
            allure.attach("Kod editörü bulundu", name="Status")
        
        assert code_editor is not None, "Kod editörü bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Kod İçeriği")
    @allure.title("Laptop ekranında Selenium kodunun olduğunu doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_laptop_code_content(self, driver):
        """Laptop ekranında Selenium kodunun olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        code_content = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".editor-content"))
        )
        code_text = code_content.text
        
        with allure.step("Kod içeriğini al"):
            allure.attach(code_text, name="Code Content")
        
        assert "selenium" in code_text.lower(), f"'selenium' not found in code: {code_text}"
        assert "webdriver" in code_text.lower(), f"'webdriver' not found in code: {code_text}"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Blog Kartları")
    @allure.title("Blog kartlarının sayıda olduğunu doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blog_cards_count(self, driver):
        """4 blog kartının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        post_cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".post-card"))
        )
        
        with allure.step(f"Blog kart sayısı: {len(post_cards)}"):
            allure.attach(str(len(post_cards)), name="Card Count")
        
        assert len(post_cards) == 4, f"Expected 4 blog cards, but found {len(post_cards)}"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Blog Kartları")
    @allure.title("Blog kartlarında AI başlığının olduğunu doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_blog_card_selenium(self, driver):
        """Blog kartlarında AI başlığının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        post_cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".post-card h3"))
        )
        # Blog kartlarına scroll yap
        if post_cards:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", post_cards[0])
            import time
            time.sleep(1)
        
        card_titles = [card.text for card in post_cards]
        
        with allure.step("Blog kart başlıklarını al"):
            allure.attach("\n".join(card_titles), name="Card Titles")
        
        # Case-insensitive kontrol
        assert any("AI" in title.upper() for title in card_titles), "AI başlığı bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Blog Kartları")
    @allure.title("Blog kartlarında Java başlığının olduğunu doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_blog_card_cypress(self, driver):
        """Blog kartlarında Java başlığının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        post_cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".post-card h3"))
        )
        # Blog kartlarına scroll yap
        if post_cards:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", post_cards[0])
            import time
            time.sleep(1)
        
        card_titles = [card.text for card in post_cards]
        
        with allure.step("Blog kart başlıklarını al"):
            allure.attach("\n".join(card_titles), name="Card Titles")
        
        assert any("Java" in title for title in card_titles), "Java başlığı bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Hakkımda Bölümü")
    @allure.title("Hakkımda bölümünde Alper Türk yazısını doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_about_section(self, driver):
        """Hakkımda bölümünde Alper Türk yazısının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        about_section = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#hakkimda"))
        )
        # Elemente scroll yap
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", about_section)
        import time
        time.sleep(1)
        about_text = about_section.text
        
        with allure.step("Hakkımda metnini al"):
            allure.attach(about_text, name="About Text")
        
        assert "Alper Türk" in about_text, f"'Alper Türk' not found in about section"
        assert "Adnan Menderes Üniversitesi" in about_text, f"'Adnan Menderes Üniversitesi' not found"
        assert "YBS" in about_text, f"'YBS' not found in about section"
    
    @allure.feature("Blog Sayfası")
    @allure.story("İletişim Bölümü")
    @allure.title("İletişim bölümünde Gmail adresini doğrula")
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_email(self, driver):
        """İletişim bölümünde Gmail adresinin olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        contact_section = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#iletisim"))
        )
        # Elemente scroll yap
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contact_section)
        import time
        time.sleep(1)
        contact_text = contact_section.text
        
        with allure.step("İletişim metnini al"):
            allure.attach(contact_text, name="Contact Text")
        
        assert "turkalper034@gmail.com" in contact_text, f"Gmail adresi bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("İletişim Bölümü")
    @allure.title("İletişim bölümünde LinkedIn linkini doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_contact_linkedin(self, driver):
        """İletişim bölümünde LinkedIn linkinin olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        linkedin_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#iletisim a[href*='linkedin']"))
        )
        
        with allure.step("LinkedIn linkini al"):
            allure.attach(linkedin_link.get_attribute("href"), name="LinkedIn URL")
        
        assert linkedin_link is not None, "LinkedIn linki bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("İletişim Bölümü")
    @allure.title("İletişim bölümünde GitHub linkini doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_contact_github(self, driver):
        """İletişim bölümünde GitHub linkinin olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        github_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#iletisim a[href*='github']"))
        )
        
        with allure.step("GitHub linkini al"):
            allure.attach(github_link.get_attribute("href"), name="GitHub URL")
        
        assert github_link is not None, "GitHub linki bulunamadı"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Navigation")
    @allure.title("Navigation linklerinin tıklanabilir olduğunu doğrula")
    @allure.severity(allure.severity_level.MINOR)
    def test_navigation_links(self, driver):
        """Navigation linklerinin tıklanabilir olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        nav_links = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
        )
        
        with allure.step(f"Navigation link sayısı: {len(nav_links)}"):
            allure.attach(str(len(nav_links)), name="Nav Link Count")
        
        assert len(nav_links) == 3, f"Expected 3 navigation links, but found {len(nav_links)}"
        
        for link in nav_links:
            assert link.is_displayed(), f"Navigation link is not displayed: {link.text}"
            assert link.is_enabled(), f"Navigation link is not enabled: {link.text}"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Footer")
    @allure.title("Footer'da Alper Türk yazısını doğrula")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_footer(self, driver):
        """Footer'da Alper Türk yazısının olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        footer = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        footer_text = footer.text
        
        with allure.step("Footer metnini al"):
            allure.attach(footer_text, name="Footer Text")
        
        assert "Alper Türk" in footer_text, f"'Alper Türk' not found in footer"
        assert "QA" in footer_text, f"'QA' not found in footer"
    
    @allure.feature("Blog Sayfası")
    @allure.story("Video Arka Plan")
    @allure.title("Video elementinin var olduğunu doğrula")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_background_video(self, driver):
        """Arka plan video elementinin olduğunu doğrula"""
        wait = WebDriverWait(driver, 10)
        video = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        
        with allure.step("Video elementinin varlığını kontrol et"):
            allure.attach("Video elementi bulundu", name="Status")
        
        assert video is not None, "Video elementi bulunamadı"
