########################## ASIL KONU BURASI KANKA #################################

#Profesyonel kodlamada kullanabileceğin konular unutmaman için not!

#Binary Types

#bytes, bytearry, memoryview


################ İLERİ SEVİYE İSTATİSTİKSEL DAĞILIM FONKSİYONLARI ################

import random

# -----------------------------------------------------------------------------
# betavariate(alpha, beta)
# Beta dağılımına göre 0 ile 1 arasında rastgele sayı üretir.
#
# Matematiksel olarak:
# Beta dağılımı genellikle olasılık oranları (probability proportions)
# modellemek için kullanılır.
#
# Parametreler:
# alpha > 0  (başarı sayısını temsil eder gibi düşünülebilir)
# beta  > 0  (başarısızlık sayısını temsil eder gibi düşünülebilir)
#
# Örneğin: Bayesian istatistikte öncül (prior) dağılım olarak kullanılır.
# Çıktı her zaman 0 ile 1 arasındadır.
# -----------------------------------------------------------------------------

print(random.betavariate(1, 8))


# -----------------------------------------------------------------------------
# expovariate(lambda)
# Üstel (Exponential) dağılıma göre rastgele sayı üretir.
#
# Matematiksel anlamı:
# Sürekli bir olayın gerçekleşme süresini modellemek için kullanılır.
# (örneğin: bir makinenin bozulma süresi)
#
# lambda = olayın gerçekleşme oranı (rate parameter)
# Ortalama = 1 / lambda
#
# Özellik: "Memoryless property" yani geçmişten bağımsızdır.
# -----------------------------------------------------------------------------

print(random.expovariate(0.5))


# -----------------------------------------------------------------------------
# gammavariate(alpha, beta)
# Gamma dağılımına göre rastgele sayı üretir.
#
# Matematiksel kullanım:
# Bekleme süreleri, sigorta modelleri, kuyruk teorisi.
#
# alpha = şekil parametresi (shape)
# beta  = ölçek parametresi (scale)
#
# Eğer alpha tam sayı ise:
# Bu, alpha tane üstel dağılımın toplamı gibi düşünülebilir.
# -----------------------------------------------------------------------------

print(random.gammavariate(100, 2))


# -----------------------------------------------------------------------------
# gauss(mu, sigma)
# Normal (Gaussian) dağılıma göre rastgele sayı üretir.
#
# mu    = ortalama (mean)
# sigma = standart sapma
#
# Çan eğrisi şeklinde simetrik bir dağılımdır.
# Doğal olayların çoğu yaklaşık normal dağılıma uyar:
# boy, sınav puanı, ölçüm hataları vb.
#
# Not: gauss() ile normalvariate() benzerdir,
# fakat algoritma olarak farklı yöntem kullanırlar.
# -----------------------------------------------------------------------------

print(random.gauss(100, 50))


# -----------------------------------------------------------------------------
# lognormvariate(mu, sigma)
# Log-normal dağılıma göre rastgele sayı üretir.
#
# Eğer X normal dağılıyorsa,
# Y = e^X ise Y log-normal dağılıma uyar.
#
# Finans, gelir dağılımı, biyolojik büyüme gibi
# negatif olamayan ve çarpanlı büyüyen sistemlerde kullanılır.
# -----------------------------------------------------------------------------

print(random.lognormvariate(0, 0.25))


# -----------------------------------------------------------------------------
# normalvariate(mu, sigma)
# Normal dağılıma göre rastgele sayı üretir.
#
# gauss() ile benzer iş yapar.
# mu    = ortalama
# sigma = standart sapma
#
# Merkezi Limit Teoremi nedeniyle
# birçok bağımsız rastgele değişkenin toplamı
# yaklaşık normal dağılıma yaklaşır.
# -----------------------------------------------------------------------------

print(random.normalvariate(100, 50))


# -----------------------------------------------------------------------------
# vonmisesvariate(mu, kappa)
# Von Mises dağılımına göre rastgele açı üretir.
#
# Bu dağılım, "dairesel normal dağılım" olarak düşünülebilir.
# Yani yön / açı istatistiklerinde kullanılır.
#
# mu    = ortalama yön (radyan cinsinden)
# kappa = yoğunluk parametresi (büyüdükçe dağılım sıkılaşır)
#
# Kullanım alanları:
# - Rüzgar yönü analizi
# - Jeoloji
# - Navigasyon sistemleri
# -----------------------------------------------------------------------------

print(random.vonmisesvariate(0, 5))


# -----------------------------------------------------------------------------
# paretovariate(alpha)
# Pareto dağılımına göre rastgele sayı üretir.
#
# "80-20 kuralı" (Pareto prensibi) bu dağılıma dayanır.
#
# alpha = şekil parametresi
#
# Gelir dağılımı, şehir nüfusları, internet trafiği gibi
# "ağır kuyruklu" (heavy-tailed) dağılımlarda kullanılır.
#
# Büyük değerler nadirdir ama mümkündür.
# -----------------------------------------------------------------------------

print(random.paretovariate(3))


# -----------------------------------------------------------------------------
# weibullvariate(alpha, beta)
# Weibull dağılımına göre rastgele sayı üretir.
#
# alpha = ölçek parametresi
# beta  = şekil parametresi
#
# Özellikle güvenilirlik mühendisliği ve
# arıza analizlerinde kullanılır.
#
# Eğer beta = 1 ise dağılım üstel dağılıma dönüşür.
# -----------------------------------------------------------------------------

print(random.weibullvariate(1, 1.5))


################################################################################
