# 🧪 Blog Website Test Automation

Profesyonel Selenium + Pytest test otomasyon projesi. Blog web sitesini otomatik test eder ve HTML raporu oluşturur.

## 🌐 Test Edilen Web Sitesi

Bu proje, **Alper Türk** tarafından geliştirilen profesyonel QA & Test Otomasyon blog web sitesini test eder. Web sitesi modern web teknolojileri ve en iyi uygulamalar kullanılarak oluşturulmuştur.

### 🎨 Web Sitesi Özellikleri

#### SEO Optimizasyonu
- ✅ Meta description ve keywords
- ✅ Open Graph meta tagleri (Facebook paylaşımı için)
- ✅ Twitter Card meta tagleri
- ✅ Structured Data (Schema.org JSON-LD)
- ✅ Semantic HTML5 yapısı
- ✅ SEO-friendly URL yapısı

#### Accessibility (Erişilebilirlik)
- ✅ ARIA labels ve aria-hidden attributes
- ✅ Semantic HTML elementleri
- ✅ Keyboard navigasyon desteği
- ✅ Screen reader uyumlu
- ✅ Color contrast uyumu

#### Modern UI/UX
- ✅ Glassmorphism tasarım
- ✅ 3D laptop animasyonu
- ✅ Hareketli video arka plan
- ✅ Smooth scroll navigasyon
- ✅ Parallax efektleri
- ✅ Hover animasyonları
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ Back to Top butonu
- ✅ Hero bölümü CTA butonları
- ✅ Blog kartlarında meta bilgiler
- ✅ Yetenekler bölümü

#### Teknik Detaylar
- ✅ CSS Grid ve Flexbox
- ✅ CSS animasyonları ve transitions
- ✅ JavaScript Intersection Observer
- ✅ Modern CSS backdrop-filter
- ✅ Gradient renkler
- ✅ Box-shadow efektleri
- ✅ Font Awesome iconları

## 📊 Test Sonuçları

✅ **16/16 Test Başarılı** - Tüm testler geçti!

## 🛠️ Kullanılan Teknolojiler ve Araçlar

| Araç | Sürüm | Açıklama | Icon |
|------|-------|----------|------|
| **Python** | 3.12.0 | Programlama dili | 🐍 |
| **Selenium** | 4.15.2 | Web otomasyon framework | 🤖 |
| **Pytest** | 7.4.3 | Test framework | 🧪 |
| **Pytest-HTML** | 3.2.0 | HTML rapor oluşturma | 📄 |
| **Allure-Pytest** | 2.13.2 | Detaylı test raporlama | 📊 |
| **WebDriver Manager** | 4.0.1 | Otomatik driver yönetimi | 🚗 |
| **Chrome** | Son sürüm | Test browser'ı | 🌐 |

## 📋 Test Senaryoları

1. ✅ **Sayfa Başlığı Kontrolü** - Sayfa başlığının doğru olduğunu doğrular
2. ✅ **Header Kontrolü** - Header'da "Alper Türk - QA Blog" yazısını doğrular
3. ✅ **Hero Bölümü** - Hero bölümünde "Test Otomasyonu" yazısını doğrular
4. ✅ **Laptop Kontrolü** - 3D laptop elementinin var olduğunu doğrular
5. ✅ **Laptop Ekranı** - Laptop ekranında kod editörünü doğrular
6. ✅ **Kod İçeriği** - Laptop ekranında Selenium kodunu doğrular
7. ✅ **Blog Kartları** - 4 blog kartının olduğunu doğrular
8. ✅ **Selenium Kartı** - Blog kartlarında Selenium başlığını doğrular
9. ✅ **Cypress Kartı** - Blog kartlarının varlığını doğrular
10. ✅ **Hakkımda Bölümü** - Alper Türk, ADÜ, YBS bilgilerini doğrular
11. ✅ **İletişim Email** - Gmail adresini doğrular
12. ✅ **İletişim LinkedIn** - LinkedIn linkini doğrular
13. ✅ **İletişim GitHub** - GitHub linkini doğrular
14. ✅ **Navigation** - Navigation linklerini doğrular
15. ✅ **Footer** - Footer'da Alper Türk yazısını doğrular
16. ✅ **Video Arka Plan** - Video elementini doğrular

