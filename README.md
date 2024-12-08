# 3DRoomWithPyOpenGL

## Proje Hakkında

Bu proje, 3 boyutlu uzayda bir 3B model oluşturarak çeşitli geometrik nesneler eklenmesini, yüzey kaplamalarının uygulanmasını ve aydınlatma modelleriyle sahnenin gerçekçi bir şekilde aydınlatılmasını amaçlamaktadır. Proje, İstanbul Ticaret Üniversitesi Bilgisayar Mühendisliği BİL333 Bilgisayar Grafikleri dersi kapsamında gerçekleştirilmiştir.

---

## Grup Bilgileri

| Okul Numarası | Grup Üyeleri       | Görev Dağılımı                                             |
| ------------- | ------------------ | ---------------------------------------------------------- |
| 200030012     | Ahmet Servet Polat | Proje yönetimi, odanın oluşturulması                       |
| -             | Kenan Koçoğlu      | Işık kaynaklarının oluşturulması, nesnelerin oluşturulması |
| -             | Mehmet Enes Odabaş | Nesne kaplamaları ve aydınlatma modelinin oluşturulması    |

---

## Proje Özellikleri

### Geometrik Nesneler

-   **Küre:** Merkezi odanın ortasına yerleştirilir. (Kırmızı)
-   **Küp:** Bir köşeye yerleştirilir. (Mavi)
-   **Piramit:** Çapraz köşeye konumlandırılır. (Yeşil)
-   **Silindir:** Diğer bir köşeye dik olarak yerleştirilir. (Sarı)

### Parlak ve Mat Yüzeyler

-   **Parlak Yüzeyler:** Küre ve küp
-   **Mat Yüzeyler:** Piramit ve silindir
-   Malzeme özellikleri (ambient, diffuse, specular) doğru şekilde ayarlanarak kontrast sağlanır.

### Kapalı Oda

-   Dikdörtgen prizma şeklinde tasarlanmıştır.
-   Duvarlar, taban ve tavan basit düzlemlerle oluşturulmuştur.
-   Kamera, odanın köşelerinden birine yerleştirilerek sahnedeki tüm nesneler görüntülenir.

### Işık Kaynakları

-   **Ortam Işığı:** Tüm sahneyi düşük seviyede aydınlatır.
-   **Alan Işığı:** Bir duvar boyunca yayılan ışık sağlar.
-   **Nokta Işığı:** Kürenin üzerine odaklanmıştır.
-   (Opsiyonel) **Yönlü Işık:** Genel aydınlatma sağlar.

### Aydınlatma Modeli

-   **Phong Aydınlatma Modeli** kullanılmıştır.
    -   Ambient (Ortam)
    -   Diffuse (Yayılma)
    -   Specular (Yansıma)
-   Global aydınlatma uygulanarak gerçekçi bir ışık yayılımı sağlanmıştır.

---

## Kullanılan Teknolojiler ve Araçlar

-   **Programlama Dili:** Python
-   **Kütüphaneler:** PyOpenGL
-   **Araçlar:**
    -   Docker (Deployment için)
    -   venv (Sanal ortam yönetimi için)

---

## Projenin Çalıştırılması

---

## Projeye Ait Ekran Çıktıları

-   Modelin, nesnelerin ve ışıklandırmanın ekran görüntüleri proje dosyalarında yer almaktadır.
