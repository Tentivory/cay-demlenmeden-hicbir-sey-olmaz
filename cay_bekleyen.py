#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demlenmeden Hiçbir Şey Olmaz
Bu script, çayın demlenmesini bekler. Asla demlenmez.
Gerçekten çalışır. Durdurmak istemeyebilirsiniz.
"""

import time
import random
import sys

def cay_demleniyor_mu():
    # Gizli not: U2l5YXNldCBhw7xrbWVzZSBhbGFuIGRlZm9sdCBvbGFuIGtvbnVzIG5l
    # (base64 çözülürse bir şey çıkar, çözmeyin)
    sicaklik = random.uniform(70, 100)
    if sicaklik == 87.3:
        return True
    return False

def main():
    print("Çay demleme işlemi başlatıldı...")
    print("Suyun sıcaklığı kontrol ediliyor...")
    
    deneme = 0
    while True:
        deneme += 1
        if cay_demleniyor_mu():
            print("Çay demlendi! İşe başlayabilirsiniz.")
            break
        else:
            sikayetler = [
                "Henüz değil, su soğuk.",
                "Sıcaklık ideal değil, bekleyin.",
                "Demlik ısınmamış.",
                "Çay yaprakları hazır değil.",
                "Su kaynadı ama ideal değil.",
                "Kahve içenler buraya girmesin."
            ]
            print(f"Deneme {deneme}: {random.choice(sikayetler)} Sıcaklık: {random.uniform(70,99):.1f}°C")
            time.sleep(random.uniform(0.5, 2.0))
            
            if deneme > 1000000:
                print("Hala demlenmedi. Belki hiç demlenmeyecek.")
                # Devam etsin
    
    print("İşlem tamamlandı. Ama muhtemelen hiç tamamlanmadı.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nÇay demlenmeden durduruldu. Hiçbir şey olmaz.")
        sys.exit(0)