## 🚀 Kurulum

### Gereksinimler

- 🐍 **Python 3.8+** - [İndir](https://www.python.org/downloads/)
- 🌐 **Chrome Browser** - [İndir](https://www.google.com/chrome/)

### Adım 1: Python Kurulumu

1. Python'u [python.org](https://www.python.org/downloads/) adresinden indirin
2. Kurulum sırasında **"Add Python to PATH"** seçeneğini İŞARETLEYİN (çok önemli!)
3. Install Now'a tıklayın
4. Kurulum bitince terminali kapatıp yeniden açın

### Adım 2: Dependencies Kurulumu

Terminali açın ve proje klasörüne gidin:

```bash
cd C:\Users\turka\OneDrive\Desktop\YapayZeka\blog-sayfasi
```

Dependencies'leri kurun:

```bash
pip install -r requirements.txt
```

## 🏃 Testleri Çalıştırma

### Otomatik Script ile (Önerilen)

Windows'ta sadece çift tıklayın:
```
run_tests.bat
```

Bu script:
- Dependencies'leri kurar
- Önceki test sonuçlarını temizler
- Testleri çalıştırır
- HTML raporunu oluşturur
- Raporu tarayıcıda açar

### Manuel Çalıştırma

```bash
# Testleri çalıştır
pytest tests/ --html=report.html --self-contained-html -v

# Raporu aç
start report.html
```

## 📁 Proje Yapısı

```
blog-sayfasi/
├── tests/
│   ├── __init__.py
│   └── test_blog.py          # Selenium testleri
├── index.html                # Test edilecek web sitesi
├── style.css                 # Web sitesi stilleri
├── script.js                 # Web sitesi scriptleri
├── background.mp4            # Arka plan videosu
├── requirements.txt          # Python dependencies
├── run_tests.bat            # Otomatik test koşma scripti
├── README.md                # Bu dosya
└── report.html              # Test raporu (testlerden sonra oluşur)
```

## 🔧 Test Özellikleri

- 🤖 **Selenium WebDriver** - Chrome browser otomasyonu
- 🧪 **Pytest** - Test framework
- 📊 **Allure** - Profesyonel test raporlama
- 📄 **Pytest-HTML** - HTML rapor oluşturma
- 🚗 **WebDriver Manager** - Otomatik driver yönetimi
- ⏱️ **Explicit Waits** - Stabil element bekleme
- 📎 **Attachments** - Test sonuçlarına ek bilgiler
- 🔄 **Session Scope** - Tek browser tüm testler için

## 🎯 Test Severity Seviyeleri

- 🔴 **CRITICAL** - Sayfa başlığı, header
- 🟡 **NORMAL** - Hero bölümü, blog kartları, hakkımda, iletişim
- 🟢 **MINOR** - Kod içeriği, navigation, footer
- ⚪ **TRIVIAL** - Video arka plan

## 📈 Performans İyileştirmeleri

- ✅ **Session Scope Fixture** - Tüm testler için tek browser kullanımı
- ✅ **Explicit Waits** - Stabil element bekleme
- ✅ **Scroll into View** - Elementlerin görünür olduğundan emin olma
- ✅ **Tek Browser** - Çok fazla sekme açılma sorunu çözüldü

## 🎨 Web Sitesi Teknolojileri

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling, animations, glassmorphism
- **JavaScript (ES6+)** - Interactivity, animations
- **Font Awesome 6.4.0** - Icon library

### CSS Özellikleri
- CSS Grid ve Flexbox
- Backdrop-filter (glassmorphism)
- CSS Animations ve Keyframes
- Gradient renkler
- Box-shadow efektleri
- Media queries (responsive)

### JavaScript Özellikleri
- Intersection Observer API
- Smooth scroll
- Event listeners
- DOM manipulation
- Parallax efektleri

### SEO ve Accessibility
- Meta tagleri (description, keywords, author)
- Open Graph (Facebook)
- Twitter Card
- Schema.org Structured Data
- ARIA attributes
- Semantic HTML

## 📝 Notlar

- Testler local HTML dosyası üzerinde çalışır
- Her test oturumunda tek browser açılır
- Test sonuçları `report.html` dosyasında saklanır
- Tüm testler ~14 saniyede tamamlanır
- Web sitesi tamamen responsive tasarım
- SEO ve accessibility uyumlu

## 👨‍💻 Geliştirici

**Alper Türk** - QA & Test Otomasyon Uzmanı

- 📧 Email: turkalper034@gmail.com
- 💼 LinkedIn: [Profil](https://www.linkedin.com/in/alper-t%C3%BCrk-633696386/?isSelfProfile=true)
- 🐙 GitHub: [turkalper034-prog](https://github.com/turkalper034-prog)

## 🎓 Eğitim

**Adnan Menderes Üniversitesi** - Yönetim Bilişim Sistemleri (YBS) Mezunu

## 🛠️ Yetenekler

- Selenium WebDriver
- Cypress
- Python
- Pytest
- JavaScript
- Git
- Test Otomasyonu
- QA Methodolojileri
- Cucumber
-Jenkins
-Postman
-Newman

## 📄 Lisans

Bu proje eğitim ve test amaçlıdır.

## 🚀 Jenkins CI/CD Pipeline

Bu proje Jenkins ile CI/CD pipeline olarak yapılandırılmıştır. Her push işlemi otomatik test çalıştırır.

### Jenkins Kurulum

#### Adım 1: Jenkins Kurulumu

**Windows:**
```bash
# Jenkins indir
# https://www.jenkins.io/download/ adresinden Windows installer'ı indirin
# Kurulumu tamamlayın
# http://localhost:8080 adresinden Jenkins'e erişin
```

**Linux (Ubuntu/Debian):**
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins
```

#### Adım 2: Jenkins Eklentileri

Jenkins'e giriş yaptıktan sonra şu eklentileri kurun:
- **Pipeline Plugin** (varsayılan olarak yüklü)
- **Git Plugin** (varsayılan olarak yüklü)
- **Allure Plugin** (test raporları için)
- **HTML Publisher Plugin** (HTML raporları için)

#### Adım 3: Pipeline Oluşturma

1. Jenkins Dashboard → "New Item"
2. Pipeline adı: `qa-blog-website-pipeline`
3. "Pipeline" seç
4. "OK" tıkla
5. Pipeline konfigürasyonu:
   - **Definition**: Pipeline script from SCM
   - **SCM**: Git
   - **Repository URL**: `https://github.com/turkalper034-prog/qa-blog-website-otomasyon.git`
   - **Branch**: `*/main`
   - **Script Path**: `Jenkinsfile`
6. "Save" tıkla

#### Adım 4: GitHub Webhook (Otomatik Tetikleme)

1. GitHub repository'ye git
2. Settings → Webhooks → "Add webhook"
3. Payload URL: `http://YOUR_JENKINS_URL/github-webhook/`
4. Content type: `application/json`
5. "Just the push event" seç
6. "Add webhook" tıkla

#### Adım 5: Pipeline'ı Çalıştır

1. Jenkins Dashboard → Pipeline'ı seç
2. "Build Now" tıkla
3. Pipeline otomatik olarak çalışır:
   - Checkout
   - Python kurulumu
   - Dependencies kurulumu
   - Test çalıştırma
   - Allure raporu oluşturma
   - Artifact arşivleme

### Docker ile Çalıştırma (Opsiyonel)

Docker kullanarak test ortamını izole edebilirsiniz:

```bash
# Docker image oluştur
docker build -t qa-blog-automation .

# Container içinde testleri çalıştır
docker run --rm -v $(pwd)/report.html:/app/report.html qa-blog-automation
```

### Pipeline Stages

1. **Checkout** - GitHub'dan kod çekme
2. **Setup Python Environment** - Python ortamı hazırlama
3. **Install Dependencies** - Python paketlerini yükleme
4. **Run Tests** - Selenium testlerini çalıştırma
5. **Generate Allure Report** - Allure raporu oluşturma
6. **Archive Artifacts** - Test raporlarını arşivleme

---

**Son Güncelleme:** 15 Ekim 2026
**Test Sonucu:** ✅ 16/16 Başarılı
**Web Sitesi:** ✅ Profesyonel SEO & Accessibility Optimizasyonlu
**Jenkins Pipeline:** ✅ CI/CD Entegre
