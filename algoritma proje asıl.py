print("----------------------uygulamamıza hoşgeldiniz---------------------------\n")

username="iemirerdogan07"
password="abc123"


print("uygulamdan çıkmak isterseniz 5 e basınız")
print("devam etmek için 1 e basınız")
check=input("basınız:")

if check=="1":
 print("--BİLGİLENDİRME--")
 print("karşınıza 2 tane soru çıkacak:1-üye oldunuz mu?\n2-şifrenizi unuttunuz mu?\nkendi durumunuza göre gelen soruları cevaplayınız.")
 #--> üye olma kısmı
 uye=input("üye oldunuz mu?:")
 if uye=="hayır":
     username=input("kullanıcı adınızı oluşturunuz:")
     password=input("şifre oluşturunuz:")
     print("başarıyla üye olunmuştur")
 elif uye=="evet":    
     print("giriş yapma kısmına geçiniz\n")


#--> giriş yapma kısmı
   
 while True:
      kullaniciadi=input("kullanıcı adınızı giriniz:")
      if kullaniciadi==username:
           print("kullanıcı adınız doğrudur")
           break
      else:
           print("kullanıcı adınız yanlıştır bir daha deneyin")
           continue
    
#-->şifremi unuttum kısmı
 kontrol=input("şifrenizi unuttunuz mu?:")
 if kontrol=="evet":
     password=(input("şifrenizi oluşturunuz:"))
     print("şifreniz oluşturuldu")
 elif kontrol=="hayır":
     print("devam ediniz\n")


 while True:
     
       sifre=input("şifrenizi giriniz:")
       if sifre==password:
           print("şifreniz doğrudur")
           print("uygulamaya giriş yapılmıştır")
           break
       else:
           print("şifreniz yanlıştır tekrar deneyin")
           continue
          
elif check=="5":
    print("uygulamadan çıkıldı\niyi günler dileriz:)")

          

          


      
        
      
