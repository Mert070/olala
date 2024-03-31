Mekan = input("Mektep'e girdin, yatakhaneye çıkmak istiyorsan 'yatakhane', sınıflarda kalmak istiyorsan 'sınıf' yaz.\n")
if Mekan == "yatakhane":
  devre = input("Yatakhaneye çıktın. Önünde 5 tane Yatakhane var. Gireceğin yatakhanenin devre numarasını yaz.\n")

  if devre == "160":
    y160 = input("İçeride 60 Puşt anarşist tayfayla kavga çıkardı. Kaçacaksan 'kaçacağım' savaşacaksan 'savaşacağım' yaz.\n")
    if y160 == ("kaçacağım"):
      print("kaçarken 160 İmam'a takıldın, 160 Paşa seni sike sike öldürdü.")
    else:
      print("Savaşırken anarşistler seni kura fırlattı ve öldün.")
  elif devre == "159":
    y159 = input("Yatakhanenin Sağına gideceksen 'sağ' soluna gideceksen 'sol' yaz.\n")
    if y159 == ("sağ"):
      Cork = input("31 Çeken bir pandayla karşılaştın, üzerine koşuyor. Kaçacaksan 'kaçacağım' savaşacaksan 'savaşacağım' yaz.\n")
      if Cork == ("kaçacağım") or ("Kaçacağım"):
        print("Kaçarken Körki'ye çarptın ve seni kura fırlatarak öldürdü.")
      else:
        print("Panda üstüne düştü ve Öldün.")
    else:
      orco = input("Orço'yla karşılaştın, kapitalist olduğunu öğrenmiş, eyvah! Hangi yöne kaçacaksın? Sağa gideceksen 'sağ' sola gideceksen 'sol' yaz\n")
      if orco == ("sağ") or ("Sağ"):
        print("Orco seni yakaladı ve öldürdü.")
      else:
        print("Orco kafana terlik attı ve öldün")
  elif devre == "158":
    a158 = input("158 malo yatakhanesine girilmesine çok sinirlendi, M.Akif'e gitmek istiyorsan 'git', savaşacaksan 'taaruz' yaz.\n")
    if a158 == ("git") or ("Git"):
      print("M.Akif'e gittin, Dicle'ye yakalandın ve senin üstünde zıplayarak seni öldürdü.")
    else:
      i158 = input("Karşında Bora Kocabay ve İlteriş Kılıç var. Hangisiyle savaşacaksın?\n")
      if i158 == ("Bora Kocabay") or ("bora kocabay"):
        print("üstüne atladın ve onu öldürdün ancak Başpet ihanet etti ve senin mabadına kılıç soktu ve öldün.")
      else:
        print("olamaz İlteriş Kılıç yine sinirli, sinirini senden çıkardı ve seni 158 maloyla beraber sikti, hayatının anlamı kalmadığını düşünerek tavsiye vermesi için Ali Önce'ye gittin ve seni potakura fırlatarak sorunu çözdü.")
  elif devre == "157":
    a157 = input("Yatakhaneye girdin, sağında Hamdi solunda Ali Önce var. Hangisine dalacaksın. Eğer Kaçacaksan 'kaçacağım' savaşacaksan savaşacağın kişinin adını yaz.\n")
    if a157 == ("kaçacağım") or ("Kaçacağım"):
      print("Olamaz! dün yemek istemeyen Paşa protein ihtiyacını karşılamak için seni yedi. ")
    elif a157 == ("Ali Önce") or ("ali önce"):
      print("Ali Önce'yle savaşırken paltosu yüzüne geldi, kokudan bayıldın. armut sana takıldı ve üstüne düştü. Altında ezilerek öldün.")
    else:
      print("Hamdi antrenmandan çıkmış olmalı ki yorgun. Hamdiyi tuttun ve aşağı attın. Artık 157 senden korkuyor. Oyunu Kazandın!")
  else:
    a156 = input("Yatakhanenin kapısının önündeyken Buğrahan abiye yakalandın, döneceksen 'dön' içeri gireceksen 'gir' yaz \n")
    if a156 == ("dön") or ("Dön"):
      ("Seni Yakaladı ve vurucuya teslim etti artık kaçış yok. Öldün.")
    else:
      print("İçeride Efe Dalgıç abinin dambıllarına takıldın ve dambılı yamulttun. Çok sinirlenmiş olmalı ki seni Halter yaptı. Yere sert düştün ve öldün")
else:
  print("Sınıfta Erden Tuğcu vardı sözlünü düşük girdi. Sınıfta kaldın ve Nakil aldırdın.")


      



  

